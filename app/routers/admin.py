from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pathlib
from ..core.database import get_sqlite_conn

router = APIRouter(prefix="/admin-v2", tags=["admin"])
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    conn = get_sqlite_conn()
    stats = {}
    stats["nb_products"] = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    stats["nb_orders"] = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    stats["ca_ttc"] = conn.execute("SELECT COALESCE(SUM(total_ttc),0) FROM orders WHERE status IN ('paid','preparing','shipped','delivered')").fetchone()[0]
    stats["stock_alert"] = conn.execute("SELECT COUNT(*) FROM products WHERE stock_qty <= stock_alert_threshold").fetchone()[0]
    orders = conn.execute("SELECT * FROM orders ORDER BY created_at DESC LIMIT 20").fetchall()
    low_stock = conn.execute("SELECT * FROM products WHERE stock_qty <= stock_alert_threshold ORDER BY stock_qty ASC LIMIT 20").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "admin/dashboard.html", {
        "request": request,
        "stats": stats,
        "orders": orders,
        "low_stock": low_stock
    })

@router.get("/products", response_class=HTMLResponse)
def admin_products(request: Request):
    conn = get_sqlite_conn()
    products = conn.execute("SELECT * FROM products ORDER BY event_type, price_ttc").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "admin/products.html", {
        "request": request,
        "products": products
    })

@router.get("/orders", response_class=HTMLResponse)
def admin_orders(request: Request):
    conn = get_sqlite_conn()
    orders = conn.execute("SELECT * FROM orders ORDER BY created_at DESC").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "admin/orders.html", {
        "request": request,
        "orders": orders
    })
