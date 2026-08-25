from .base import BaseAgent

class CatalogueAgent(BaseAgent):
    """Fiches produits SEO"""
    def analyze(self):
        conn = self.get_conn()
        try:
            missing_desc = conn.execute("SELECT COUNT(*) as c FROM products WHERE (long_desc IS NULL OR long_desc='') AND is_active=1").fetchone()
            no_images = conn.execute("SELECT COUNT(*) as c FROM products WHERE id NOT IN (SELECT product_id FROM product_images) AND is_active=1").fetchone()
            conn.close()
            return {
                "missing_desc": missing_desc["c"] if missing_desc else 0,
                "no_images": no_images["c"] if no_images else 0
            }
        except Exception as e:
            return {"error": str(e)}

    def recommend(self):
        return [
            "Générer fiches V3: titre optimisé SEO 'Kit Anniversaire Licorne 70pcs - Pastel - 15 Enfants', bénéfices 3 bullets, dimensions, contenu pack, FAQ, Parfait pour badges",
            "Ajouter min 3 photos + vidéo 15s TikTok par produit",
            "Schema.org Product + FAQ + AggregateRating"
        ]

    def generate_fiche(self, product_name, event_type, attributes):
        """Template génération fiche"""
        title = f"{product_name} - {attributes.get('color','')} - {attributes.get('qty','')} - {event_type}"
        benefits = [
            "Fête garantie sans stress - tout compris",
            "Économie 15% vs achat séparé",
            "Livraison 48h Nantes + avis vérifiés"
        ]
        return {
            "title_seo": title,
            "benefits": benefits,
            "faq": [
                {"q":"Délai?","a":"24/48h stock, 48/72h perso, 5-8j dropship"},
                {"q":"Personnalisable?","a":"Oui prénom/date/message/photo"},
                {"q":"Hélium?","a":"Non, sans hélium, paille fournie"}
            ]
        }
