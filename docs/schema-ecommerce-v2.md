# Schéma E-commerce V2 - L'Effet Waouh

## Vision : de la location à la vente + location hybride

**Actuel V1** : tu loues du matériel cher (photobooth 360 à 550€/jour) avec opérateur.
**Objectif V2** : tu vends des consommables à forte rotation (cierges, confettis, ballons gender reveal à 10-30€) + tu continues la location premium. La vente finance le stock location.

C'est le modèle **Amazon + Rent the Runway** : la vente fait du volume quotidien, la location fait la marge week-end.

---

## 1. Schéma SQL - Explication

### Tables cœur vente

```
categories (arbo)
  ├── products (1 produit = 1 SKU principal)
  │   ├── product_variants (couleur rose/bleu, lot x1/x3/x6)
  │   ├── product_images (plusieurs photos)
  │   └── product_categories (N-N)
  ├── cart / cart_items (panier invité ou connecté)
  ├── orders / order_items (commande + snapshot prix)
  ├── reviews (avis)
  └── stock_movements (traçabilité)

+ shipping_methods, coupons, addresses, wishlists
+ tables V1 conservées : users, leads, bookings (location), invoices
```

### Pourquoi ce schéma ?

- **products.price_ht / price_ttc + tva_rate** : obligatoire pour facturation française TVA. Tu as 20% sur déco, mais 5.5% sur livres ? Prévoir.
- **stock_qty dans products ET variants** : le ballon rose et bleu ont des stocks séparés.
- **price_ttc_at_add dans cart_items** : si tu changes ton prix demain, le panier d'hier garde l'ancien prix (légal).
- **orders.shipping_address_json / billing_address_json** : snapshot JSON de l'adresse au moment de la commande. Si le client déménage, la facture reste valide.
- **order_items.name_snapshot / sku_snapshot** : idem, si tu renommes un produit, la commande historique ne change pas.
- **stock_movements** : pour savoir pourquoi ton stock est passé de 150 à 20 (vente, casse, inventaire).

### Index critiques

- `idx_products_event` : pour filtrer rapidement `/c/gender-reveal`
- `idx_orders_status` : dashboard "commandes à préparer"
- `v_product_stock` : vue qui calcule stock total produit + variantes

---

## 2. Différence Location vs Vente dans le code

|  | Location (V1) | Vente (V2) |
|---|---|---|
| Table | `bookings` | `orders` + `order_items` |
| Prix | 550€ / jour | 10€ définitif |
| Stock | 1 photobooth loué = indisponible ce jour | 150 ballons -1 à chaque vente |
| Logistique | Opérateur + camion | Colissimo + étiquette |
| Marge | 70% après amortissement | 60-75% immédiate |
| Fréquence | Samedi | Tous les jours |

**Tu dois garder les 2.** Le client qui achète un pack gender reveal à 44.90€ aujourd'hui reviendra louer le photobooth 360 à 550€ pour son mariage dans 6 mois.

---

## 3. Migration depuis V1

Fichier `sql/migrate_from_v1.sql` à créer :

```sql
-- Garder users, leads, bookings tels quels
-- Créer nouvelles tables via schema_v2.sql
-- Optionnel : transformer certains ALACARTE en produits vente
INSERT INTO products(sku, name, price_ttc, event_type, is_consumable)
SELECT 'LEGACY-'||id, pack, total, 'mariage', 0 FROM bookings LIMIT 0; -- exemple
```

---

## 4. Exemple de requête business

**Top 5 produits gender reveal les plus rentables :**
```sql
SELECT p.sku, p.name, p.stock_qty, 
       (p.price_ttc - p.cost_price) as marge_unitaire,
       (p.price_ttc - p.cost_price)/p.price_ttc*100 as marge_pct,
       SUM(oi.quantity) as vendus
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
WHERE p.event_type='gender_reveal'
GROUP BY p.id
ORDER BY marge_unitaire * vendus DESC LIMIT 5;
```

**Commandes à préparer ce matin (Nantes) :**
```sql
SELECT number, email, total_ttc, shipping_method_code, created_at
FROM orders WHERE status='paid' ORDER BY created_at ASC;
```

---

## 5. Prochaine étape : FastAPI

Le schéma est prêt pour FastAPI + SQLAlchemy :

```python
class Product(Base):
  __tablename__ = 'products'
  id = Column(Integer, primary_key=True)
  sku = Column(String, unique=True)
  variants = relationship("ProductVariant")
  images = relationship("ProductImage")
  categories = relationship("Category", secondary="product_categories")
```
