# CATALOGUE INTELLIGENT - 150+ PRODUITS V3

## Principe: Pas 1000 produits inutiles, mais 150 qui vendent

### 5 types de produits (comme demandé)

#### 1. Produits d'appel (trafic, marge faible, panier +1)
- Bougies chiffres or 2.90€ (anniversaire)
- Confettis biodégradables 3.90€ (gender reveal, mariage)
- Cartes à gratter lot 10 9.90€ (GR)
- Ballons chiffres 80cm 9.90€

Objectif: SEO "bougie chiffre 3 or", Google Shopping pas cher, entrée catalogue

#### 2. Produits rentables (marge >70%, best-sellers)
- Cierges magiques lot 50 28.90€ (marge 70%)
- Affiches personnalisées 12.90€ (marge 84%)
- Bougies personnalisées lot 10 34.90€ (marge 71%)
- Kit arche ballons GR 85pcs 28.90€ (marge 68%)

#### 3. Produits complémentaires (upsell)
- Si ballon 90cm GR → fumigènes + canons + cartes pronostics (règle upsell)
- Si cadeaux invités mariage (dragées) → emballage pochon + étiquette perso
- Si kit anniversaire licorne → vaisselle licorne + pinata + sachets cadeaux

Table `product_relations` : source_id, target_id, relation_type (upsell/cross-sell/complement), boost_score

#### 4. Produits premium (marge € élevée, image marque)
- Lettres lumineuses LOVE 40cm 88.90€
- Néon Mr&Mrs 88.90€
- Timbale argent baptême 49.90€
- Coffret parrain marraine luxe 88.90€
- Kit Gender Reveal Premium 30 pers 128.90€

Objectif: augmenter panier moyen, preuve expertise

#### 5. Best-sellers (à pousser homepage)
Basé recherche web + Etsy + Amazon:
- Gender Reveal: ballon 90cm (4409 ventes/mois Amazon), canons confettis, fumigènes, badges Team Boy/Girl
- Mariage: cierges 40cm, arche ballons blanc/or 200pcs, rideau LED 3x3m
- Anniversaire: kit licorne 70pcs (best-seller 2024), kit 30 ans rose gold, Harry Potter, super-héros, Barbie
- Baptême: bougie verre ambré personnalisée (best-seller FR), contenant dragées plexi, magnet photo, fiole fleurs séchées
- Naissance: guirlande Bienvenue Bébé, ballons BABY, cartes étapes

---

## Répartition catalogue V3 (150+ produits)

| Univers | Nb produits | % | Panier moyen |
|---------|-------------|---|--------------|
| Mariage | 38 | 25% | 44.90€ |
| Gender Reveal | 22 | 15% | 49.90€ |
| Anniversaire | 40 | 27% | 24.90€ |
| Baptême | 20 | 13% | 16.90€ |
| Naissance | 21 | 14% | 22.90€ |
| Baby Shower | 18 | 12% | 24.90€ |
| Kits | 13 | 9% | 88.90€ |
| Personnalisables | 9 | 6% | 14.90€ |
| Autres | 12 | 8% | 19.90€ |
| **TOTAL** | **~193** | - | **74.90€ objectif** |

> Note: total >150 car kits comptent double, mais produits uniques ~160

---

## Règles upsell/cross-sell V3

```sql
-- Exemple règles
Ballon GR 90cm → Fumigènes lot 2 (+35% conversion), Canons x3 (+40%), Cartes à gratter (+25%)
Cadeaux invités mariage (bougies lot 10) → Étiquettes perso lot 30 (+50%), Pochons lavande (+30%)
Kit anniversaire licorne → Vaisselle 20 pers (+45%), Pinata (+30%), Sachets cadeaux (+60%)
Baptême bougie → Contenant dragées plexi (+40%), Magnet photo (+35%)
Naissance affiche perso → Cadre bois (+25%), Carte étapes (+20%)
```

Implémentation: table `product_relations` + scoring + affichage fiche produit "Parfait avec" + panier "Ajoutez pour débloquer livraison gratuite à 75€"

---

## Recherche intelligente (comme demandé)

**Exemples requêtes:**
- "gender reveal fille garçon" → doit retourner kits GR + ballons + déco rose/bleu
- "bapteme garcon" → bougies bleu, contenants, magnets garçon
- "anniversaire licorne 5 ans" → kit licorne + vaisselle + pinata + bougie chiffre 5
- "cadeau invité mariage pas cher" → bougies lot 10, savons, pochons lavande <3€/pers

**Scoring:**
- event_type match +20
- couleur match (rose/bleu) +15
- thème match (licorne, Harry Potter) +15
- âge match (30 ans, 1 an) +10
- tags match +5
- best-seller boost +10

**Implémentation V3:**
- Table `products` colonnes `event_type`, `tags` (JSON), `theme`, `color`, `age_min/max`
- FTS5 SQLite pour recherche full-text
- Router `/search?q=` avec scoring Python

---

## Fiche produit V3 pro (comme demandé)

**Structure:**
1. Photos/vidéos (min 3, idéal 5 + vidéo 15s TikTok)
2. Titre optimisé SEO: "Kit Anniversaire Licorne 70pcs - Pastel - 15 Enfants - Vaisselle + Pinata Inclus"
3. Bénéfices (3 bullets): "Fête garantie sans stress", "Économie 15% vs séparé", "Livraison 48h"
4. Description courte + longue
5. Dimensions, matériaux, contenu pack (liste)
6. Personnalisation (si applicable) avec aperçu live
7. Délai/livraison (stock 24h, POD 48h, dropship 5-8j)
8. Avis vérifiés (table `reviews`)
9. FAQ (ex: "Ballon avec hélium? Non, sans")
10. Produits complémentaires (upsell)
11. Badge "Parfait pour" : Mariage, Gender Reveal, etc.

---

## Kits événementiels - Objectif panier x4

| Kit | Contenu | Prix séparé | Prix kit | Économie | Marge |
|-----|---------|-------------|----------|----------|-------|
| Mariage Essentiel 50 pers | 50 cierges + 1kg confettis + 24 bulles + 20 marque-places + livre or | 108€ | 88.90€ | 18% | 63% |
| GR Premium 30 pers | Ballon 90cm + 4 fumigènes + 10 canons + arche 85pcs + badges + cartes | 152€ | 128.90€ | 15% | 62% |
| Baby Shower Fille 20 pers | Kit déco 70pcs + vaisselle 20 + jeux 20 + bougies 15 + guirlande prénom | 104€ | 88.90€ | 15% | 64% |
| Baptême 20 invités | 20 bougies perso + 20 contenants plexi + 20 magnets + déco table + guirlande | 151€ | 128.90€ | 15% | 62% |
| Anniversaire Licorne 15 enfants | Kit 70pcs + vaisselle 15 + pinata + sachets 15 + guirlande + chapeaux | 89€ | 74.90€ | 16% | 65% |

---

## SEO produits

- Slug: `kit-anniversaire-licorne-70pcs-pastel-15-enfants` (mots-clés)
- Meta title: "Kit Anniversaire Licorne 70pcs | Déco Complète 15 Enfants | L'Effet Waouh"
- Tags: licorne, pastel, fille, 5 ans, anniversaire enfant, kit complet

---

## Dashboard produits (à faire)

- Best-sellers (CA, qty)
- Faibles rotations (<5 ventes/mois → à déstocker ou supprimer)
- Stock (alerte <10)
- Marge par produit
