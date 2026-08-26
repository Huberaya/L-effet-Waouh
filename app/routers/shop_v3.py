from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pathlib, re
from ..core.database import get_sqlite_conn
from ..core.product_images import get_product_image

router = APIRouter()
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

def enrich_products(products):
    """Ajoute image_url correspondante à chaque produit"""
    enriched = []
    for p in products:
        d = dict(p)
        d['image_url'] = get_product_image(d)
        enriched.append(d)
    return enriched

def intelligent_search_score(query: str, product: dict) -> int:
    """Scoring recherche intelligente couleur/thème/âge/prénom/occasion"""
    q = query.lower()
    score = 0
    name = (product['name'] or '').lower()
    desc = (product['short_desc'] or '').lower()
    event = (product['event_type'] or '').lower()
    slug = (product['slug'] or '').lower()
    
    # Event type match +20
    events = ['mariage','gender reveal','gender_reveal','baby shower','baby_shower','naissance','bapteme','baptême','anniversaire','bebe','bébé']
    for ev in events:
        if ev in q and ev.replace(' ','_') in event:
            score += 20
        if ev in q and ev in name:
            score += 15
    
    # Couleur +15
    colors = ['rose','bleu','or','gold','blanc','pastel','noir','fille','garcon','garçon','boy','girl']
    for c in colors:
        if c in q and c in (name+' '+desc+' '+slug):
            score += 15
    
    # Thème +15
    themes = ['licorne','princesse','super','heros','foot','football','espace','dino','dinosaure','sirene','sirène','safari','tropical','harry','potter','barbie','glow','animaux','elegant','élégant','80','90']
    for t in themes:
        if t in q and t in (name+' '+desc+' '+slug):
            score += 15
    
    # Âge +10
    ages = re.findall(r'(\d+)\s*ans?', q)
    for age in ages:
        if age in name or age in slug:
            score += 10
    if '1 an' in q or '1an' in q:
        if '1 an' in name or '1-an' in slug:
            score += 10
    
    # Tags
    if q in name:
        score += 20
    if q in desc:
        score += 10
    if q in slug:
        score += 10
    
    # Best-seller boost
    if product['is_featured']:
        score += 5
    
    # Mots individuels
    for word in q.split():
        if len(word) > 2 and word in name:
            score += 3
    
    return score

@router.get("/search", response_class=HTMLResponse)
def search(request: Request, q: str = ""):
    conn = get_sqlite_conn()
    if not q:
        products = conn.execute("SELECT * FROM products WHERE is_active=1 ORDER BY is_featured DESC LIMIT 40").fetchall()
        conn.close()
        products = enrich_products(products)
        return templates.TemplateResponse(request, "shop/category.html", {
            "request": request,
            "products": products,
            "title": f"Toute la boutique - {len(products)} produits",
            "query": q
        })
    
    # Recherche large
    like = f"%{q}%"
    # Try FTS if exists, fallback LIKE
    try:
        products = conn.execute("""
            SELECT * FROM products WHERE is_active=1 
            AND (name LIKE ? OR short_desc LIKE ? OR slug LIKE ? OR event_type LIKE ?)
            LIMIT 100
        """, (like, like, like, like)).fetchall()
    except:
        products = []
    
    # Scoring intelligent
    scored = []
    for p in products:
        s = intelligent_search_score(q, dict(p))
        if s > 0 or len(q) < 3:
            scored.append((s, p))
    
    # Si pas de résultats avec scoring, retourner tous les LIKE
    if not scored and products:
        scored = [(1, p) for p in products]
    
    scored.sort(key=lambda x: x[0], reverse=True)
    result_products = [p for s,p in scored[:60]]
    
    # Suggestions si peu de résultats
    suggestions = []
    if len(result_products) < 5:
        suggestions = conn.execute("SELECT * FROM products WHERE is_featured=1 AND is_active=1 ORDER BY RANDOM() LIMIT 8").fetchall()
    
    conn.close()
    return templates.TemplateResponse(request, "shop/search.html", {
        "request": request,
        "products": enrich_products(result_products),
        "query": q,
        "title": f"Recherche: {q} - {len(result_products)} résultats",
        "suggestions": enrich_products(suggestions),
        "scored": [(s, dict(p)['name'][:40]) for s,p in scored[:10]]
    })

@router.get("/kits", response_class=HTMLResponse)
def kits(request: Request):
    conn = get_sqlite_conn()
    kits_products = conn.execute("""
        SELECT * FROM products WHERE is_active=1 AND slug LIKE 'kit-%' OR slug LIKE '%kit-%' OR name LIKE '%Kit %'
        ORDER BY 
          CASE event_type
            WHEN 'mariage' THEN 1
            WHEN 'gender_reveal' THEN 2
            WHEN 'baby_shower' THEN 3
            WHEN 'naissance' THEN 4
            WHEN 'bapteme' THEN 5
            WHEN 'anniversaire' THEN 6
            ELSE 7
          END,
          price_ttc DESC
        LIMIT 30
    """).fetchall()
    # Fallback if no kits via slug, use products with 'kit' in name or price >60 and featured
    if len(kits_products) < 5:
        kits_products = conn.execute("""
            SELECT * FROM products WHERE is_active=1 AND (price_ttc > 60 OR name LIKE '%Kit%' OR name LIKE '%Pack%')
            ORDER BY price_ttc DESC LIMIT 20
        """).fetchall()
    conn.close()
    return templates.TemplateResponse(request, "shop/kits.html", {
        "request": request,
        "products": enrich_products(kits_products),
        "title": "Kits Événementiels - Panier moyen x4"
    })

@router.get("/event/{event_type}", response_class=HTMLResponse)
def event_page(request: Request, event_type: str):
    from fastapi.responses import RedirectResponse
    event_type = event_type.replace('-','_')
    # V5: unifier vers /explorer single page pour cohérence immersive
    return RedirectResponse(f"/explorer?event={event_type}", status_code=302)

@router.get("/blog", response_class=HTMLResponse)
def blog_index(request: Request):
    articles = [
        {"slug":"idees-gender-reveal","title":"15 idées Gender Reveal originales 2024-2025","desc":"Ballon 90cm, fumigènes, cartes à gratter...","img":"06-bulles-confettis.jpg","keywords":"gender reveal idee"},
        {"slug":"organiser-baby-shower","title":"Comment organiser un Baby Shower parfait","desc":"Checklist, déco, jeux, cadeaux invités","img":"10-vin-honneur.jpg","keywords":"organiser baby shower"},
        {"slug":"decoration-mariage-petit-budget","title":"Décoration mariage petit budget: 20 idées chic","desc":"Arche ballons, chemin gaze, marque-places...","img":"05-cierges-magiques.jpg","keywords":"decoration mariage pas cher"},
        {"slug":"cadeaux-invites-bapteme","title":"Cadeaux invités baptême: 15 idées personnalisables","desc":"Bougies, dragées, magnets, fioles fleurs séchées","img":"08-piscine-balles.jpg","keywords":"cadeau invite bapteme"},
        {"slug":"themes-anniversaire-enfant","title":"16 thèmes anniversaire enfant qui cartonnent","desc":"Licorne best-seller 2024, Harry Potter, super-héros...","img":"09-premiere-danse.jpg","keywords":"theme anniversaire enfant"},
        {"slug":"organisation-bapteme-guide","title":"Organisation baptême: guide complet","desc":"Étapes, checklist, déco, cadeaux","img":"03-livre-or-audio.jpg","keywords":"organiser bapteme"},
    ]
    return templates.TemplateResponse(request, "shop/blog.html", {
        "request": request,
        "articles": articles,
        "title": "Blog idées déco — Gender Reveal, Mariage, Baptême, Anniversaire"
    })

@router.get("/blog/{slug}", response_class=HTMLResponse)
def blog_article(request: Request, slug: str):
    conn = get_sqlite_conn()
    # Produits liés selon slug
    if 'gender' in slug:
        related = conn.execute("SELECT * FROM products WHERE event_type='gender_reveal' AND is_featured=1 LIMIT 4").fetchall()
    elif 'baby-shower' in slug:
        related = conn.execute("SELECT * FROM products WHERE event_type='baby_shower' LIMIT 4").fetchall()
    elif 'mariage' in slug:
        related = conn.execute("SELECT * FROM products WHERE event_type='mariage' AND is_featured=1 LIMIT 4").fetchall()
    elif 'bapteme' in slug:
        related = conn.execute("SELECT * FROM products WHERE event_type='bapteme' LIMIT 4").fetchall()
    elif 'anniversaire' in slug:
        related = conn.execute("SELECT * FROM products WHERE event_type='anniversaire' AND is_featured=1 LIMIT 4").fetchall()
    else:
        related = conn.execute("SELECT * FROM products WHERE is_featured=1 LIMIT 4").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "shop/blog_article.html", {
        "request": request,
        "slug": slug,
        "related": related,
        "title": f"Guide {slug.replace('-',' ')} — L'Effet Waouh"
    })
