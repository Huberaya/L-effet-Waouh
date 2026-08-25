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
from .routers import shop, cart, checkout, admin, shop_v3, admin_v3
app.include_router(shop.router)
app.include_router(shop_v3.router)
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
        cats = conn.execute("SELECT * FROM categories WHERE parent_id IS NULL AND is_active=1 ORDER BY position").fetchall()
    except:
        cats = []
    try:
        nb_products = conn.execute("SELECT COUNT(*) FROM products WHERE is_active=1").fetchone()[0]
    except:
        nb_products = 0
    try:
        nb_gr = conn.execute("SELECT COUNT(*) FROM products WHERE event_type='gender_reveal' AND is_active=1").fetchone()[0]
    except:
        nb_gr = 0
    conn.close()
    # Try V3 home, fallback V2
    try:
        return templates.TemplateResponse(request, "shop/home_v3.html", {
            "request": request,
            "featured": featured,
            "categories": cats,
            "nb_products": nb_products,
            "nb_gr": nb_gr
        })
    except:
        return templates.TemplateResponse(request, "shop/home.html", {
            "request": request,
            "featured": featured,
            "categories": cats,
            "nb_products": nb_products,
            "nb_gr": nb_gr
        })

@app.get("/health")
def health():
    return {"status": "ok", "version": "v2-vente", "time": datetime.datetime.now().isoformat(), "env": "vercel" if __import__("os").getenv("VERCEL") else "local"}

@app.get("/reservation")
def legacy_reservation():
    return RedirectResponse("/shop/c/mariage", status_code=302)

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
        "https://leffetwaouh.fr/shop",
        "https://leffetwaouh.fr/kits",
        "https://leffetwaouh.fr/blog",
        "https://leffetwaouh.fr/event/mariage",
        "https://leffetwaouh.fr/event/gender-reveal",
        "https://leffetwaouh.fr/event/baby-shower",
        "https://leffetwaouh.fr/event/naissance",
        "https://leffetwaouh.fr/event/bapteme",
        "https://leffetwaouh.fr/event/anniversaire",
    ]
    for p in products:
        urls.append(f"https://leffetwaouh.fr/shop/p/{p['slug']}")
    for c in cats:
        urls.append(f"https://leffetwaouh.fr/shop/c/{c['slug']}")
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
