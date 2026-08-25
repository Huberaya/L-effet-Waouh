# BUSINESS MODEL HYBRIDE - L'Effet Waouh V3

## Objectif: Rentabilité max + panier moyen x4 + risque min

### Synthèse décision
**HYBRIDE** = Stock best-sellers (60%) + Print-on-Demand personnalisés (25%) + Dropshipping complémentaire (15%)

Pas 100% stock (risque), pas 100% dropship (qualité/délai).

---

## 1. STOCK - Best-sellers à forte rotation (60% CA)

**Quoi:**
- Gender reveal: ballon 90cm, canons confettis, fumigènes T1, cartes à gratter
- Mariage: cierges magiques 40cm (marge 70%), confettis bio, bulles, marque-places bois
- Anniversaire: kits 50-70pcs (licorne, super-héros, 30 ans rose gold), bougies chiffres
- Baptême: bougies personnalisées verre ambré (stock vide + étiquette à poser), contenants dragées plexi, magnets
- Naissance: guirlandes, ballons BABY, cartes étapes

**Fournisseurs:**
- FR: Artiflor (naissance/baptême), P'Tit Clown (4000 refs fête, 48h), Feuillazur Lyon
- EU: Labis BE, Marco BE (baptême/mariage rubans boîtes), Europages
- Faire.com wholesale (MOQ 200€, pas 50pcs Chine)
- Alibaba seulement si MOQ 50-100 validé + échantillon qualité (ex: Patimate Balloons 4409 ventes/mois Amazon, $1.72 wholesale vs $6.68 retail = marge 74%)

**Coûts:**
- Achat: 2-8€ moyen
- Vente: 9.90-28.90€
- Marge brute: 65-75%
- Stock initial: 1500€ pour 40 références x 20pcs

**Logistique:**
- Local Nantes, étagères, cartons 20x20x10
- Préparation <24h, Mondial Relay + Colissimo

### 2. PRINT-ON-DEMAND Personnalisés (25% CA, marge 80%)

**Quoi:**
- Affiches A4 prénom date poids (PDF auto généré → imprimé local Printful/Imprimeur Nantes)
- Bougies: stock pot vide + cire + étiquette imprimée à la demande (Zebra)
- Étiquettes rondes 4cm: Sticker Mule ou imprimante thermique couleur
- Ballons bulle personnalisés: vinyle découpé plotter Silhouette
- Livres d'or bois gravés: laser local (Atelier gravure Nantes)
- Mugs, bodys, bavoirs: Printful/POD EU (délai 3-5j)

**Workflow V3:**
Produit → Personnalisation (prénom/date/message/photo/couleur/thème) → Aperçu live canvas → Commande → Fichier print → Production 24-48h

**Prix:**
- Affiche 12.90€ (coût 2€ print + 1€ papier = marge 77%)
- Bougie 6.90€ (coût 2€ = marge 71%)
- Marge POD >80% car valeur perçue personnalisation

**Tech:**
- Canvas preview JS (base.html déjà critical CSS)
- Stockage fichiers perso dans /uploads (S3 Vercel Blob future)
- Table `product_personalizations` (product_id, field_type, required)

### 3. DROPSHIPPING Complémentaire (15% CA, marge 30-40%)

**Quoi:**
- Gros/encombrants: arche métal 3m, lettres lumineuses LOVE 40cm, néon Mr&Mrs, pinatas
- Faible rotation: thèmes anniversaire niche (safari, cosmos), produits entreprise, PACS, retraite

**Fournisseurs:**
- BigBuy (EU, 48h, pas de stock), Brandsdistribution, Dropshippers FR via Faire
- Jamais AliExpress direct client (délai/qualité)

**Règle:** Toujours afficher délai 5-8j, pas 24h. Marge plus faible mais 0 stock.

---

## 2. CALCUL RENTABILITÉ

### Panier moyen actuel vs V3
- Actuel: 1 produit ~19.90€ (30 produits, pas de kits)
- V3 avec kits + upsell: objectif 74.90€ (x3.7)

Exemple Kit Mariage Essentiel 50 pers:
- 50 cierges (coût 9€) + 1kg confettis (5€) + 24 bulles (4€) + 20 marque-places (3.8€) + livre or (11€) = coût 32.8€, vente 88.90€, marge 56.1€ (63%)
- Vs vente séparée 108€ mais client achète 1 seul produit → panier x4

### Coûts complets (exemple commande 74.90€)
- Produit: 26€
- Livraison: 6.90€ (facturée 4.90€, perte 2€) → seuil gratuit 75€ pour inciter +1 produit
- Emballage: 1.2€
- Frais Stripe: 1.5% + 0.25 = 1.37€
- Pub (CAC): 12€ (Meta/TikTok)
- SAV/retours: 1.5€ (3% retours)
- **Marge nette: 74.90 -26 -2 -1.2 -1.37 -12 -1.5 = 30.83€ (41%)**

### CAC / LTV
- CAC cible: 12€ (ROAS 3)
- LTV: client revient 1.8x/an pour autres événements (naissance → baptême → 1 an → anniversaires)
- LTV 1 an: 74.90 x 1.8 = 134.82€, marge 55€ → LTV/CAC = 4.6 (sain >3)

### Produits les plus rentables (analyse V3)
1. Cierges magiques lot 50: achat 9€ vente 28.90€ marge 70%
2. Affiches personnalisées: achat 2€ vente 12.90€ marge 84%
3. Bougies personnalisées: achat 2€ vente 6.90€ marge 71% + volume (20-30 par commande)
4. Kits anniversaire 70pcs: achat 8€ vente 24.90€ marge 68% + best-seller licorne
5. Cartes à gratter lot 10: achat 2.2€ vente 9.90€ marge 78%

**Produits d'appel (marge faible mais trafic):** ballons chiffres 2.90€, confettis 3.90€ → amènent vers kits

---

## 3. STOCKAGE & MOQ

| Fournisseur | MOQ | Délai | Qualité | Marge |
|-------------|-----|-------|---------|-------|
| P'Tit Clown FR | 1 | 48h | ★★★★ | 55% |
| Artiflor FR | 50€ | 72h | ★★★★★ | 60% |
| Faire EU | 200€ | 5j | ★★★★ | 65% |
| Alibaba (Patimate) | 50pcs | 15j + douane | ★★★ | 74% |

Décision: Démarrer FR/EU (48h-5j) pour cashflow, tester Alibaba seulement si best-seller validé >50 ventes/mois.

---

## 4. AUTOMATISATION V3

- **Sourcing Agent:** veille prix MOQ, alerte rupture
- **Catalogue Agent:** génère fiches SEO (titre optimisé, bénéfices, FAQ)
- **Stock Agent:** commande auto si stock <10
- **POD Agent:** génère PDF affiche, envoie à Printful

---

## 5. NEXT STEPS

🟢 FAIT: Analyse fournisseurs FR/EU/Alibaba, calcul marge, définition hybride
🟡 EN COURS: Implémentation tables `product_personalizations`, `kits`, preview canvas
🔵 ACTION HUMAINE REQUISE:
- Ouvrir compte Faire.com (lien: https://www.faire.com) - 2 min OAuth
- Commander échantillons Artiflor (https://www.artiflor.fr) - 50€ test
- Choisir imprimeur Nantes pour affiches (ou Printful https://www.printful.com)
- Ouvrir compte Stripe (si pas déjà) pour encaissement
