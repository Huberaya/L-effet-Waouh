from .base import BaseAgent

class CommercialAgent(BaseAgent):
    """Prospects/Clients CRM"""
    def analyze(self):
        conn = self.get_conn()
        try:
            prospects = conn.execute("SELECT COUNT(*) as c FROM users WHERE role='client'").fetchone()
            abandoned = conn.execute("SELECT COUNT(*) as c FROM carts WHERE id NOT IN (SELECT cart_id FROM cart_items) OR id IN (SELECT cart_id FROM cart_items)").fetchone()
            conn.close()
            return {
                "prospects": prospects["c"] if prospects else 0,
                "carts": abandoned["c"] if abandoned else 0,
                "segments": ["mariage","GR","naissance","baby shower","bapteme","anniversaire","par panier","par source","par comportement"]
            }
        except:
            return {"prospects":0,"carts":0}

    def recommend(self):
        return [
            "Segmentation par event_type, date événement, panier moyen, source, comportement",
            "Panier abandonné: 1h rappel + photo + livraison gratuite 75€, 24h +10% WAOUH10, 72h dernier rappel + kit",
            "Cross-sell: mariage → lune de miel, naissance → baptême 3 mois + 1 an, GR → baby shower",
            "LTV: client revient 1.8x/an pour autres événements"
        ]

    def email_flow(self, flow_name):
        flows = {
            "panier_abandonne": [
                {"delay":"1h","subject":"Votre panier vous attend + livraison gratuite dès 75€","content":"Rappel + photo produits"},
                {"delay":"24h","subject":"-10% pour finaliser votre commande","content":"+10% WAOUH10 + urgence stock"},
                {"delay":"72h","subject":"Dernier rappel + idée kit complet","content":"Alternative kit + témoignage"},
            ],
            "bienvenue": [
                {"delay":"J0","subject":"Bienvenue -10%","content":"BIENVENUE10 + best-sellers"},
                {"delay":"J2","subject":"Notre histoire + personnalisation","content":"Storytelling + perso"},
                {"delay":"J5","subject":"Kits complets + avis","content":"Kits x4 + témoignages"},
            ]
        }
        return flows.get(flow_name, [])
