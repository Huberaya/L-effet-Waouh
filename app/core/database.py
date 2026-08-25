import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

# Handle Vercel /tmp for SQLite
db_url = DATABASE_URL
if db_url.startswith("sqlite"):
    # If path is relative and on Vercel, use /tmp
    if os.getenv("VERCEL"):
        if "waouh_v2.db" in db_url and "/tmp" not in db_url:
            db_url = "sqlite:////tmp/waouh_v2.db"

connect_args = {"check_same_thread": False} if db_url.startswith("sqlite") else {}
engine = create_engine(db_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_sqlite_conn():
    """Direct sqlite3 connection - handles Vercel /tmp"""
    import sqlite3
    db_path = "./waouh_v2.db"
    url = os.getenv("DATABASE_URL", db_url)
    if "sqlite:///" in url:
        db_path = url.replace("sqlite:///", "")
        # Handle 4 slashes for absolute
        if db_path.startswith("/"):
            pass
        else:
            # relative
            if os.getenv("VERCEL"):
                db_path = "/tmp/waouh_v2.db"
    # Ensure dir exists
    os.makedirs(os.path.dirname(db_path) if os.path.dirname(db_path) else ".", exist_ok=True)
    conn = sqlite3.connect(db_path, timeout=20)
    conn.row_factory = sqlite3.Row
    # Auto-init if empty (Vercel cold start)
    try:
        cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        if not cur.fetchone():
            # DB empty, init
            import pathlib
            root = pathlib.Path(__file__).parent.parent.parent
            for f in ["sql/schema_v2.sql", "sql/seed_categories.sql", "sql/seed_products_gender_reveal.sql", "sql/seed_products_naissance_mariage.sql"]:
                p = root / f
                if p.exists():
                    conn.executescript(p.read_text())
            conn.commit()
    except Exception as e:
        print(f"DB auto-init error: {e}")
    return conn
