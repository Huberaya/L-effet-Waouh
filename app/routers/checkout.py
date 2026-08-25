from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import pathlib, datetime, secrets
from ..core.database import get_sqlite_conn

router = APIRouter()
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/checkout", response_class=HTMLResponse)
def checkout_page(request: Request):
    conn = get_sqlite_conn()
    token = request.cookies.get("cart_token")
    if not token:
        conn.close()
        return RedirectResponse("/cart", status_code=302)
    cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
    if not cart:
        conn.close()
        return RedirectResponse("/cart", status_code=302)
    items = conn.execute("""
        SELECT ci.*, p.name, p.sku, p.price_ttc, p.tva_rate
        FROM cart_items ci JOIN products p ON p.id=ci.product_id
        WHERE ci.cart_id=?
    """, (cart["id"],)).fetchall()
    if not items:
        conn.close()
        return RedirectResponse("/cart", status_code=302)
    total_ttc = sum([i["quantity"] * i["price_ttc_at_add"] for i in items])
    shipping_methods = conn.execute("SELECT * FROM shipping_methods WHERE is_active=1 ORDER BY price_ttc").fetchall()
    # calcul frais port gratuit ?
    conn.close()
    return templates.TemplateResponse(request, "shop/checkout.html", {
        "request": request,
        "items": items,
        "total_ttc": total_ttc,
        "shipping_methods": shipping_methods
    })

@router.post("/checkout/confirm")
def checkout_confirm(
    request: Request,
    email: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    street: str = Form(...),
    zip_code: str = Form(...),
    city: str = Form(...),
    phone: str = Form(None),
    shipping_method: str = Form(...),
    notes: str = Form(None)
):
    conn = get_sqlite_conn()
    token = request.cookies.get("cart_token")
    cart = conn.execute("SELECT * FROM carts WHERE token=?", (token,)).fetchone()
    items = conn.execute("""
        SELECT ci.*, p.name, p.sku, p.price_ht, p.price_ttc, p.tva_rate, p.cost_price
        FROM cart_items ci JOIN products p ON p.id=ci.product_id
        WHERE ci.cart_id=?
    """, (cart["id"],)).fetchall()
    
    total_ttc = sum([i["quantity"] * i["price_ttc_at_add"] for i in items])
    # shipping
    ship = conn.execute("SELECT * FROM shipping_methods WHERE code=?", (shipping_method,)).fetchone()
    shipping_cost = ship["price_ttc"] if ship else 0
    if ship and ship["free_from"] and total_ttc >= ship["free_from"]:
        shipping_cost = 0
    
    total_ht = total_ttc / 1.2  # simplification TVA 20%
    total_tva = total_ttc - total_ht
    
    # Génère numéro commande
    number = "W-" + datetime.datetime.now().strftime("%Y%m") + "-" + secrets.token_hex(3).upper()
    
    shipping_json = f'{{"first_name":"{first_name}","last_name":"{last_name}","street":"{street}","zip":"{zip_code}","city":"{city}","phone":"{phone}"}}'
    
    cur = conn.execute("""
        INSERT INTO orders(number, email, phone, status, total_ht, total_tva, total_ttc, shipping_cost_ttc, shipping_method_code, shipping_address_json, notes, created_at)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    """, (number, email, phone, "paid", total_ht, total_tva, total_ttc + shipping_cost, shipping_cost, shipping_method, shipping_json, notes, datetime.datetime.now().isoformat()))
    order_id = cur.lastrowid
    
    # order_items
    for it in items:
        conn.execute("""
            INSERT INTO order_items(order_id, product_id, variant_id, name_snapshot, sku_snapshot, quantity, price_ht, price_ttc, tva_rate, total_ht, total_ttc)
            VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """, (order_id, it["product_id"], it["variant_id"], it["name"], it["sku"], it["quantity"], it["price_ht"], it["price_ttc_at_add"], it["tva_rate"] or 20, it["quantity"]*it["price_ht"], it["quantity"]*it["price_ttc_at_add"]))
        # décrémente stock
        conn.execute("UPDATE products SET stock_qty=stock_qty-? WHERE id=?", (it["quantity"], it["product_id"]))
        if it["variant_id"]:
            conn.execute("UPDATE product_variants SET stock_qty=stock_qty-? WHERE id=?", (it["quantity"], it["variant_id"]))
        # log stock
        conn.execute("INSERT INTO stock_movements(product_id, variant_id, type, quantity, order_id, reason) VALUES(?,?,?,?,?,?)",
                     (it["product_id"], it["variant_id"], "sale", -it["quantity"], order_id, f"Commande {number}"))
    
    # vide panier
    conn.execute("DELETE FROM cart_items WHERE cart_id=?", (cart["id"],))
    conn.commit()
    conn.close()
    
    return RedirectResponse(f"/checkout/success/{number}", status_code=302)

@router.get("/checkout/success/{number}", response_class=HTMLResponse)
def checkout_success(request: Request, number: str):
    conn = get_sqlite_conn()
    order = conn.execute("SELECT * FROM orders WHERE number=?", (number,)).fetchone()
    items = conn.execute("SELECT * FROM order_items WHERE order_id=?", (order["id"],)).fetchall() if order else []
    conn.close()
    if not order:
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse(request, "shop/success.html", {
        "request": request,
        "order": order,
        "items": items
    })
