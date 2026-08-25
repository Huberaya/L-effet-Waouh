#!/usr/bin/env python3
"""Init DB V2"""
import sqlite3, pathlib, os
db='waouh_v2.db'
if os.path.exists(db):
    os.remove(db)
    print(f"Supprimé {db}")
con=sqlite3.connect(db)
for f in ['sql/schema_v2.sql','sql/seed_categories.sql','sql/seed_products_gender_reveal.sql','sql/seed_products_naissance_mariage.sql']:
    print(f"Import {f}...")
    sql=pathlib.Path(f).read_text()
    con.executescript(sql)
con.commit()
print("✅ DB V2 prête")
for r in con.execute("SELECT event_type, COUNT(*) FROM products GROUP BY event_type"):
    print(r)
con.close()
