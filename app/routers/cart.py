from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib, secrets, datetime
from ..core.database import get_sqlite_conn

router = APIRouter()
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

def get_or_create_cart(request: Request, response: Response, conn):
    token = request.cookies.get("cart_token")
    if not token:
        token = secrets.token_urlsafe(24)
        response.set_cookie("cart_token", token, max_age=30*24*3600, httponly=True, samesite="lax")
    # cherche cart
    cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
    if not cart:
        conn.execute("INSERT INTO carts(token, created_at, updated_at) VALUES(?,?,?)", (token, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
        conn.commit()
        cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
    return cart, token

@router.get("/cart", response_class=HTMLResponse)
def view_cart(request: Request):
    conn = get_sqlite_conn()
    token = request.cookies.get("cart_token")
    items = []
    total = 0
    if token:
        cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
        if cart:
            items = conn.execute("""
                SELECT ci.*, p.name, p.slug, p.price_ttc, v.name as variant_name, v.attribute_value
                FROM cart_items ci
                JOIN products p ON p.id=ci.product_id
                LEFT JOIN product_variants v ON v.id=ci.variant_id
                WHERE ci.cart_id=?
            """, (cart["id"],)).fetchall()
            total = sum([i["quantity"] * i["price_ttc_at_add"] for i in items])
    conn.close()
    return templates.TemplateResponse(request, "shop/cart.html", {
        "request": request,
        "items": items,
        "total": total,
        "shipping_free_from": 59.0
    })

@router.post("/cart/add")
def add_to_cart(request: Request, product_id: int = Form(...), variant_id: int = Form(None), quantity: int = Form(1)):
    conn = get_sqlite_conn()
    prod = conn.execute("SELECT * FROM products WHERE id=?", (product_id,)).fetchone()
    if not prod:
        conn.close()
        return RedirectResponse("/shop", status_code=302)
    
    price = prod["price_ttc"]
    if variant_id:
        var = conn.execute("SELECT * FROM product_variants WHERE id=?", (variant_id,)).fetchone()
        if var and var["price_ttc"]:
            price = var["price_ttc"]
    
    # get cart
    token = request.cookies.get("cart_token") or secrets.token_urlsafe(24)
    cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
    if not cart:
        conn.execute("INSERT INTO carts(token) VALUES(?)", (token,))
        conn.commit()
        cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
    
    # upsert
    existing = conn.execute("SELECT * FROM cart_items WHERE cart_id=? AND product_id=? AND (variant_id=? OR (variant_id IS NULL AND ? IS NULL))",
                            (cart["id"], product_id, variant_id, variant_id)).fetchone()
    if existing:
        conn.execute("UPDATE cart_items SET quantity=quantity+? WHERE id=?", (quantity, existing["id"]))
    else:
        conn.execute("INSERT INTO cart_items(cart_id, product_id, variant_id, quantity, price_ttc_at_add) VALUES(?,?,?,?,?)",
                     (cart["id"], product_id, variant_id, quantity, price))
    conn.commit()
    conn.close()
    resp = RedirectResponse("/cart", status_code=302)
    resp.set_cookie("cart_token", token, max_age=30*24*3600, httponly=True, samesite="lax")
    return resp

@router.post("/cart/remove/{item_id}")
def remove_item(item_id: int, request: Request):
    conn = get_sqlite_conn()
    token = request.cookies.get("cart_token")
    if token:
        cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
        if cart:
            conn.execute("DELETE FROM cart_items WHERE id=? AND cart_id=?", (item_id, cart["id"]))
            conn.commit()
    conn.close()
    return RedirectResponse("/cart", status_code=302)

@router.post("/cart/clear")
def clear_cart(request: Request):
    conn = get_sqlite_conn()
    token = request.cookies.get("cart_token")
    if token:
        cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
        if cart:
            conn.execute("DELETE FROM cart_items WHERE cart_id=?", (cart["id"],))
            conn.commit()
    conn.close()
    return RedirectResponse("/cart", status_code=302)
