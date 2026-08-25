# Arborescence V2 - Plateforme Vente + Location

## Structure complète proposée

```
waouh-v2/
├── README.md
├── docker-compose.yml
├── .env.example
├── .gitignore
├── requirements.txt
│
├── sql/
│   ├── schema_v2.sql          # Schéma complet V1+V2
│   ├── seed_categories.sql    # 20 catégories mariage/naissance/gender
│   ├── seed_products_gender_reveal.sql # 10 produits GR + variantes
│   ├── seed_products_naissance_mariage.sql # 15 produits + packs
│   └── migrate_from_v1.sql
│
├── seed/
│   ├── categories.json
│   ├── products_full.json     # Export JSON pour front
│   └── images/                # À remplir avec tes visuels
│
├── app/
│   ├── main.py                # FastAPI entrypoint (port 8000)
│   ├── core/
│   │   ├── config.py          # Settings depuis .env
│   │   ├── database.py        # SQLAlchemy + SQLite/Postgres
│   │   ├── security.py        # hash, JWT
│   │   └── shipping.py        # Calcul frais port
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py         # Product, Variant, Image, Category
│   │   ├── order.py           # Order, OrderItem, Cart
│   │   └── legacy.py          # Booking, Lead (V1)
│   ├── schemas/
│   │   ├── product.py         # Pydantic
│   │   └── order.py
│   ├── routers/
│   │   ├── shop.py            # /shop, /c/{slug}, /p/{slug}
│   │   ├── cart.py            # /cart, /cart/add
│   │   ├── checkout.py        # /checkout + Stripe webhook
│   │   ├── admin_products.py  # CRUD produits
│   │   ├── admin_orders.py    # Commandes à préparer
│   │   └── legacy.py          # /reservation (location) conservé
│   ├── services/
│   │   ├── stripe_service.py
│   │   ├── stock_service.py
│   │   └── email_service.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── shop/
│   │   │   ├── category.html  # Grille produits
│   │   │   ├── product.html   # Fiche produit avec variantes rose/bleu
│   │   │   └── cart.html
│   │   └── admin/
│   └── static/
│       ├── css/
│       ├── js/
│       └── uploads/           # Images produits
│
├── docs/
│   ├── schema-ecommerce-v2.md
│   ├── arborescence-v2.md
│   ├── catalogue-strategy.md
│   └── business-plan-vente.md
│
└── scripts/
    ├── init_db.py
    ├── import_seed.py
    └── generate_sitemap.py
```

## Catalogue V2 - Stratégie par univers

### 1. Gender Reveal (priorité #1 - marge 70%, viral TikTok)
**Objectif : 20 produits, ticket moyen 35€, 10 commandes/jour = 10k€/mois**

- Produits d'appel à 3.90€ : canon confettis x1 (marge 75%)
- Produits héros à 10-14.90€ : ballon 90cm, fumigènes lot 2
- Packs à 44.90€ et 84.90€ : marge 60%, panier moyen boosté

**SEO :** `gender reveal`, `ballon gender reveal`, `fumigene rose bleu`

### 2. Mariage VENTE (consommables)
**Objectif : transformer tes clients location en clients vente**

- Cierges magiques lot 50/100 : achat 9€, vente 28.90€ = marge 69%
- Confettis biodégradables 1kg : achat 5€, vente 19.90€
- Pack sortie mairie 50 pers : 49.90€ (tu l'as déjà en location 199€)

**Cross-sell :** Quand quelqu'un réserve photobooth 360 à 550€, propose pack cierges + confettis en vente additionnelle.

### 3. Naissance / Baby Shower
**Objectif : capter après gender reveal (même cliente 6 mois plus tard)**

- Guirlande Bienvenue Bébé, ballons BABY, kit empreintes
- Kit baby shower fille/garçon 70 pièces : 24.90€ (achat 8€)

### 4. Location premium (conservé)
- Photobooth 360, miroir magique, livre d'or audio, néons
- Toujours avec opérateur, mais fiche produit avec bouton "Louer" vs "Acheter"

---

## Flux client V2

```
TikTok Gender Reveal (vidéo ballon éclatable)
  -> /p/ballon-eclatable-gender-reveal-90cm
  -> Choix variante Rose/Bleu
  -> Ajout panier + cross-sell "Ajoute 3 canons pour 10.50€"
  -> /cart -> /checkout (email + adresse)
  -> Stripe 14.90€
  -> Webhook -> order status paid -> stock -1 -> email + étiquette Colissimo
  -> 6 mois plus tard : email "Bébé est là ? -10% sur déco naissance"
  -> 1 an plus tard : "Baptême ?"
```

---

## Stock initial conseillé (1500€)

| Produit | Qté | Coût unitaire | Total |
|---|---|---|---|
| Ballon 90cm + confettis | 100 | 2.50€ | 250€ |
| Fumigènes lot 2 | 50 | 4€ | 200€ |
| Canons confettis | 200 | 0.90€ | 180€ |
| Cartes à gratter | 50 lots | 2.20€ | 110€ |
| Cierges 40cm lot 50 | 40 lots | 9€ | 360€ |
| Confettis bio 1kg | 20 kg | 5€ | 100€ |
| Kits arche ballons | 15 | 9€ | 135€ |
| Divers | - | - | 165€ |
| **TOTAL** | | | **1500€** |

**Retour :** 1500€ / marge moyenne 10€ = 150 ventes = 1 mois TikTok.

---

## Prochain fichier à créer : `app/models/product.py` (SQLAlchemy)
