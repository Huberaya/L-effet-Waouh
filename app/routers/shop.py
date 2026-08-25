from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pathlib
from ..core.database import get_sqlite_conn

router = APIRouter()
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/shop", response_class=HTMLResponse)
def shop_all(request: Request, event: str = None, q: str = None):
    conn = get_sqlite_conn()
    sql = "SELECT * FROM products WHERE is_active=1"
    params = []
    if event:
        sql += " AND event_type=?"
        params.append(event)
    if q:
        sql += " AND (name LIKE ? OR short_desc LIKE ?)"
        params.extend([f"%{q}%", f"%{q}%"])
    sql += " ORDER BY is_featured DESC, created_at DESC LIMIT 60"
    products = conn.execute(sql, params).fetchall()
    cats = conn.execute("SELECT * FROM categories WHERE parent_id IS NULL ORDER BY position").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "shop/category.html", {
        "request": request,
        "products": products,
        "categories": cats,
        "current_event": event,
        "query": q,
        "title": f"Boutique {event}" if event else "Toute la boutique"
    })

@router.get("/shop/c/{slug}", response_class=HTMLResponse)
def shop_category(request: Request, slug: str):
    conn = get_sqlite_conn()
    cat = conn.execute("SELECT * FROM categories WHERE slug=?", (slug,)).fetchone()
    if not cat:
        conn.close()
        raise HTTPException(404, "Catégorie non trouvée")
    # Produits de cette catégorie ou de ses enfants
    products = conn.execute("""
        SELECT p.* FROM products p
        JOIN product_categories pc ON pc.product_id=p.id
        JOIN categories c ON c.id=pc.category_id
        WHERE (c.slug=? OR c.parent_id=(SELECT id FROM categories WHERE slug=?))
        AND p.is_active=1
        ORDER BY p.is_featured DESC, p.price_ttc ASC
    """, (slug, slug)).fetchall()
    # Si pas via liaison, fallback event_type
    if not products:
        products = conn.execute("SELECT * FROM products WHERE event_type=? AND is_active=1 ORDER BY is_featured DESC", (cat["event_type"],)).fetchall()
    
    subcats = conn.execute("SELECT * FROM categories WHERE parent_id=? ORDER BY position", (cat["id"],)).fetchall()
    conn.close()
    return templates.TemplateResponse(request, "shop/category.html", {
        "request": request,
        "products": products,
        "categories": subcats,
        "current_category": cat,
        "title": cat["name"]
    })

@router.get("/shop/p/{slug}", response_class=HTMLResponse)
def product_detail(request: Request, slug: str):
    conn = get_sqlite_conn()
    prod = conn.execute("SELECT * FROM products WHERE slug=? AND is_active=1", (slug,)).fetchone()
    if not prod:
        conn.close()
        raise HTTPException(404, "Produit non trouvé")
    variants = conn.execute("SELECT * FROM product_variants WHERE product_id=? AND is_active=1 ORDER BY price_ttc", (prod["id"],)).fetchall()
    images = conn.execute("SELECT * FROM product_images WHERE product_id=? ORDER BY position", (prod["id"],)).fetchall()
    # Produits similaires même event
    similar = conn.execute("SELECT * FROM products WHERE event_type=? AND id!=? AND is_active=1 ORDER BY RANDOM() LIMIT 4", (prod["event_type"], prod["id"])).fetchall()
    # Calcul marge
    marge = round((prod["price_ttc"] - (prod["cost_price"] or 0)) / prod["price_ttc"] * 100, 1) if prod["price_ttc"] else 0
    conn.close()
    # Try V3 template, fallback V2
    try:
        return templates.TemplateResponse(request, "shop/product_v3.html", {
            "request": request,
            "product": prod,
            "variants": variants,
            "images": images,
            "similar": similar,
            "marge": marge
        })
    except:
        return templates.TemplateResponse(request, "shop/product.html", {
            "request": request,
            "product": prod,
            "variants": variants,
            "images": images,
            "similar": similar,
            "marge": marge
        })

@router.get("/shop/event/{event_type}", response_class=HTMLResponse)
def shop_event(request: Request, event_type: str):
    conn = get_sqlite_conn()
    products = conn.execute("SELECT * FROM products WHERE event_type=? AND is_active=1 ORDER BY is_featured DESC, price_ttc", (event_type,)).fetchall()
    cat = conn.execute("SELECT * FROM categories WHERE event_type=? AND parent_id IS NULL LIMIT 1", (event_type,)).fetchone()
    conn.close()
    return templates.TemplateResponse(request, "shop/category.html", {
        "request": request,
        "products": products,
        "title": cat["name"] if cat else event_type,
        "current_event": event_type
    })
