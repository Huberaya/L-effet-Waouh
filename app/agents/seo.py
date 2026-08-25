from .base import BaseAgent

class SEOAgent(BaseAgent):
    """Contenu blog/guides"""
    def analyze(self):
        return {
            "articles_plan": [
                {"slug":"idees-gender-reveal","kw":"idee gender reveal","vol":5400,"products":"ballon 90cm, fumigènes, canons"},
                {"slug":"organiser-baby-shower","kw":"organiser baby shower","vol":3600,"products":"kits 70pcs, vaisselle, jeux"},
                {"slug":"decoration-mariage-petit-budget","kw":"decoration mariage pas cher","vol":2900,"products":"arche blanc/or, chemin gaze"},
                {"slug":"cadeaux-invites-bapteme","kw":"cadeau invite bapteme","vol":1900,"products":"bougies perso, dragées plexi, magnets"},
                {"slug":"themes-anniversaire-enfant","kw":"theme anniversaire enfant","vol":8100,"products":"kits licorne, Harry Potter, super-héros"},
            ],
            "sitemap_count": 171,
            "need": "10 articles 2000 mots + sitemap.xml + schema.org"
        }

    def recommend(self):
        return [
            "Écrire 10 articles piliers 2000 mots avec intro 150 mots kw, sommaire ancre, H2/H3, photos, 3-5 produits intégrés, FAQ, CTA kit",
            "Sitemap.xml auto généré depuis categories+products - FAIT",
            "Schema.org: Product, Breadcrumb, FAQ, Article, Organization",
            "Pinterest: chaque produit → pin avec lien (moteur recherche visuel)"
        ]

    def generate_article_outline(self, slug):
        outlines = {
            "idees-gender-reveal": {
                "title":"15 idées Gender Reveal originales 2024-2025: fille ou garçon",
                "h2":["1. Le ballon éclatable 90cm - best-seller","2. Fumigènes T1 extérieur","3. Canons confettis","4. Boîte surprise","5. Cartes à gratter","Checklist complète","Budget"],
                "cta":"Kit GR Premium 30 pers 128.90€"
            }
        }
        return outlines.get(slug, {"title":slug,"h2":["Intro","Idées","Checklist","Produits"]})
