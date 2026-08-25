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
        for sql_file in ["sql/schema_v2.sql", "sql/seed_categories.sql", "sql/seed_products_gender_reveal.sql", "sql/seed_products_naissance_mariage.sql"]:
            p = ROOT / sql_file
            if p.exists():
                conn.executescript(p.read_text())
        conn.commit()
        conn.close()
        print(f"✅ DB Vercel init: {db_path}")
except Exception as e:
    print(f"⚠️ DB init error: {e}")

__all__ = ["app"]
