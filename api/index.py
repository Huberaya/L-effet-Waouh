"""
Vercel entrypoint - L'Effet Waouh V2
"""
import os
import sys
from pathlib import Path

# Add root to path
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# Vercel uses /tmp for writable SQLite, else Postgres via DATABASE_URL
# Auto-init DB if not exists (for demo)
os.environ.setdefault("DATABASE_URL", os.getenv("DATABASE_URL", "sqlite:////tmp/waouh_v2.db"))

from app.main import app

# Vercel expects 'app' variable
# For local Vercel dev, ensure DB exists
try:
    from app.core.database import get_sqlite_conn
    import sqlite3
    db_path = "/tmp/waouh_v2.db"
    if not os.path.exists(db_path):
        # Init from SQL files
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

# Export for Vercel
__all__ = ["app"]
