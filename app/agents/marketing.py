from .base import BaseAgent

class MarketingAgent(BaseAgent):
    """Acquisition pub - ne dépense pas sans autorisation"""
    def analyze(self):
        return {
            "channels": ["Meta Ads","TikTok Ads","Google Shopping","Pinterest Ads"],
            "best_products_for_ads": [
                {"sku":"GR-BAL-90-001","name":"Ballon 90cm","marge":"74%","hook":"4409 ventes/mois Amazon"},
                {"sku":"KIT-MAR-400","name":"Kit Mariage 50 pers","marge":"63%","hook":"Panier x4 88.90€"},
                {"sku":"ANN-LICORNE-200","name":"Kit Licorne 70pcs","marge":"68%","hook":"Best-seller 2024"},
            ],
            "status":"Préparé, 0€ dépensé (attente autorisation)"
        }

    def recommend(self):
        return [
            "Meta: Audience femmes 25-45 intérêt mariage/grossesse/bébé, créas vidéo 15s ballon, landing /event/gender-reveal, Pixel + CAPI, remarketing 30j/7j/180j",
            "TikTok: 18-35 fête/déco/bébé, créas UGC, landing kits, Pixel",
            "Google Shopping: flux produits GTIN, best-sellers + kits, kw 'ballon gender reveal'",
            "Pinterest: femmes 25-54, pins produits + idées, landing blog",
            "⚠️ Ne dépenser aucun budget sans autorisation humaine - campagnes prêtes"
        ]

    def prepare_campaign(self, channel, product_sku):
        return {
            "channel": channel,
            "product": product_sku,
            "audience": "Femmes 25-45 mariage/bébé" if channel=="Meta" else "18-35 fête",
            "crea": "Vidéo 15s ballon éclatement + texte bénéfice",
            "landing": "/event/gender-reveal ou /kits",
            "tracking": "Pixel installé",
            "budget_proposed": "10€/j test, attente autorisation",
            "status": "🔵 Prêt, non lancé"
        }
