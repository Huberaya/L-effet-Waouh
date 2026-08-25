from .base import BaseAgent

class SupportAgent(BaseAgent):
    """Réponses simples"""
    def analyze(self):
        return {
            "faq": [
                {"q":"Délai livraison?","a":"Stock Nantes 24/48h, Perso 48/72h, Dropship 5-8j affiché"},
                {"q":"Ballon avec hélium?","a":"Non, sans hélium, paille fournie, tient 2-3j"},
                {"q":"Personnalisable?","a":"Oui prénom/date/message/photo/couleur/thème, aperçu live"},
                {"q":"Retour?","a":"14j hors consommable (confettis, cierges, fumigènes)"},
                {"q":"Livraison gratuite?","a":"Dès 75€, sinon 4.90€ Mondial Relay, 6.90€ Colissimo"},
                {"q":"Paiement sécurisé?","a":"Stripe, 3D Secure, PayPal"},
            ]
        }

    def recommend(self):
        return [
            "Réponse auto <2h pour questions simples via LLM + base connaissance",
            "Escalade humaine si complexe (commande spécifique, SAV)",
            "Ton chaleureux, pas commercial agressif, personnalisé prénom + événement"
        ]

    def answer(self, question):
        faq = self.analyze()["faq"]
        q_lower = question.lower()
        for item in faq:
            if any(word in q_lower for word in item["q"].lower().split()):
                return item["a"]
        return "Merci pour votre question! Nous vous répondons sous 2h. Pour urgent: contact@leffetwaouh.fr"
