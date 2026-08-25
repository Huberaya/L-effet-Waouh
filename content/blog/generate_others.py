articles = {
"organiser-baby-shower": {"kw":"organiser baby shower","vol":3600,"title":"Comment organiser un Baby Shower parfait: guide complet + checklist","products":"kits 70pcs, vaisselle, jeux pronostics"},
"decoration-mariage-petit-budget": {"kw":"decoration mariage pas cher","vol":2900,"title":"Décoration mariage petit budget: 20 idées chic sans se ruiner","products":"arche blanc/or, chemin gaze, marque-places"},
"cadeaux-invites-bapteme": {"kw":"cadeau invite bapteme","vol":1900,"title":"Cadeaux invités baptême: 15 idées originales et personnalisables","products":"bougies perso, dragées plexi, magnets, fioles fleurs"},
"themes-anniversaire-enfant": {"kw":"theme anniversaire enfant","vol":8100,"title":"Thèmes anniversaire enfant 2024: 16 idées qui cartonnent (licorne, Harry Potter...)","products":"kits licorne, Harry Potter, super-héros, Barbie, Glow"},
"organisation-bapteme-guide": {"kw":"organiser bapteme","vol":1300,"title":"Organisation baptême: guide complet étapes + checklist","products":"bougies, contenants, déco table, guirlande prénom"},
"cadeaux-naissance-originaux": {"kw":"cadeau naissance original","vol":2400,"title":"Cadeaux naissance originaux: 20 idées qui changent des bodys","products":"affiche perso, cartes étapes, cadre empreintes"},
"evjf-accessoires": {"kw":"accessoires evjf","vol":1200,"title":"EVJF: 10 idées d'accessoires pour une fête inoubliable","products":"bandeau Team Bride, voile, lunettes coeur"},
"anniversaire-30-ans": {"kw":"decoration 30 ans","vol":2100,"title":"Anniversaire 30 ans: déco rose gold, idées, organisation","products":"kit 30 ans rose gold 50pcs, ballons chiffres"},
"personnalisation-evenement": {"kw":"decoration personnalisee mariage","vol":900,"title":"Personnalisation: comment rendre votre événement unique","products":"affiches, ballons bulle, bougies, étiquettes"},
}
for slug, data in articles.items():
    content = f"""# {data['title']}

**Mot-clé:** {data['kw']} ({data['vol']}/mois)

## Intro

Organiser {slug.replace('-',' ')}? Guide complet 2024-2025 avec idées testées, checklist, budget et produits L'Effet Waouh stock Nantes 48h.

## Idées principales

1. Produit d'appel best-seller
2. Kit complet
3. Personnalisable prénom/date
4. Déco table/salle
5. Cadeaux invités

## Checklist

- Déco: {data['products']}
- Animation: jeux, photobooth
- Souvenirs: bougies, magnets, cartes
- Budget: Essentiel 49.90€, Fête 84.90€, Premium 128.90€

## Produits recommandés

{data['products']}

## FAQ

Délai 24/48h stock, 48/72h perso, 5-8j dropship. Sans hélium. Personnalisable oui.

## CTA

Voir kits → /kits + Boutique → /shop/event/{slug.split('-')[0] if '-' in slug else 'mariage'}
"""
    open(f"content/blog/{slug}.md","w").write(content)
    print(f"OK {slug}")
