# NOUVELLE ARCHITECTURE - L'Effet Waouh V3 Marque Grands Moments de Vie

## Positionnement validé
**De:** Boutique gadgets mariage
**Vers:** Marque spécialisée produits, accessoires, décorations, cadeaux, gadgets pour grands moments de vie et événements festifs

**Slogan nouveau:** "Tout ce qu'il vous faut pour créer un événement inoubliable — et le rendre inoubliable"
**Baseline:** "La marque des grands moments de vie"

---

## 1. NAVIGATION SIMPLE (9 entrées max)

```
MARIAGE • GENDER REVEAL • BABY SHOWER • NAISSANCE • BAPTÊME • ANNIVERSAIRE • PERSONNALISÉ • KITS • PROMOTIONS
```

**Sous-nav intelligente au hover:**
- MARIAGE: Décoration | Accessoires invités | Accessoires mariés | Cadeaux invités | Jeux | Photobooth | Table | Salle | Voiture | EVJF/EVG | Personnalisés | Kits mariage | Cérémonie | Témoins
- GENDER REVEAL: Ballons | Confettis | Fumigènes | Boîtes surprise | Kits révélation | Déco rose/bleu | Photo | Jeux | Cartes | Badges | Table | Kits complets | Personnalisables
- BABY SHOWER: Kits déco | Ballons | Guirlandes | Vaisselle | Table | Jeux | Cadeaux invités | Photo | Personnalisée | Kits complets
- NAISSANCE: Cadeaux | Déco | Boîtes souvenirs | Photo | Cartes étapes | Affiches | Personnalisés | Bébé | Parents | Coffrets | Baby Shower
- BAPTÊME: Déco | Cadeaux invités | Contenants | Bougies | Table | Souvenirs | Coffrets | Personnalisés | Parrain/Marraine
- ANNIVERSAIRE: Enfant | Adulte | 18 ans | 20 ans | 30 ans | 40 ans | 50 ans | 60 ans | Thèmes (Princesse, Licorne, Super-héros, Football, Espace, Animaux, Tropical, Élégant, Années 80/90)
- PERSONNALISÉ: Prénom | Date | Message | Photo | Couleur | Thème
- KITS: Kit Mariage | Kit Gender Reveal | Kit Baby Shower | Kit Naissance | Kit Baptême | Kit Anniversaire
- PROMOTIONS: Best-sellers | Nouveautés | -20% | Packs

---

## 2. SITEMAP & SEO ARCHITECTURE

```
/ (home) -> Tout pour créer un événement inoubliable
/shop -> Tous produits + filtres
/shop/c/{slug} -> Catégorie (ex: mariage-decoration)
/shop/p/{slug} -> Fiche produit avec Parfait pour + FAQ + avis
/shop/event/{type} -> Page événementielle SEO (ex: gender-reveal)
/shop/kits -> Tous les kits
/shop/kits/{slug} -> Kit détaillé
/blog -> Magazine
/blog/{slug} -> Article SEO (ex: idees-gender-reveal, organiser-baby-shower, decoration-mariage)
/guides/{slug} -> Guide complet
/search?q= -> Recherche intelligente (produit, événement, couleur, thème, âge)
/personnalisation -> Page explicative personnalisation
/c/{promo} -> Promotions
```

**Pages événementielles SEO à créer:**
- /event/mariage-decoration
- /event/gender-reveal-idees
- /event/baby-shower-organisation
- /event/naissance-cadeaux
- /event/bapteme-decoration
- /event/anniversaire-enfant-themes
- /event/anniversaire-30-ans

---

## 3. RECHERCHE INTELLIGENTE

**Champ recherche header qui comprend:**
- Produit: "ballon", "cierge", "confettis"
- Événement: "mariage", "gender reveal", "baptême"
- Couleur: "rose", "bleu", "or", "blanc"
- Thème: "licorne", "princesse", "football", "espace"
- Âge: "18 ans", "30 ans", "1 an"
- Prénom: "Léa" -> propose produits personnalisables

**Exemple:** Client tape "gender reveal fille garçon"
-> Retourne: Ballons 90cm rose/bleu, fumigènes lot 2, canons confettis, pack essentiel, cartes à gratter

**Implémentation:** 
- SQL: `WHERE name LIKE %q% OR event_type LIKE %q% OR tags LIKE %q%`
- Puis scoring: event_type match +20, couleur match +15, thème match +10
- Autocomplete avec 5 suggestions max

---

## 4. FICHE PRODUIT NOUVELLE (conversion)

```
[Photos pro + vidéo TikTok]
Titre optimisé SEO
Bénéfices (3 bullets)
Prix + Marge + Stock + Livraison
Personnalisation -> Prénom/Date/Message/Photo/Couleur -> Aperçu live
Variantes rose/bleu/lot
Quantité + Add to cart confetti
Parfait pour: [badges événements]
Description + Dimensions + Matériaux + Contenu pack + Délai
FAQ (3-5 questions)
Avis vérifiés (avec photos)
Produits complémentaires (upsell/cross-sell)
```

---

## 5. KITS ÉVÉNEMENTIELS (panier moyen x4)

**Structure kit:**
- Kit = produit parent qui contient plusieurs produits
- Table `kits` + `kit_items` (product_id, quantity)
- Prix kit = sum(products) -15% (économie affichée)
- Page kit avec checklist "Tout pour organiser ma..."

**Kits à créer:**
- Kit Mariage Essentiel (50 pers): 50 cierges + 1kg confettis + 24 bulles + livre or = 89.90€ (au lieu de 108€)
- Kit Gender Reveal Essentiel: ballon + fumigènes + canons + cartes + poudre = 44.90€
- Kit Baby Shower Fille 70pcs: arche + guirlandes + vaisselle + jeux = 59.90€
- Kit Naissance Bienvenue: guirlande + ballons BABY + kit empreintes + boîte souvenirs = 49.90€
- Kit Baptême 20 invités: 20 bougies personnalisées + 20 contenants dragées + déco table = 69.90€
- Kit Anniversaire Enfant Licorne: arche + vaisselle + pinata + jeux = 39.90€

---

## 6. UPSELL / CROSS-SELL

**Règles:**
- Ballons → propose déco complémentaire (guirlande, arche)
- Cadeaux invités → propose emballage (pochon, étiquette personnalisée)
- Kit Gender Reveal → propose accessoires complémentaires (badges Team Boy/Girl, cartes pronostics)
- Produit personnalisé → propose autres personnalisés assortis (ex: bougie + contenant dragées même prénom)

**Implémentation:**
- Table `product_relations` (product_id, related_id, type: upsell/cross-sell/complement)
- Sur fiche produit: "Souvent achetés ensemble" (4 produits)
- Dans panier: "Ajoute 3 canons pour 10.50€ et débloque livraison gratuite !"
- Après add to cart: popup "Les clients qui ont acheté ce ballon ont aussi pris..."

---

## 7. MOBILE-FIRST

- Topbar hamburger + recherche sticky
- Hero 70vh sur mobile (vs 100vh desktop)
- Portfolio grid 1 col sur mobile, 2 cols tablette, 3-4 desktop
- Boutons 48px min height pour pouce
- Checkout en 1 colonne, Apple Pay / Google Pay si Stripe
- Images optimisées WebP + lazy loading
- PWA possible plus tard

---

## 8. TECH ARCHITECTURE V3

```
Vercel (front) -> FastAPI (api/index.py) -> Postgres Neon (prod) / SQLite /tmp (demo)
Static: /app/static/* servi par FastAPI StaticFiles
Templates: Jinja2 avec inline CSS fallback
Search: SQL LIKE + scoring
Kits: table kits + kit_items
Personnalisation: product_personalization_options + order_item_personalization
Avis: reviews table + is_verified_purchase
Blog: posts table + markdown
```

**Nouveaux fichiers à créer:**
- sql/seed_categories_v3_full.sql (50+ catégories)
- sql/seed_products_v3_full.sql (150+ produits)
- app/routers/search.py (recherche intelligente)
- app/routers/kits.py
- app/templates/shop/kits.html
- app/templates/blog/
- app/models/kit.py, personalization.py

---

## 9. CONVERSION & CONFIANCE

- Badges: "Stock Nantes", "Expédition 24h", "14j retours", "Paiement sécurisé"
- Preuve sociale: avis vérifiés avec photos, "127 personnes ont acheté ce produit ce mois"
- Urgence légitime: "Plus que 8 en stock" si stock <10, pas de fausse urgence
- Livraison gratuite seuil visuel avec progress bar
- Photos pro + vidéos TikTok démo
- FAQ sur chaque fiche

---

## Objectif: Passer de boutique 30 produits -> marque 150+ produits, 9 univers, kits, personnalisation, SEO, mobile-first
