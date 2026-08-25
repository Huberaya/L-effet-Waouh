-- ============================================================
-- L'EFFET WAOUH - SCHEMA E-COMMERCE V2 (Vente + Location)
-- Compatible SQLite (dev) & PostgreSQL (prod avec ajustements)
-- Date: 2026-08-25
-- ============================================================

-- ==================== EXISTANT V1 (conservé) ====================
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  name TEXT,
  phone TEXT,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'client', -- client, admin, pro
  created_at TEXT
);

CREATE TABLE IF NOT EXISTS sessions(token TEXT PRIMARY KEY, user_id INTEGER, expires INTEGER);
CREATE TABLE IF NOT EXISTS leads(
  id INTEGER PRIMARY KEY AUTOINCREMENT, company TEXT, contact TEXT, sector TEXT,
  email TEXT, phone TEXT, website TEXT, socials TEXT, source TEXT, status TEXT,
  score INTEGER DEFAULT 0, first_contact TEXT, last_interaction TEXT,
  next_action TEXT, notes TEXT, potential TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS bookings(
  id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, name TEXT, email TEXT,
  phone TEXT, event_date TEXT, venue TEXT, pack TEXT, options TEXT, total REAL,
  status TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS invoices(
  id INTEGER PRIMARY KEY AUTOINCREMENT, booking_id INTEGER, number TEXT,
  amount REAL, status TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS outbox(
  id INTEGER PRIMARY KEY AUTOINCREMENT, to_email TEXT, subject TEXT, body TEXT,
  kind TEXT, status TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT, title TEXT, content TEXT,
  status TEXT, scheduled_at TEXT, stats TEXT, created_at TEXT);

CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY AUTOINCREMENT, kind TEXT, payload TEXT, created_at TEXT);

-- ==================== NOUVEAU V2 : E-COMMERCE VENTE ====================

-- 1. CATEGORIES (arborescente)
CREATE TABLE IF NOT EXISTS categories(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  parent_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
  description TEXT,
  image_url TEXT,
  event_type TEXT NOT NULL, -- mariage, naissance, gender_reveal, baby_shower, evjf, bapteme, anniversaire, multi
  position INTEGER DEFAULT 0,
  is_active INTEGER DEFAULT 1,
  meta_title TEXT,
  meta_description TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_categories_parent ON categories(parent_id);
CREATE INDEX IF NOT EXISTS idx_categories_event ON categories(event_type);

-- 2. PRODUITS (VENTE)
CREATE TABLE IF NOT EXISTS products(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sku TEXT UNIQUE NOT NULL,
  ean TEXT,
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  short_desc TEXT, -- 160 chars pour cards
  long_desc TEXT, -- markdown / HTML
  price_ht REAL NOT NULL,
  price_ttc REAL NOT NULL,
  tva_rate REAL DEFAULT 20.0,
  cost_price REAL, -- prix achat pour calcul marge
  stock_qty INTEGER DEFAULT 0,
  stock_alert_threshold INTEGER DEFAULT 5,
  weight_grams INTEGER DEFAULT 0,
  length_cm REAL, width_cm REAL, height_cm REAL,
  is_active INTEGER DEFAULT 1,
  is_featured INTEGER DEFAULT 0,
  is_consumable INTEGER DEFAULT 0, -- 1 = confettis, cierges, fumigènes (pas de retour)
  is_digital INTEGER DEFAULT 0,
  event_type TEXT, -- mariage, gender_reveal, naissance, multi
  brand TEXT,
  supplier TEXT,
  supplier_url TEXT,
  video_url TEXT, -- lien TikTok/Reel démo
  meta_title TEXT,
  meta_description TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_products_slug ON products(slug);
CREATE INDEX IF NOT EXISTS idx_products_event ON products(event_type);
CREATE INDEX IF NOT EXISTS idx_products_active ON products(is_active);

-- 3. TABLE DE LIAISON PRODUIT <-> CATEGORIES (N-N)
CREATE TABLE IF NOT EXISTS product_categories(
  product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
  PRIMARY KEY (product_id, category_id)
);

-- 4. IMAGES PRODUITS
CREATE TABLE IF NOT EXISTS product_images(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  url TEXT NOT NULL,
  alt TEXT,
  position INTEGER DEFAULT 0,
  is_main INTEGER DEFAULT 0,
  created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_product_images_product ON product_images(product_id);

-- 5. VARIANTES (couleur, taille, lot)
CREATE TABLE IF NOT EXISTS product_variants(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  sku TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL, -- ex: "Rose - Lot 10", "Bleu - 90cm"
  attribute_type TEXT, -- color, size, pack_qty, combo
  attribute_value TEXT, -- rose, bleu, 90cm, x50
  price_ht REAL, -- si NULL, hérite du produit parent
  price_ttc REAL,
  stock_qty INTEGER DEFAULT 0,
  image_url TEXT,
  is_active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_variants_product ON product_variants(product_id);

-- 6. ADRESSES CLIENTS
CREATE TABLE IF NOT EXISTS addresses(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  label TEXT DEFAULT 'domicile',
  first_name TEXT, last_name TEXT,
  street TEXT NOT NULL,
  street2 TEXT,
  zip TEXT NOT NULL,
  city TEXT NOT NULL,
  country TEXT DEFAULT 'FR',
  phone TEXT,
  is_default_shipping INTEGER DEFAULT 0,
  is_default_billing INTEGER DEFAULT 0,
  created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_addresses_user ON addresses(user_id);

-- 7. PANIERS
CREATE TABLE IF NOT EXISTS carts(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
  token TEXT UNIQUE, -- pour invités non connectés
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_carts_token ON carts(token);
CREATE INDEX IF NOT EXISTS idx_carts_user ON carts(user_id);

CREATE TABLE IF NOT EXISTS cart_items(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cart_id INTEGER NOT NULL REFERENCES carts(id) ON DELETE CASCADE,
  product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  variant_id INTEGER REFERENCES product_variants(id) ON DELETE SET NULL,
  quantity INTEGER NOT NULL DEFAULT 1,
  price_ttc_at_add REAL NOT NULL, -- snapshot prix au moment ajout
  created_at TEXT DEFAULT (datetime('now')),
  UNIQUE(cart_id, product_id, variant_id)
);

-- 8. METHODES DE LIVRAISON
CREATE TABLE IF NOT EXISTS shipping_methods(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT UNIQUE NOT NULL, -- colissimo, mondial_relay, chronopost, retrait
  name TEXT NOT NULL,
  price_ttc REAL NOT NULL,
  free_from REAL, -- franco à partir de X€
  estimated_days_min INTEGER,
  estimated_days_max INTEGER,
  carrier TEXT,
  is_active INTEGER DEFAULT 1
);

-- 9. COUPONS / CODES PROMO
CREATE TABLE IF NOT EXISTS coupons(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT UNIQUE NOT NULL, -- BIENVENUE10
  type TEXT NOT NULL, -- percent, fixed
  value REAL NOT NULL, -- 10 pour 10% ou 10€ 
  min_amount_ttc REAL DEFAULT 0,
  max_uses INTEGER DEFAULT 0, -- 0 = illimité
  used_count INTEGER DEFAULT 0,
  valid_from TEXT,
  valid_to TEXT,
  is_active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT (datetime('now'))
);

-- 10. COMMANDES VENTE (coeur e-commerce)
CREATE TABLE IF NOT EXISTS orders(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  number TEXT UNIQUE NOT NULL, -- W-202608-0001
  user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
  email TEXT NOT NULL,
  phone TEXT,
  status TEXT NOT NULL DEFAULT 'pending', -- pending, paid, preparing, shipped, delivered, cancelled, refunded, failed
  total_ht REAL NOT NULL,
  total_tva REAL NOT NULL,
  total_ttc REAL NOT NULL,
  shipping_cost_ttc REAL DEFAULT 0,
  discount_amount_ttc REAL DEFAULT 0,
  shipping_method_code TEXT REFERENCES shipping_methods(code),
  shipping_address_json TEXT, -- snapshot JSON complet
  billing_address_json TEXT,
  payment_method TEXT, -- stripe, paypal, alma
  payment_intent_id TEXT,
  paid_at TEXT,
  coupon_code TEXT,
  notes TEXT,
  tracking_number TEXT,
  tracking_url TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_orders_user ON orders(user_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);
CREATE INDEX IF NOT EXISTS idx_orders_number ON orders(number);

CREATE TABLE IF NOT EXISTS order_items(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id INTEGER REFERENCES products(id) ON DELETE SET NULL,
  variant_id INTEGER REFERENCES product_variants(id) ON DELETE SET NULL,
  name_snapshot TEXT NOT NULL,
  sku_snapshot TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  price_ht REAL NOT NULL,
  price_ttc REAL NOT NULL,
  tva_rate REAL NOT NULL,
  total_ht REAL NOT NULL,
  total_ttc REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items(order_id);

-- 11. MOUVEMENTS DE STOCK (traçabilité)
CREATE TABLE IF NOT EXISTS stock_movements(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER REFERENCES products(id) ON DELETE SET NULL,
  variant_id INTEGER REFERENCES product_variants(id) ON DELETE SET NULL,
  type TEXT NOT NULL, -- in, out, sale, return, adjustment, inventory
  quantity INTEGER NOT NULL, -- positif ou négatif
  reason TEXT,
  order_id INTEGER REFERENCES orders(id) ON DELETE SET NULL,
  created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_stock_product ON stock_movements(product_id);

-- 12. AVIS CLIENTS
CREATE TABLE IF NOT EXISTS reviews(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
  order_id INTEGER REFERENCES orders(id) ON DELETE SET NULL,
  rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
  title TEXT,
  comment TEXT,
  is_verified_purchase INTEGER DEFAULT 0,
  is_approved INTEGER DEFAULT 0,
  created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_reviews_product ON reviews(product_id);

-- 13. WISHLIST
CREATE TABLE IF NOT EXISTS wishlists(
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  created_at TEXT DEFAULT (datetime('now')),
  PRIMARY KEY (user_id, product_id)
);

-- 14. FOURNISSEURS (pour achat malin)
CREATE TABLE IF NOT EXISTS suppliers(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  contact_name TEXT,
  email TEXT,
  phone TEXT,
  website TEXT,
  notes TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

-- 15. TABLES SEO / REDIRECTIONS
CREATE TABLE IF NOT EXISTS seo_redirects(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  from_path TEXT UNIQUE NOT NULL,
  to_path TEXT NOT NULL,
  code INTEGER DEFAULT 301
);

-- ==================== VUES UTILES ====================
CREATE VIEW IF NOT EXISTS v_product_stock AS
SELECT p.id, p.sku, p.name, p.stock_qty + COALESCE(SUM(v.stock_qty),0) as total_stock,
       p.is_active, p.event_type
FROM products p
LEFT JOIN product_variants v ON v.product_id = p.id
GROUP BY p.id;

CREATE VIEW IF NOT EXISTS v_orders_daily AS
SELECT date(created_at) as day, COUNT(*) as nb_orders, SUM(total_ttc) as ca_ttc, AVG(total_ttc) as panier_moyen
FROM orders WHERE status IN ('paid','preparing','shipped','delivered')
GROUP BY date(created_at);

-- ==================== DONNEES DE BASE ====================
INSERT OR IGNORE INTO shipping_methods(code, name, price_ttc, free_from, estimated_days_min, estimated_days_max, carrier) VALUES
('colissimo_dom', 'Colissimo Domicile', 6.90, 79.00, 2, 3, 'Colissimo'),
('mondial_relay', 'Mondial Relay Point', 4.90, 59.00, 3, 4, 'Mondial Relay'),
('chronopost', 'Chronopost Express', 14.90, 150.00, 1, 1, 'Chronopost'),
('retrait_nantes', 'Retrait gratuit Nantes', 0, 0, 0, 0, 'Retrait');

INSERT OR IGNORE INTO coupons(code, type, value, min_amount_ttc, valid_to) VALUES
('BIENVENUE10', 'percent', 10, 30, datetime('now', '+90 days')),
('WAOUH15', 'percent', 15, 80, datetime('now', '+30 days'));
