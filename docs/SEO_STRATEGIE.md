# SEO STRATÉGIE - L'Effet Waouh V3

## Objectif: Trafic organique idées déco + produits

### Architecture SEO (validée)

**Sitemap:**
```
/ (homepage tout événements)
/event/mariage
/event/gender-reveal
/event/naissance
/event/baby-shower
/event/bapteme
/event/anniversaire
/event/anniversaire/enfant
/event/anniversaire/30-ans
/event/autres/fiancailles etc

/kits
/kits/mariage-50-pers
/kits/gender-reveal-premium-30-pers

/shop/c/{category_slug}
/shop/p/{product_slug}

/blog
/blog/idees-gender-reveal-fille-garcon
/blog/comment-organiser-baby-shower
/blog/decoration-mariage-petit-budget
/blog/cadeaux-invites-bapteme-original
/blog/organisation-bapteme-guide-complet
/blog/themes-anniversaire-enfant-2024

/guides (pages piliers 2000 mots)
```

**Navigation 9 entrées max (comme demandé):**
MARIAGE | GENDER REVEAL | BABY SHOWER | NAISSANCE | BAPTÊME | ANNIVERSAIRE | PERSONNALISÉ | KITS | PROMOS

Sous-nav hover: ex MARIAGE → Déco salle, Table, Voiture, Gadgets, Accessoires invités/mariés, Cadeaux invités, Jeux, Photobooth, EVJF/EVG, Personnalisés, Kits, Cérémonie, Témoins

### SEO On-page produits

**Titre:** "Kit Anniversaire Licorne 70pcs - Pastel - 15 Enfants - Vaisselle + Pinata Inclus | L'Effet Waouh"
- Mot-clé principal + attributs + bénéfice + marque

**Meta desc:** "Kit complet licorne 70pcs pour 15 enfants: déco, vaisselle, pinata, sachets. Thème pastel best-seller 2024. Livraison 48h. Économisez 15%."

**Slug:** kit-anniversaire-licorne-70pcs-pastel-15-enfants (mots-clés)

**Contenu fiche:**
- H1: nom produit
- H2: Contenu du pack, Personnalisation, Livraison, Avis, FAQ
- FAQ schema.org: "Le ballon contient-il de l'hélium? Non..."
- Avis schema.org AggregateRating
- Breadcrumb: Accueil > Anniversaire > Enfant > Licorne > Kit 70pcs

### Blog / Magazine (trafic idées)

**Objectif:** capter "idées déco gender reveal", "organiser baby shower", etc.

**10 articles piliers à créer (2000 mots + photos + produits intégrés):**

1. **Idées Gender Reveal 2024-2025: 15 façons originales d'annoncer fille ou garçon**
   - Mots-clés: idee gender reveal, annonce sexe bebe original, gender reveal fille garcon
   - Produits: ballon 90cm, fumigènes, canons, cartes à gratter
   - Search volume: 5400/mois "gender reveal idee"

2. **Comment organiser un Baby Shower parfait: guide complet + checklist**
   - Mots-clés: organiser baby shower, decoration baby shower fille garcon
   - Produits: kits déco 70pcs, vaisselle, jeux pronostics, cadeaux invités
   - Volume: 3600/mois

3. **Décoration mariage petit budget: 20 idées chic sans se ruiner**
   - Mots-clés: decoration mariage pas cher, idee deco mariage
   - Produits: arche ballons blanc/or, chemin gaze, marque-places bois, rideau LED
   - Volume: 2900/mois

4. **Cadeaux invités baptême: 15 idées originales et personnalisables**
   - Mots-clés: cadeau invite bapteme, souvenir bapteme invite
   - Produits: bougies personnalisées, contenants dragées plexi, magnets photo, fioles fleurs séchées
   - Volume: 1900/mois

5. **Organisation baptême: guide complet étapes + checklist**
   - Mots-clés: organiser bapteme, decoration bapteme
   - Volume: 1300/mois

6. **Thèmes anniversaire enfant 2024: 16 idées qui cartonnent (licorne, Harry Potter...)**
   - Mots-clés: theme anniversaire enfant, anniversaire licorne, anniversaire harry potter
   - Produits: kits 70pcs par thème
   - Volume: 8100/mois "theme anniversaire"

7. **Cadeaux naissance originaux: 20 idées qui changent des bodys**
   - Mots-clés: cadeau naissance original, idee cadeau naissance
   - Produits: affiche personnalisée, cartes étapes, cadre empreintes, boîte souvenirs
   - Volume: 2400/mois

8. **EVJF: 10 idées d'accessoires pour une fête inoubliable**
   - Mots-clés: accessoires evjf, decoration evjf
   - Produits: bandeau Team Bride, voile, lunettes cœur

9. **Anniversaire 30 ans: déco rose gold, idées, organisation**
   - Mots-clés: decoration 30 ans, anniversaire 30 ans femme
   - Produits: kit 30 ans rose gold 50pcs, ballons chiffres

10. **Personnalisation: comment rendre votre événement unique**
    - Mots-clés: decoration personnalisee mariage bapteme anniversaire
    - Produits: affiches, ballons bulle, bougies, étiquettes

**Structure article:**
- Intro 150 mots avec mot-clé
- Sommaire ancre
- H2/H3 avec mots-clés
- Photos avant/après + UGC
- Produits intégrés (3-5) avec lien
- FAQ
- CTA kit complet

### Technique SEO

- **Sitemap.xml** auto généré depuis categories + products
- **Robots.txt**
- **Schema.org:** Product, Breadcrumb, FAQ, Article, Organization
- **Vitesse:** CSS 13KB inline, images WebP, lazy load, Vercel CDN
- **Mobile-first:** déjà V2 (hero 100vh, grid 2 cols)
- **Core Web Vitals:** LCP <2.5s (hero image optimisée), CLS 0 (dimensions fixées)
- **Recherche intelligente:** FTS5 + scoring (voir CATALOGUE_INTELLIGENT.md)

### Netlinking & Social

- Pinterest: chaque produit → pin avec lien (trafic SEO Pinterest = moteur recherche visuel)
- Instagram: lien bio → Linktree kits (pas SEO direct mais trafic)
- Partenariats: blogs mariage, baby shower, baptême (guest posts)

### KPIs

- Trafic organique: 0 → 5000 visites/mois en 6 mois (objectif)
- Positions: top 10 sur "kit gender reveal", "cadeau invité baptême personnalisé", "kit anniversaire licorne"
- Conversion organique: 2.5% (vs 1% pub)

### Next

🟢 FAIT: Architecture sitemap, structure fiche produit SEO, 10 idées articles piliers
🟡 EN COURS: Implémentation sitemap.xml, robots.txt, schema.org, blog templates
🔵 ACTION HUMAINE: Google Search Console https://search.google.com/search-console + soumettre sitemap

