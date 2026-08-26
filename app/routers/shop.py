from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pathlib
from ..core.database import get_sqlite_conn
from ..core.product_images import get_product_image

router = APIRouter()
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

def enrich_products(products):
    enriched=[]
    for p in products:
        d=dict(p)
        d['image_url']=get_product_image(d)
        enriched.append(d)
    return enriched

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
    # Enrich
    prod_dict = dict(prod)
    prod_dict['image_url'] = get_product_image(prod_dict)
    similar_enriched = enrich_products(similar)
    # Try immersive premium template first
    for tmpl in ["shop/product_premium_v5.html", "shop/product_immersive.html", "shop/product_v3.html", "shop/product.html"]:
        try:
            return templates.TemplateResponse(request, tmpl, {
                "request": request,
                "product": prod_dict,
                "variants": variants,
                "images": images,
                "similar": similar_enriched,
                "marge": marge
            })
        except Exception as e:
            print(f"Template {tmpl} failed: {e}")
            continue
    raise HTTPException(500, "Template error")
