"""
L'Effet Waouh V2 - FastAPI Shop Vente + Location
Lancement: uvicorn app.main:app --reload --port 8000
"""
from fastapi import FastAPI, Request, Depends, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import os, sqlite3, pathlib, datetime, secrets

from .core.database import get_sqlite_conn

BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(title="L'Effet Waouh V2 - Vente + Location")

# Static
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Import routers
from .routers import shop, cart, checkout, admin

app.include_router(shop.router)
app.include_router(cart.router)
app.include_router(checkout.router)
app.include_router(admin.router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    conn = get_sqlite_conn()
    # Featured products
    featured = conn.execute("SELECT * FROM products WHERE is_featured=1 AND is_active=1 ORDER BY RANDOM() LIMIT 8").fetchall()
    # Categories racines
    cats = conn.execute("SELECT * FROM categories WHERE parent_id IS NULL AND is_active=1 ORDER BY position").fetchall()
    # Stats
    nb_products = conn.execute("SELECT COUNT(*) FROM products WHERE is_active=1").fetchone()[0]
    nb_gr = conn.execute("SELECT COUNT(*) FROM products WHERE event_type='gender_reveal' AND is_active=1").fetchone()[0]
    conn.close()
    return templates.TemplateResponse(request, "shop/home.html", {
        "request": request,
        "featured": featured,
        "categories": cats,
        "nb_products": nb_products,
        "nb_gr": nb_gr
    })

@app.get("/health")
def health():
    return {"status": "ok", "version": "v2-vente", "time": datetime.datetime.now().isoformat()}

# Legacy redirect for old V1 routes
@app.get("/reservation")
def legacy_reservation():
    return RedirectResponse("/shop/c/mariage", status_code=302)
