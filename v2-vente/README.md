# v2-vente - Arborescence Catalogue Vente

Cette arborescence est la **vitrine commerciale** de ta future boutique.
Chaque dossier = un univers avec ses produits best-sellers.

```
v2-vente/
├── README.md (ce fichier)
├── gender-reveal/      -> 12 produits, marge 70%, viral TikTok
├── naissance/          -> 6 produits, récurrence après gender reveal
├── mariage/            -> 9 produits vente (cierges, confettis) + location premium
├── baby-shower/        -> 3 kits
└── packs/              -> Packs combinés 44.90€ et 84.90€

Total: 30 produits, 20 catégories, stock 1975 unités, 1500€ achat initial
```

## Gender Reveal - Détail (ton univers #1)

| SKU | Produit | Prix vente | Coût achat | Marge | Stock | Pourquoi best-seller |
|-----|---------|------------|------------|-------|-------|---------------------|
| GR-BAL-90-001 | Ballon éclatable 90cm + confettis | 10€ | 2.5€ | 75% | 150 | Le produit d'appel TikTok #1 |
| GR-FUM-002 | Fumigènes lot 2 rose/bleu | 14.90€ | 4€ | 73% | 80 | Vidéo slow-motion |
| GR-CAN-30-003 | Canon confettis 30cm | 3.90€ | 0.9€ | 77% | 300 | Upsell panier |
| GR-BOX-004 | Boîte surprise à ballons | 24.90€ | 8€ | 68% | 25 | Effet waouh ouverture |
| GR-GRAT-005 | Cartes à gratter lot 10 | 9.90€ | 2.2€ | 78% | 100 | Pour famille |
| GR-KIT-ARCHE-007 | Kit arche 85pcs | 28.90€ | 9€ | 69% | 40 | Déco complète |
| PACK-GR-ESSENT-040 | Pack Essentiel (ballon+fumigènes+canons+cartes+poudre) | 44.90€ | 15€ | 66% | 40 | Panier moyen boosté |

**Stratégie:** Le client vient pour ballon 10€, tu upsell canons x3 à 10.50€, puis pack essentiel 44.90€.

## Naissance - Récurrence

Cliente gender reveal mois 5 -> baby shower mois 7 -> naissance mois 9
Même cliente = 3 achats = 10€ + 24.90€ + 16.90€ = 51.80€ LTV

Produits:
- Guirlande Bienvenue Bébé Dorée 7.90€ (marge 77%)
- Ballons BABY doré 12.90€
- Kit empreintes 16.90€
- Boîte souvenirs 22.90€

## Mariage Vente - Cross-sell location

Tu loues photobooth 360 à 550€ le samedi, tu vends en plus:
- Cierges lot 50 à 28.90€ (achat 9€)
- Confettis bio 1kg à 19.90€ (achat 5€)
- Pack sortie mairie 50 pers à 49.90€ (achat 18€, marge 64%)

Le client location devient client vente, et inversement.

## Où sont les fichiers techniques ?

- `../sql/schema_v2.sql` : schéma SQL complet
- `../sql/seed_categories.sql` : 20 catégories
- `../sql/seed_products_*.sql` : 30 produits + variantes rose/bleu
- `../app/` : boutique FastAPI fonctionnelle (Phase 3)
- `../docs/` : docs business

## Lancer la boutique Phase 3

```bash
cd waouh-v2
pip install -r requirements.txt
python scripts/init_db.py
uvicorn app.main:app --reload --port 8000
# -> http://localhost:8000
# -> http://localhost:8000/shop/event/gender_reveal
# -> http://localhost:8000/admin-v2
```
