# L'Effet Waouh — Vente & Location d'animations mariage, naissance, gender reveal

## 🎯 Vision
**V1 (existant) :** Location premium photobooth 360, miroir magique, livre d'or audio avec opérateur (550-1490€/presta)
**V2 (nouveau) :** Vente de consommables à forte marge (gender reveal, naissance, mariage) + location conservée

> La vente finance le stock location. Modèle hybride Amazon + Rent the Runway.

---

## 📁 Arborescence

```
L-effet-Waouh/
├── README.md (ce fichier)
├── README_V2.md (détail V2)
├── docs/
│   ├── business-location-materiel-mariage.md (étude rentabilité location)
│   ├── schema-ecommerce-v2.md (schéma SQL expliqué)
│   ├── arborescence-v2.md (structure FastAPI)
│   └── catalogue-strategy.md (stratégie gender reveal)
│
├── v2-vente/  <- VITRINE COMMERCIALE (à lire en 1er)
│   ├── README.md (stratégie stock 1500€ + LTV cliente)
│   ├── gender-reveal/catalogue.md (12 produits, marge 70%)
│   ├── naissance/catalogue.md (6 produits, récurrence)
│   ├── mariage/catalogue.md (9 produits vente + cross-sell location)
│   └── packs/catalogue.md (packs 44.90€ et 84.90€)
│
├── sql/  <- SCHEMA + SEED
│   ├── schema_v2.sql (15 tables e-commerce + V1 conservé)
│   ├── seed_categories.sql (20 catégories)
│   ├── seed_products_gender_reveal.sql (10 best-sellers)
│   └── seed_products_naissance_mariage.sql (20 produits)
│
├── app/  <- BOUTIQUE FASTAPI V2 (Phase 3)
│   ├── main.py
│   ├── core/ (config, database, security)
│   ├── models/product.py
│   ├── routers/shop.py, cart.py, checkout.py, admin.py
│   ├── templates/shop/ (home, category, product, cart, checkout, success)
│   └── static/css/style.css
│
├── waouh/  <- LEGACY V1 (location) - conservé intact
│   ├── app.py (1035 lignes, stdlib, SQLite)
│   ├── automation/ (agents.py, content_engine.py, prospect_engine.py)
│   ├── brand/brand.md
│   └── content/ (blog + 54 fichiers generated)
│
├── visuels/ (35+ visuels AI demo)
├── build_*.py (génération landing/catalogue V1)
└── requirements.txt, .env.example, docker-compose.yml
```

---

## 🚀 Lancer V2 en local (30 produits, 1975 unités stock)

```bash
pip install -r requirements.txt
python scripts/init_db.py
uvicorn app.main:app --reload --port 8000

# -> http://localhost:8000
# -> http://localhost:8000/shop/event/gender_reveal (12 produits)
# -> http://localhost:8000/shop/p/ballon-eclatable-gender-reveal-90cm (variantes rose/bleu)
# -> http://localhost:8000/admin-v2 (CA, stock faible, commandes)
```

## 📊 Catalogue V2

- **Gender Reveal (12 produits, stock 1200, marge 66-78%)** : Ballon 90cm 10€, fumigènes lot 2 14.90€, canons 3.90€, pack essentiel 44.90€
- **Mariage vente (9 produits, stock 445)** : Cierges lot 50 28.90€ (achat 9€, marge 69%), confettis bio 1kg 19.90€
- **Naissance (6 produits, stock 220)** : Guirlande 7.90€ marge 77%, kit empreintes 16.90€
- **Baby Shower (3 produits)** : Kits 70pcs 24.90€

**Stock initial conseillé : 1500€ = 400 produits = 2 cartons. Retour en 1 mois TikTok (5 commandes/jour = 2900€ net/mois)**

---

## 🔄 V1 vs V2

|  | V1 Location | V2 Vente |
|---|---|---|
| Table | bookings | orders + order_items |
| Prix | 550€/jour | 10€ définitif |
| Stock | 1 photobooth = indispo ce jour | 150 ballons -1 par vente |
| Marge | 70% après 5 locations | 70% immédiate |
| Fréquence | Samedi | Tous les jours |

---

## 📦 Prochaines étapes

- [ ] Intégrer Stripe Checkout réel
- [ ] Ajouter vraies photos produits dans app/static/uploads/
- [ ] Connecter TikTok Shop / Shopify
- [ ] Créer landing gender reveal dédiée

---

© 2026 L'Effet Waouh - Nantes - Vente & Location
