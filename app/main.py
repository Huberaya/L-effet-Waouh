"""
L'Effet Waouh V2 - FastAPI Shop Vente + Location
Lancement local: uvicorn app.main:app --reload --port 8000
Vercel: via api/index.py
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import pathlib, datetime

from .core.database import get_sqlite_conn

BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(
    title="L'Effet Waouh V2 - Vente & Location",
    description="Boutique gender reveal, naissance, mariage - 30 produits, marge 70%",
    version="2.0.0"
)

# Static
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Routers
from .routers import shop, cart, checkout, admin, shop_v3, admin_v3, explorer
app.include_router(shop.router)
app.include_router(shop_v3.router)
app.include_router(explorer.router)
app.include_router(cart.router)
app.include_router(checkout.router)
app.include_router(admin.router)
app.include_router(admin_v3.router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    conn = get_sqlite_conn()
    try:
        featured = conn.execute("SELECT * FROM products WHERE is_featured=1 AND is_active=1 ORDER BY RANDOM() LIMIT 8").fetchall()
    except:
        featured = []
    try:
        # Stats for universes
        by_event = conn.execute("SELECT event_type, COUNT(*) as c FROM products WHERE is_active=1 GROUP BY event_type").fetchall()
        stats = {r['event_type']: r['c'] for r in by_event}
    except:
        stats = {}
    conn.close()
    # Enrich
    try:
        from .core.product_images import get_product_image
        import hashlib
        enriched = []
        for p in featured:
            d = dict(p)
            d['image_url'] = get_product_image(d)
            h = int(hashlib.md5(d.get('slug','').encode()).hexdigest()[:6], 16)
            d['bg_color'] = f"hsl({h%360}, 35%, 96%)"
            enriched.append(d)
        featured = enriched
    except:
        pass
    
    universes = [
        {"slug":"mariage","name":"Mariage","count":stats.get('mariage',30),"desc":"Déco salle, table, voiture, cadeaux invités","img":"/static/images/products/mariage-arche-blanc-or-200pcs.jpg","color":"#EDE6DC"},
        {"slug":"gender_reveal","name":"Gender Reveal","count":stats.get('gender_reveal',14),"desc":"Ballons 90cm, fumigènes, canons","img":"/static/images/products/gender-reveal-ballon-90cm-rose.jpg","color":"#FFD6DE"},
        {"slug":"baby_shower","name":"Baby Shower","count":stats.get('baby_shower',19),"desc":"Kits 70pcs, vaisselle, jeux","img":"/static/images/products/baby-shower-kit-fille-70pcs.jpg","color":"#C5E8FF"},
        {"slug":"naissance","name":"Naissance","count":stats.get('naissance',21),"desc":"Guirlandes, affiches perso","img":"/static/images/products/naissance-guirlande-bienvenue.jpg","color":"#E8D5B5"},
        {"slug":"bapteme","name":"Baptême","count":stats.get('bapteme',15),"desc":"Bougies perso, dragées plexi","img":"/static/images/products/bapteme-bougie-verre-ambre.jpg","color":"#C9B6E4"},
        {"slug":"anniversaire","name":"Anniversaire","count":stats.get('anniversaire',24),"desc":"Licorne, Harry Potter, 30 ans","img":"/static/images/products/anniversaire-licorne-70pcs.jpg","color":"#A8B5A0"},
        {"slug":"kits","name":"Kits x4","count":13,"desc":"Tout compris, économie 15%","img":"/static/images/products/kit-mariage-50-pers.jpg","color":"#121212"},
    ]
    
    for tmpl in ["shop/home_premium_v5.html", "shop/home_immersive.html", "shop/home_v3.html", "shop/home.html"]:
        try:
            return templates.TemplateResponse(request, tmpl, {
                "request": request,
                "featured": featured,
                "universes": universes,
                "nb_products": sum(stats.values()) if stats else 120,
                "nb_gr": stats.get('gender_reveal',14)
            })
        except Exception as e:
            print(f"Template {tmpl} failed: {e}")
            continue
    return HTMLResponse("Home error", status_code=500)

@app.get("/health")
def health():
    return {"status": "ok", "version": "v2-vente", "time": datetime.datetime.now().isoformat(), "env": "vercel" if __import__("os").getenv("VERCEL") else "local"}

@app.get("/reservation")
def legacy_reservation():
    return RedirectResponse("/shop/c/mariage", status_code=302)

@app.get("/shop", response_class=HTMLResponse)
def redirect_shop():
    return RedirectResponse("/explorer", status_code=302)

@app.get("/shop/event/{event_type}", response_class=HTMLResponse)
def redirect_shop_event(event_type: str):
    return RedirectResponse(f"/explorer?event={event_type}", status_code=302)

@app.get("/shop/c/{slug}", response_class=HTMLResponse)
def redirect_shop_c(slug: str):
    # Try to map category slug to event
    conn = get_sqlite_conn()
    try:
        cat = conn.execute("SELECT event_type FROM categories WHERE slug=?", (slug,)).fetchone()
        if cat and cat['event_type']:
            return RedirectResponse(f"/explorer?event={cat['event_type']}", status_code=302)
    except:
        pass
    finally:
        conn.close()
    return RedirectResponse(f"/explorer?q={slug}", status_code=302)

@app.get("/sitemap.xml")
def sitemap():
    from fastapi.responses import Response
    conn = get_sqlite_conn()
    try:
        products = conn.execute("SELECT slug, updated_at FROM products WHERE is_active=1 LIMIT 500").fetchall()
        cats = conn.execute("SELECT slug FROM categories WHERE is_active=1 LIMIT 100").fetchall()
    except:
        products = []
        cats = []
    conn.close()
    urls = [
        "https://leffetwaouh.fr/",
        "https://leffetwaouh.fr/explorer",
        "https://leffetwaouh.fr/kits",
        "https://leffetwaouh.fr/blog",
        "https://leffetwaouh.fr/explorer?event=mariage",
        "https://leffetwaouh.fr/explorer?event=gender_reveal",
        "https://leffetwaouh.fr/explorer?event=baby_shower",
        "https://leffetwaouh.fr/explorer?event=naissance",
        "https://leffetwaouh.fr/explorer?event=bapteme",
        "https://leffetwaouh.fr/explorer?event=anniversaire",
    ]
    for p in products:
        urls.append(f"https://leffetwaouh.fr/shop/p/{p['slug']}")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls[:1000]:
        xml += f"  <url><loc>{u}</loc><changefreq>weekly</changefreq></url>\n"
    xml += "</urlset>"
    return Response(content=xml, media_type="application/xml")

@app.get("/robots.txt")
def robots():
    from fastapi.responses import PlainTextResponse
    txt = "User-agent: *\nAllow: /\nSitemap: https://leffetwaouh.fr/sitemap.xml\n"
    return PlainTextResponse(txt)

@app.get("/api/products")
def api_products():
    """API JSON pour Vercel / front headless"""
    conn = get_sqlite_conn()
    products = conn.execute("SELECT id, sku, slug, name, price_ttc, stock_qty, event_type, is_featured FROM products WHERE is_active=1 ORDER BY is_featured DESC LIMIT 50").fetchall()
    conn.close()
    return [dict(p) for p in products]
