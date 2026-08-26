from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pathlib, re, hashlib
from ..core.database import get_sqlite_conn
from ..core.product_images import get_product_image

router = APIRouter()
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

def normalize_name(name: str) -> str:
    """Normalise pour déduplication: enlève lot, tailles, couleurs"""
    n = name.lower()
    # Enlève lot, pcs, etc
    n = re.sub(r'lot\s*\d+|-\s*lot.*|70\s*pcs|60\s*pcs|50\s*pcs|40\s*pcs|30\s*pcs|20\s*pers|15\s*pers|10\s*pers|\d+\s*pcs|\d+\s*pers', '', n)
    n = re.sub(r'rose|bleu|or|gold|blanc|noir|pastel|fille|garçon|garcon', '', n)
    n = re.sub(r'[^a-z0-9]+', ' ', n)
    return n.strip()

def deduplicate_products(products):
    """Supprime doublons: même nom normalisé + même event_type -> garde 1 (meilleure marge/stock)"""
    seen = {}
    unique = []
    for p in products:
        d = dict(p)
        norm = normalize_name(d.get('name','')) + '|' + (d.get('event_type','') or '')
        # Clé plus précise: si kit, on garde distinction
        if 'kit' in d.get('slug','') and 'kit' in norm:
            # Garde kits séparés si prix diff >20
            norm = norm + '|' + str(int(d.get('price_ttc',0)//20))
        
        if norm not in seen:
            seen[norm] = d
            unique.append(d)
        else:
            # Garde celui avec stock + featured
            existing = seen[norm]
            # Si nouveau a plus de stock ou featured, remplace
            if (d.get('is_featured',0) > existing.get('is_featured',0)) or (d.get('stock_qty',0) > existing.get('stock_qty',0)*1.5):
                # Remplace dans unique
                idx = next((i for i, x in enumerate(unique) if normalize_name(x.get('name',''))+'|'+(x.get('event_type','') or '') == norm), None)
                if idx is not None:
                    unique[idx] = d
                seen[norm] = d
            # Sinon ignore doublon
    return unique

def enrich_products(products):
    enriched = []
    for p in products:
        d = dict(p) if not isinstance(p, dict) else p
        d['image_url'] = get_product_image(d)
        # Couleur de fond unique basée sur hash slug pour éviter répétition visuelle
        h = int(hashlib.md5(d.get('slug','').encode()).hexdigest()[:6], 16)
        hue = h % 360
        # Palette douce
        d['bg_color'] = f"hsl({hue}, 35%, 96%)"
        d['accent_color'] = f"hsl({hue}, 60%, 70%)"
        enriched.append(d)
    return enriched

@router.get("/explorer", response_class=HTMLResponse)
def explorer(request: Request, event: str = None, filter: str = None, q: str = None, couleur: str = None, theme: str = None, age: str = None):
    conn = get_sqlite_conn()
    try:
        # Base query
        sql = "SELECT * FROM products WHERE is_active=1"
        params = []
        if event and event != 'all' and event != 'kits':
            sql += " AND event_type=?"
            params.append(event)
        if event == 'kits':
            sql += " AND (name LIKE '%Kit%' OR slug LIKE '%kit%' OR price_ttc > 60)"
        
        # Filtres additionnels
        if filter:
            if filter == 'kit':
                sql += " AND (name LIKE '%Kit%' OR slug LIKE '%kit%')"
            elif filter == 'perso':
                sql += " AND (name LIKE '%Personnalis%' OR slug LIKE '%personnalis%' OR slug LIKE '%perso%')"
            elif filter in ['rose','bleu','or','gold','blanc','noir']:
                sql += " AND (name LIKE ? OR slug LIKE ?)"
                params.extend([f"%{filter}%", f"%{filter}%"])
        
        if q:
            sql += " AND (name LIKE ? OR short_desc LIKE ? OR slug LIKE ?)"
            params.extend([f"%{q}%", f"%{q}%", f"%{q}%"])
        
        if couleur:
            sql += " AND (name LIKE ? OR slug LIKE ?)"
            params.extend([f"%{couleur}%", f"%{couleur}%"])
        
        if theme:
            sql += " AND (name LIKE ? OR slug LIKE ?)"
            params.extend([f"%{theme}%", f"%{theme}%"])
        
        if age:
            sql += " AND (name LIKE ? OR slug LIKE ?)"
            params.extend([f"%{age}%", f"%{age}%"])
        
        sql += " ORDER BY is_featured DESC, price_ttc ASC LIMIT 200"
        products = conn.execute(sql, params).fetchall()
        
        # Deduplication
        unique_products = deduplicate_products(products)
        
        # Si event filtre et peu de résultats, fallback sans dedup
        if len(unique_products) < 5 and event:
            # Sans dedup
            unique_products = [dict(p) for p in products]
        
        # Recommendations (même event ou best)
        if event and event != 'all':
            recos = conn.execute("SELECT * FROM products WHERE event_type=? AND is_active=1 AND is_featured=1 ORDER BY RANDOM() LIMIT 8", (event,)).fetchall()
        else:
            recos = conn.execute("SELECT * FROM products WHERE is_featured=1 AND is_active=1 ORDER BY RANDOM() LIMIT 8").fetchall()
        
        # Stats pour universes
        by_event = conn.execute("SELECT event_type, COUNT(*) as c FROM products WHERE is_active=1 GROUP BY event_type").fetchall()
        stats = {r['event_type']: r['c'] for r in by_event}
        
    except Exception as e:
        print(f"Explorer error: {e}")
        unique_products = []
        recos = []
        stats = {}
    finally:
        conn.close()
    
    # Enrich
    enriched = enrich_products(unique_products)
    recos_enriched = enrich_products(recos)
    
    # Universes data for horizontal scroll
    universes = [
        {"slug":"mariage","name":"Mariage","count":stats.get('mariage',40),"desc":"Déco salle, table, voiture, cadeaux invités","img":"/static/images/products/mariage-arche-blanc-or-200pcs.jpg","color":"#EDE6DC"},
        {"slug":"gender_reveal","name":"Gender Reveal","count":stats.get('gender_reveal',14),"desc":"Ballons 90cm, fumigènes, canons","img":"/static/images/products/gender-reveal-ballon-90cm-rose.jpg","color":"#FFD6DE"},
        {"slug":"baby_shower","name":"Baby Shower","count":stats.get('baby_shower',20),"desc":"Kits 70pcs, vaisselle, jeux","img":"/static/images/products/baby-shower-kit-fille-70pcs.jpg","color":"#C5E8FF"},
        {"slug":"naissance","name":"Naissance","count":stats.get('naissance',23),"desc":"Guirlandes, affiches perso","img":"/static/images/products/naissance-guirlande-bienvenue.jpg","color":"#E8D5B5"},
        {"slug":"bapteme","name":"Baptême","count":stats.get('bapteme',22),"desc":"Bougies perso, dragées plexi","img":"/static/images/products/bapteme-bougie-verre-ambre.jpg","color":"#C9B6E4"},
        {"slug":"anniversaire","name":"Anniversaire","count":stats.get('anniversaire',31),"desc":"Licorne, Harry Potter, 30 ans","img":"/static/images/products/anniversaire-licorne-70pcs.jpg","color":"#A8B5A0"},
        {"slug":"kits","name":"Kits x4","count":13,"desc":"Tout compris, économie 15%","img":"/static/images/products/kit-mariage-50-pers.jpg","color":"#121212"},
    ]
    
    return templates.TemplateResponse(request, "shop/explorer_v5.html", {
        "request": request,
        "products": enriched,
        "recommendations": recos_enriched,
        "universes": universes,
        "current_event": event,
        "filter": filter,
        "query": q,
        "total_before_dedup": len(products) if 'products' in locals() else 0,
        "total_after_dedup": len(enriched),
        "stats": stats,
        "title": f"Explorer {event or 'tout'} — {len(enriched)} produits uniques sans doublons"
    })

@router.get("/api/explorer/products")
def api_explorer(event: str = None, filter: str = None, q: str = None):
    """API JSON pour filtrage fluide sans rechargement page"""
    conn = get_sqlite_conn()
    try:
        sql = "SELECT id, sku, slug, name, short_desc, price_ttc, price_ht, cost_price, stock_qty, event_type, is_featured FROM products WHERE is_active=1"
        params = []
        if event and event != 'all' and event != 'kits':
            sql += " AND event_type=?"
            params.append(event)
        if event == 'kits':
            sql += " AND (name LIKE '%Kit%' OR slug LIKE '%kit%')"
        if filter == 'kit':
            sql += " AND (name LIKE '%Kit%' OR slug LIKE '%kit%')"
        elif filter == 'perso':
            sql += " AND (name LIKE '%Personnalis%' OR slug LIKE '%perso%')"
        elif filter in ['rose','bleu','or']:
            sql += " AND (name LIKE ? OR slug LIKE ?)"
            params.extend([f"%{filter}%", f"%{filter}%"])
        if q:
            sql += " AND (name LIKE ? OR slug LIKE ?)"
            params.extend([f"%{q}%", f"%{q}%"])
        sql += " ORDER BY is_featured DESC LIMIT 100"
        products = conn.execute(sql, params).fetchall()
        unique = deduplicate_products(products)
        enriched = enrich_products(unique)
        return {"products": enriched, "count": len(enriched), "dedup_removed": len(products)-len(enriched)}
    except Exception as e:
        return {"error": str(e), "products": []}
    finally:
        conn.close()
