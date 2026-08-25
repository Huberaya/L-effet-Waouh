"""
Mapping produit → image correspondante
V3: photos qui correspondent aux produits (fix)
"""
import pathlib

BASE = pathlib.Path(__file__).parent.parent / "static" / "images" / "products"

# Mapping slug → image file (relative to /static/)
# On commence avec 10 images générées, on complètera avec 30+ autres
MAPPING = {
    # Gender Reveal
    "ballon-eclatable-gender-reveal-90cm": "products/gender-reveal-ballon-90cm-rose.jpg",
    "fumigenes-couleur-rose-bleu-lot-2": "products/gender-reveal-fumigenes-rose-bleu.jpg",
    "canon-confettis-gender-reveal-30cm": "products/gender-reveal-canon-confettis.jpg",
    "cartes-a-gratter-boy-or-girl-lot-10": "products/gender-reveal-cartes-gratter.jpg",
    "boite-surprise-gender-reveal-ballons": "products/gender-reveal-boite-surprise.jpg",
    "kit-arche-ballons-gender-reveal-85-pieces": "products/gender-reveal-arche-85pcs.jpg",
    "pack-gender-reveal-essentiel": "products/gender-reveal-ballon-90cm-rose.jpg",
    "pack-gender-reveal-fete-20-personnes": "products/gender-reveal-arche-85pcs.jpg",
    
    # Mariage
    "arche-ballons-mariage-blanc-or-200pcs": "products/mariage-arche-blanc-or-200pcs.jpg",
    "rideau-lumineux-led-3x3m-chaud": "products/mariage-rideau-led-3x3m.jpg",
    "lettres-lumineuses-love-40cm": "products/mariage-lettres-love-40cm.jpg",
    "chemin-table-gaze-blanc-6m": "products/mariage-chemin-gaze-eucalyptus.jpg",
    "centre-table-eucalyptus-artificiel": "products/mariage-chemin-gaze-eucalyptus.jpg",
    "cierges-magiques-lot-50-40cm": "products/mariage-cierges-magiques-40cm.jpg",
    "cierges-magiques-lot-100-40cm": "products/mariage-cierges-magiques-40cm.jpg",
    "contenant-dragees-verre-bouchon-liege-lot-20": "products/mariage-contenants-dragees-verre.jpg",
    "bougies-personnalisees-mariage-lot-10": "products/mariage-bougies-personnalisees.jpg",
    "kit-evjf-bandeau-voile-future-mariee": "products/mariage-evjf-bandeau-voile.jpg",
    "marque-places-bois-coeur-lot-20": "products/mariage-marque-places-bois-coeur.jpg",
    "pack-sortie-mairie-50-personnes": "products/mariage-cierges-magiques-40cm.jpg",
}

# Fallback par event_type / thème / mot-clé
FALLBACK_BY_EVENT = {
    "gender_reveal": "products/gender-reveal-ballon-90cm-rose.jpg",
    "mariage": "products/mariage-arche-blanc-or-200pcs.jpg",
    "bapteme": "products/mariage-bougies-personnalisees.jpg",  # temporaire, sera remplacé par bougie baptême
    "naissance": "products/mariage-chemin-gaze-eucalyptus.jpg",
    "baby_shower": "products/gender-reveal-arche-85pcs.jpg",
    "anniversaire": "products/mariage-lettres-love-40cm.jpg",
    "autre": "products/mariage-rideau-led-3x3m.jpg",
    "multi": "products/gender-reveal-cartes-gratter.jpg",
}

FALLBACK_BY_THEME = {
    "licorne": "products/anniversaire-licorne-70pcs.jpg",
    "princesse": "products/anniversaire-princesse-60pcs.jpg",
    "super": "products/anniversaire-super-heros-60pcs.jpg",
    "foot": "products/anniversaire-football-50pcs.jpg",
    "football": "products/anniversaire-football-50pcs.jpg",
    "espace": "products/anniversaire-espace-60pcs.jpg",
    "dino": "products/anniversaire-dinosaure-50pcs.jpg",
    "dinosaure": "products/anniversaire-dinosaure-50pcs.jpg",
    "sirene": "products/anniversaire-sirene-60pcs.jpg",
    "safari": "products/anniversaire-safari-50pcs.jpg",
    "harry": "products/anniversaire-harry-potter-60pcs.jpg",
    "potter": "products/anniversaire-harry-potter-60pcs.jpg",
    "barbie": "products/anniversaire-barbie-50pcs.jpg",
    "glow": "products/anniversaire-glow-50pcs.jpg",
    "30 ans": "products/anniversaire-30-ans-rose-gold.jpg",
    "30ans": "products/anniversaire-30-ans-rose-gold.jpg",
    "18 ans": "products/anniversaire-30-ans-rose-gold.jpg",
    "bapteme": "products/bapteme-bougie-verre-ambre.jpg",
    "baptême": "products/bapteme-bougie-verre-ambre.jpg",
    "bougie": "products/bapteme-bougie-verre-ambre.jpg",
    "dragees": "products/bapteme-contenant-dragees-plexi.jpg",
    "dragées": "products/bapteme-contenant-dragees-plexi.jpg",
    "magnet": "products/bapteme-magnet-photo.jpg",
    "fiole": "products/bapteme-fiole-fleurs-sechees.jpg",
    "naissance": "products/naissance-guirlande-bienvenue.jpg",
    "bienvenue": "products/naissance-guirlande-bienvenue.jpg",
    "affiche": "products/naissance-affiche-personnalisee.jpg",
    "baby shower": "products/baby-shower-kit-fille-70pcs.jpg",
    "baby-shower": "products/baby-shower-kit-fille-70pcs.jpg",
    "kit mariage": "products/kit-mariage-50-pers.jpg",
    "kit gender": "products/kit-gender-reveal-premium-30-pers.jpg",
    "kit baby": "products/kit-baby-shower-20-pers.jpg",
    "kit bapteme": "products/kit-bapteme-20-invites.jpg",
    "kit baptême": "products/kit-bapteme-20-invites.jpg",
    "kit anniversaire": "products/kit-anniversaire-licorne-15-enfants.jpg",
    "personnalise": "products/affiche-personnalisee-prenom.jpg",
    "personnalisé": "products/affiche-personnalisee-prenom.jpg",
    "ballon bulle": "products/ballon-bulle-personnalise-prenom.jpg",
    "arche": "products/mariage-arche-blanc-or-200pcs.jpg",
    "rideau": "products/mariage-rideau-led-3x3m.jpg",
    "love": "products/mariage-lettres-love-40cm.jpg",
    "gaze": "products/mariage-chemin-gaze-eucalyptus.jpg",
    "cierges": "products/mariage-cierges-magiques-40cm.jpg",
    "marque-places": "products/mariage-marque-places-bois-coeur.jpg",
}

# Mapping direct slug complet pour 37 images
MAPPING.update({
    "bougie-personnalisee-bapteme-verre-ambre-70g": "products/bapteme-bougie-verre-ambre.jpg",
    "contenant-dragees-bapteme-plexi-lot-20": "products/bapteme-contenant-dragees-plexi.jpg",
    "magnets-bapteme-personnalises-lot-15": "products/bapteme-magnet-photo.jpg",
    "fiole-verre-fleurs-sechees-bapteme-lot-15": "products/bapteme-fiole-fleurs-sechees.jpg",
    "guirlande-bienvenue-bebe-dore": "products/naissance-guirlande-bienvenue.jpg",
    "ballons-lettres-baby-dore-40cm": "products/naissance-guirlande-bienvenue.jpg",
    "affiche-naissance-personnalisee-prenom-date": "products/naissance-affiche-personnalisee.jpg",
    "affiche-personnalisee-prenom-date-poids": "products/affiche-personnalisee-prenom.jpg",
    "ballon-bulle-personnalise-prenom-confettis": "products/ballon-bulle-personnalise-prenom.jpg",
    "bougie-personnalisee-prenom-date-70g": "products/bougie-personnalisee-prenom.jpg",
    "kit-anniversaire-licorne-70pcs": "products/anniversaire-licorne-70pcs.jpg",
    "kit-anniversaire-princesse-60pcs": "products/anniversaire-princesse-60pcs.jpg",
    "kit-anniversaire-super-heros-60pcs": "products/anniversaire-super-heros-60pcs.jpg",
    "kit-anniversaire-football-50pcs": "products/anniversaire-football-50pcs.jpg",
    "kit-anniversaire-espace-60pcs": "products/anniversaire-espace-60pcs.jpg",
    "kit-anniversaire-dinosaure-50pcs": "products/anniversaire-dinosaure-50pcs.jpg",
    "kit-anniversaire-sirene-60pcs": "products/anniversaire-sirene-60pcs.jpg",
    "kit-anniversaire-harry-potter-60pcs": "products/anniversaire-harry-potter-60pcs.jpg",
    "kit-anniversaire-barbie-50pcs": "products/anniversaire-barbie-50pcs.jpg",
    "kit-anniversaire-glow-party-50pcs": "products/anniversaire-glow-50pcs.jpg",
    "kit-anniversaire-30-ans-rose-gold-50pcs": "products/anniversaire-30-ans-rose-gold.jpg",
    "kit-mariage-essentiel-50-pers": "products/kit-mariage-50-pers.jpg",
    "kit-gender-reveal-premium-30-pers": "products/kit-gender-reveal-premium-30-pers.jpg",
    "kit-baby-shower-fille-20-pers-complet": "products/kit-baby-shower-20-pers.jpg",
    "kit-bapteme-20-invites-complet": "products/kit-bapteme-20-invites.jpg",
    "kit-anniversaire-licorne-15-enfants": "products/kit-anniversaire-licorne-15-enfants.jpg",
    "kit-deco-baby-shower-fille-70-pieces": "products/baby-shower-kit-fille-70pcs.jpg",
    "kit-deco-baby-shower-garcon-70-pieces": "products/baby-shower-kit-garcon-70pcs.jpg",
})

def get_product_image(product: dict) -> str:
    """Retourne chemin image /static/ pour un produit"""
    slug = product.get('slug','') or ''
    name = (product.get('name','') or '').lower()
    event = product.get('event_type','') or ''
    
    # 1. Direct mapping slug exact
    if slug in MAPPING:
        return f"/static/images/{MAPPING[slug]}"
    
    # 2. Partial slug match
    for key, img in MAPPING.items():
        if key in slug or slug in key:
            return f"/static/images/{img}"
    
    # 3. Theme fallback (licorne, etc)
    for theme, img in FALLBACK_BY_THEME.items():
        if theme in name or theme in slug:
            # Vérifie si fichier existe, sinon fallback event
            full_path = BASE.parent.parent.parent / "app" / "static" / "images" / img
            # On retourne quand même le chemin, même si pas encore généré, pour future
            # Mais si fichier n'existe pas, on continue
            import os
            if os.path.exists(str(full_path)):
                return f"/static/images/{img}"
            # Si pas encore généré, on garde en mémoire pour génération future
            # mais on fallback event pour l'instant
    
    # 4. Event fallback
    if event in FALLBACK_BY_EVENT:
        return f"/static/images/{FALLBACK_BY_EVENT[event]}"
    
    # 5. Default hero
    return "/static/images/01-hero.jpg"

def get_all_product_images():
    """Liste toutes les images produits existantes"""
    import os
    if not BASE.exists():
        return []
    return [f.name for f in BASE.glob("*.jpg")]
