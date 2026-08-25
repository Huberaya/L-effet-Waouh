from .base import BaseAgent

class CEOAgent(BaseAgent):
    """Business / Rentabilité"""
    def analyze(self):
        conn = self.get_conn()
        try:
            ca = conn.execute("SELECT COALESCE(SUM(total_ttc),0) as ca, COUNT(*) as nb, AVG(total_ttc) as panier FROM orders WHERE status IN ('paid','preparing','shipped','delivered')").fetchone()
            best = conn.execute("SELECT p.name, SUM(oi.quantity) as qty, SUM(oi.total_ttc) as ca FROM order_items oi JOIN products p ON p.id=oi.product_id GROUP BY p.id ORDER BY ca DESC LIMIT 5").fetchall()
            conn.close()
            return {
                "ca_total": ca["ca"] if ca else 0,
                "nb_commandes": ca["nb"] if ca else 0,
                "panier_moyen": round(ca["panier"],2) if ca and ca["panier"] else 0,
                "best_sellers": [dict(r) for r in best] if best else []
            }
        except Exception as e:
            return {"error": str(e), "ca_total": 0, "panier_moyen": 0}

    def recommend(self):
        analysis = self.analyze()
        recos = []
        panier = analysis.get("panier_moyen",0)
        if panier < 50:
            recos.append("Panier moyen <50€: pousser kits x4 (ex: Kit Mariage 88.90€) + seuil livraison gratuite 75€ + upsell")
        if panier < 75:
            recos.append("Panier <75€: afficher 'Ajoutez X€ pour livraison gratuite' + cross-sell sachets cadeaux")
        recos.append("Produits les plus rentables à pousser: cierges 70% marge, affiches perso 84%, bougies perso 71%")
        recos.append("LTV: client naissance → relance baptême 3 mois + 1 an")
        return recos
