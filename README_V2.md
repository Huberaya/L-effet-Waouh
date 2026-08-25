# L'Effet Waouh V2 - Plateforme Vente + Location

## Ce qui a été fait (Phase 1 & 2)

### ✅ Phase 1 : Schéma E-commerce V2
- `sql/schema_v2.sql` : schéma complet SQLite/Postgres avec 15 nouvelles tables
  - categories (arbo), products, product_variants, product_images, product_categories
  - carts, cart_items, orders, order_items
  - shipping_methods, coupons, addresses, reviews, wishlists, stock_movements, suppliers
  - Vues `v_product_stock` et `v_orders_daily`
  - Données de base : 4 transporteurs + 2 coupons BIENVENUE10

- `docs/schema-ecommerce-v2.md` : explication du schéma, requêtes business, migration V1->V2

### ✅ Phase 2 : Arborescence + Catalogue Gender Reveal / Naissance / Mariage

**Catégories (20) :**
- 6 racines : mariage, naissance, gender-reveal, baby-shower, evjf-evjg, bapteme
- 14 sous-catégories : gender-ballon, gender-fumigene, gender-canon-confetti, mariage-cierges, etc.

**Produits seed (35 produits) :**
- `seed_products_gender_reveal.sql` : 10 produits best-sellers
  - Ballon éclatable 90cm (10€, marge 75%, stock 150)
  - Fumigènes lot 2 (14.90€)
  - Canons confettis (3.90€ à 19.90€ pack)
  - Boîte surprise, cartes à gratter, poudre Holi, kit arche 85pcs, pinata...
- `seed_products_naissance_mariage.sql` : 15 produits + 3 packs
  - Naissance : guirlande, ballons BABY, livre or, kit empreintes, boîte souvenirs
  - Mariage vente : cierges lot 50/100 (28.90€/48.90€, marge 69%), confettis bio 1kg, bulles, pétales, livre or bois, urne, néon vente
  - Baby shower : kits 70pcs
  - Packs : Gender Essentiel 44.90€ (marge 66%), Fête 20 pers 84.90€, Sortie mairie 50 pers 49.90€

- `seed/products_full.json` : export JSON pour front
- `docs/arborescence-v2.md` : structure FastAPI proposée + flux client TikTok + stock initial 1500€

---

## Comment tester le schéma maintenant

```bash
cd /home/user/waouh-v2
sqlite3 waouh_v2.db < sql/schema_v2.sql
sqlite3 waouh_v2.db < sql/seed_categories.sql
sqlite3 waouh_v2.db < sql/seed_products_gender_reveal.sql
sqlite3 waouh_v2.db < sql/seed_products_naissance_mariage.sql

# Vérif
sqlite3 waouh_v2.db "SELECT event_type, COUNT(*) FROM products GROUP BY event_type;"
sqlite3 waouh_v2.db "SELECT slug, name, price_ttc, stock_qty FROM products WHERE is_featured=1;"
```

Résultat attendu :
- gender_reveal : 13 produits (avec packs)
- mariage : 11 produits
- naissance : 6 produits
- baby_shower : 3 produits

---

## Prochaines étapes (Phase 3) - À faire ensemble

1. **Créer `app/models/product.py`** : modèles SQLAlchemy
2. **Créer `app/main.py` FastAPI** : routes /shop, /p/{slug}, /cart, /checkout
3. **Intégrer Stripe** : checkout + webhook
4. **Front** : grille catégorie avec filtres rose/bleu, fiche produit avec variantes
5. **Admin** : CRUD produits + préparation commandes
6. **Importer tes visuels** : remplacer les placeholders par tes photos TikTok

Veux-tu que je génère maintenant le `app/main.py` FastAPI complet avec le shop fonctionnel ?
