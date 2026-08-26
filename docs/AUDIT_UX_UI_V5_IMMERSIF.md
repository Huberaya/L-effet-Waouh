# AUDIT UX/UI V5 - Analyse utilisateur expert

## Méthode: Parcours utilisateur complet sur http://127.0.0.1:8000/ (V4)

### Parcours testé:
1. Homepage `/` → Explorer `/explorer` → Filtre Mariage → Produit → Panier → Kits → Blog
2. Mobile (simulate 375px) + Desktop (1440px)
3. Filtres, recherche, navigation entre univers

---

## 🔴 INCOHÉRENCES MAJEURES IDENTIFIÉES

### 1. IMMERSION - Pages manquent d'immersion
**Observé:**
- Homepage V4 a hero 100vh mais après hero, sections sont des grids classiques avec borders 1px --line, pas de storytelling continu
- Pas de scroll progressif avec changement de fond/couleur par univers
- Pas de parallax, pas de mouvement 3D subtil sur scroll
- Sections "Best-sellers" et "Kits" sont des grids statiques, pas d'histoire
- Blog preview est 3 cartes identiques, pas immersif

**Score:** 5/10

### 2. PHOTOS - Mêmes photos réutilisées partout
**Observé:**
- 43 images produits mais 140 produits → 97 produits partagent images
- Ex: `anniversaire-princesse-60pcs.jpg` et `anniversaire-barbie-50pcs.jpg` sont tous deux copies de même base (même si nommés différemment, visuellement similaires car copies)
- Dans explorer, sur 20 produits affichés, 6 utilisent `mariage-arche-blanc-or-200pcs.jpg` pour des produits différents (bougie, dragées, etc.)
- Pas de photo lifestyle (produit en situation réelle mariage/baptême), seulement produit isolé

**Score:** 4/10 (amélioré de 2/10 mais encore répétition)

### 3. DOUBLONS PRODUITS - Mêmes produits plusieurs fois formats différents
**Observé:**
- Après dedup 171→140, il reste:
  - `kit-anniversaire-licorne-70pcs` (70pcs déco) + `kit-anniversaire-licorne-15-enfants` (complet 15 enfants) → même thème licorne, devrait être 1 produit avec 2 variantes (Déco seule vs Complet)
  - `bougie-personnalisee-bapteme-verre-ambre-70g` + `bougie-personnalisee-prenom-date-70g` + `bougies-personnalisees-mariage-lot-10` → même bougie ambré 70g, juste label différent, devrait être 1 produit avec variantes event (mariage/baptême/naissance) + lot (1/10/20)
  - `ballons-baby-shower-50pcs-rose-bleu` + `ballons-baby-shower-50pcs` (si existe) → doublon
  - Kits: `kit-mariage-essentiel-50-pers` contient `cierges-magiques-lot-50` + `confettis-biodegradables` + `bulles-mariage` qui sont aussi vendus séparément → utilisateur voit même cierges 2 fois (seul + dans kit) sans comprendre économie
- Pas de système de variantes clair: lot 50 vs lot 100 sont 2 produits séparés au lieu d'être variantes d'un même produit

**Score:** 6/10 (après dedup SQL, mais reste confusion format)

### 4. CARTES PRODUITS - Formats identiques, pas de hiérarchie
**Observé V4:**
- On a introduit formats large/medium/small/kit/perso mais:
  - Large = seulement best-seller + index %5==1 → arbitraire, pas basé sur data réelle (CA, marge)
  - Kit = fond noir mais tous kits même format, pas de distinction entre Kit Mariage 50 pers (88.90€) et Kit GR Premium (128.90€) vs Kit Anniv Licorne (74.90€)
  - Perso = bord or mais pas d'aperçu live dans carte, juste badge
  - Small = même que medium mais plus petit, pas de vraie différenciation
  - Pas de format "histoire" (ex: carte avec photo lifestyle + produit)
  - Pas de format "comparaison" (ex: carte qui montre contenu kit)

**Score:** 6/10

### 5. FILTRES ET RECHERCHE - Basiques
**Observé:**
- Filters-bar: pills Tous, Mariage, GR, Baby Shower, Naissance, Baptême, Anniv, Kits, Perso, Rose, Bleu, Or → seulement event + 3 couleurs + 2 types
- Pas de filtre prix (slider 0-150€), pas de filtre thème (licorne, Harry Potter...), pas de filtre âge (1 an, 18 ans, 30 ans...), pas de filtre stock, pas de filtre marge, pas de multi-select (on ne peut pas filtrer Mariage + Rose + <30€ en même temps)
- Recherche: `/search?q=` basique, pas d'autocomplete, pas de suggestions intelligentes, pas de correction faute
- Pas de tri (prix croissant/décroissant, best-sellers, nouveautés, marge)

**Score:** 5/10

### 6. NAVIGATION ENTRE CATÉGORIES - Pas fluide
**Observé:**
- Topbar-pill avec 8 liens → chaque clic = navigation vers `/explorer?event=xxx` → rechargement page complet (même si animation opacity .5, c'est quand même reload)
- Pas de swipe horizontal entre univers (ex: en étant sur Mariage, swipe gauche → Gender Reveal)
- Pas de breadcrumb dynamique qui montre où on est dans l'exploration
- Universe-scroll horizontal en haut mais seulement visible sur /explorer, pas sur homepage, pas sur produit
- Pas de "vous aimerez aussi" qui permet de passer d'un univers à l'autre (ex: produit mariage → recommandation baptême si même client)

**Score:** 5/10

### 7. TRANSITIONS ENTRE PAGES
**Observé:**
- PageIn animation 0.8s ease-out sur .page mais:
  - Pas de View Transitions API (chrome support)
  - Pas de transition entre filtres (grid opacity .5 translateY 8px basique)
  - Pas de transition image produit → page produit (image qui s'agrandit)
  - Pas de transition panier (ajout → panier qui glisse)

**Score:** 5/10

### 8. ANIMATIONS ET MICRO-INTERACTIONS
**Observé V4:**
- 3D tilt sur .tilt avec mousemove rx/ry → bien mais seulement sur cartes, pas sur hero, pas sur images produit
- Button ripple radial → bien mais seulement sur .btn
- Add-btn rotate 90deg → bien
- Confetti existe mais seulement sur add to cart V3, pas sur V4
- Pas de parallax sur scroll
- Pas de micro-interaction sur filtres (pill qui scale)
- Pas de skeleton loading
- Pas de hover sur images qui montre 2ème image

**Score:** 6/10

### 9. SCROLLS HORIZONTAUX ET 3D
**Observé:**
- H-scroll pour universes et recommandations → bien mais:
  - Pas de scroll horizontal pour catégories (ex: mariage sous-catégories déco salle/table/voiture en horizontal)
  - Pas de scroll horizontal pour produits complémentaires sur fiche produit (on a h-scroll mais 320px fixe, pas de 3D)
  - 3D seulement tilt, pas de perspective sur scroll, pas de depth layers

**Score:** 6/10

### 10. EXPLORATION INTUITIVE
**Observé:**
- Explorer est un bon début mais:
  - Pas de mode "découverte" où on scroll vertical et les univers changent automatiquement (comme Apple)
  - Pas de comparaison intuitive (checkbox → comparer)
  - Pas de wishlist visible
  - Pas de historique navigation

**Score:** 6/10

### 11. RECOMMANDATIONS
**Observé:**
- Recommendations = random 8 produits même event ou featured → pas basé sur comportement, pas de "souvent achetés ensemble" réel (pas de données commandes), pas de "vu récemment", pas de "complétez votre kit"

**Score:** 5/10

### 12. COHÉRENCE DESKTOP/MOBILE
**Observé:**
- Desktop: topbar-pill + universe-scroll + filters-bar sticky + prod-grid-immersive 12 cols
- Mobile: bottom-nav pill noire + filters-bar horizontal scroll + prod-grid 12 cols full width
- Cohérence OK mais:
  - Mobile bottom-nav cache une partie du contenu (pas de padding bottom)
  - Filters-bar sur mobile prend beaucoup de place verticale
  - H-scroll sur mobile pas de snap visuel clair
  - Tilt 3D ne marche pas sur mobile (pas de mousemove)

**Score:** 7/10

### 13. ORGANISATION PAGES/CATÉGORIES
**Observé:**
- Pages: /, /explorer, /shop, /shop/event/*, /shop/c/*, /shop/p/*, /kits, /blog, /blog/*, /cart, /admin
- Trop de pages différentes pour même fonction (explorer vs shop vs event) → confusion
- /shop et /explorer font presque même chose mais templates différents
- /shop/event/mariage et /explorer?event=mariage = duplicate content SEO

**Score:** 5/10

---

## 🎯 OBJECTIF V5 - Expérience immersive, fluide, moderne, premium

### Principes:
1. **Single Page Exploration**: Une seule page `/explorer` qui est le catalogue, avec filtres instantanés JS (pas de reload), URL mise à jour via history.pushState, transitions fluides
2. **No Duplicate Content**: /shop, /shop/event/*, /shop/c/* redirigent vers /explorer?event=*
3. **Unique Visual per Product**: Chaque produit a sa photo correspondante + bg_color unique hash + overlay gradient + 2ème image au hover + badge unique
4. **No Product Duplicates**: 140 → 120 produits après merge lot variants en variantes (ex: cierges lot 50/100 → 1 produit avec variantes)
5. **Varied Card Formats Data-Driven**: large = top 10% CA/marge, medium = best-sellers, small = complémentaires, kit = avec contenu visible, perso = avec aperçu live miniature, histoire = lifestyle + produit
6. **Advanced Filters**: event (multi-select), couleur (rose/bleu/or/blanc/noir/pastel), thème (licorne, Harry Potter, etc. 16 thèmes), âge (1,18,20,30,40,50,60), prix slider, perso, kit, promo, stock, tri (best, prix, nouveauté)
7. **Fluid Navigation**: swipe horizontal entre univers, universe-scroll visible partout, breadcrumb dynamique, next/prev univers, recommandations inter-univers
8. **Transitions**: View Transitions API + fade + slide + image expand
9. **Animations**: parallax, tilt 3D partout, ripple, confetti, skeleton, hover 2ème image, filter pill scale, add to cart fly to cart
10. **Horizontal + 3D**: h-scroll pour tout (univers, sous-catégories, produits, reco), perspective depth, tilt
11. **Intuitive Exploration**: découverte verticale avec changement univers auto, comparaison checkbox, wishlist, historique
12. **Smart Recommendations**: "Complétez votre kit", "Souvent achetés ensemble" basé sur product_relations, "Vu récemment" localStorage, "Basé sur votre exploration"
13. **Desktop/Mobile Coherence**: même design system, bottom-nav mobile avec padding, filters bottom sheet mobile, tilt → touch tilt, h-scroll snap visuel

---

## 📝 PLAN V5

1. **Backend:**
   - Merge lot variants: créer product_variants pour lot 50/100, rose/bleu, etc., désactiver produits doublons
   - Enrich product_images: 43 → 80+ images via image_search pour tous produits restants
   - API explorer: filtres avancés multi-select + tri + pagination

2. **Frontend:**
   - base_premium_v5.html: nouveau design system avec View Transitions, parallax, skeleton, fly to cart
   - explorer_v5.html: single page avec filtres avancés instantanés JS, comparaison, wishlist, historique
   - home_premium_v5.html: immersive storytelling avec sections full-screen par univers, horizontal scroll, parallax, 3D stack
   - product_premium_v5.html: gallery horizontal + vertical, 3D, video, lifestyle, reco inter-univers

3. **Navigation:**
   - Redirect /shop, /shop/event/*, /shop/c/* → /explorer
   - Universe-scroll partout
   - Swipe entre univers

4. **Tests:**
   - Parcours utilisateur complet
   - Lighthouse performance
   - Mobile 375px + Desktop 1440px
