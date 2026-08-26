"""
Vercel entrypoint - L'Effet Waouh V2 - Fix static serving
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# Vercel writable path for SQLite
os.environ.setdefault("DATABASE_URL", os.getenv("DATABASE_URL", "sqlite:////tmp/waouh_v2.db"))
os.environ["VERCEL"] = "1"

# Ensure static dir exists at runtime
static_dir = ROOT / "app" / "static"
print(f"Static dir exists: {static_dir.exists()}, files: {len(list(static_dir.rglob('*'))) if static_dir.exists() else 0}")

from app.main import app

# Auto-init DB if not exists
try:
    import sqlite3
    db_path = "/tmp/waouh_v2.db"
    if not os.path.exists(db_path) or os.path.getsize(db_path) < 1000:
        conn = sqlite3.connect(db_path)
        sql_files = [
            "sql/schema_v2.sql",
            "sql/seed_categories.sql",
            "sql/seed_categories_v3_full.sql",
            "sql/seed_products_gender_reveal.sql",
            "sql/seed_products_naissance_mariage.sql",
            "sql/seed_products_mariage_full.sql",
            "sql/seed_products_anniversaire.sql",
            "sql/seed_products_bapteme.sql",
            "sql/seed_products_kits_personnalises.sql",
            "sql/seed_products_naissance_full.sql",
            "sql/dedup_products.sql",
        ]
        for sql_file in sql_files:
            p = ROOT / sql_file
            if p.exists():
                try:
                    conn.executescript(p.read_text())
                    print(f"✅ Seed {sql_file}")
                except Exception as se:
                    print(f"⚠️ Seed error {sql_file}: {se}")
        conn.commit()
        # Ensure product_categories for new products if missing (assign by event_type fallback)
        try:
            conn.execute("""
            INSERT OR IGNORE INTO product_categories(product_id, category_id)
            SELECT p.id, c.id FROM products p JOIN categories c ON c.slug = p.event_type
            WHERE p.event_type IN ('mariage','anniversaire','bapteme','naissance','baby_shower','gender_reveal')
            AND NOT EXISTS (SELECT 1 FROM product_categories pc WHERE pc.product_id=p.id)
            """)
            conn.commit()
        except Exception as e2:
            print(f"⚠️ categories fallback: {e2}")
        conn.close()
        print(f"✅ DB Vercel init V3: {db_path}")
except Exception as e:
    print(f"⚠️ DB init error: {e}")

__all__ = ["app"]
