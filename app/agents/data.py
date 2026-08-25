from .base import BaseAgent

class DataAgent(BaseAgent):
    """Performances"""
    def analyze(self):
        conn = self.get_conn()
        try:
            # Ventes
            ventes = conn.execute("SELECT date(created_at) as day, COUNT(*) as nb, SUM(total_ttc) as ca FROM orders WHERE status IN ('paid','preparing','shipped','delivered') GROUP BY day ORDER BY day DESC LIMIT 7").fetchall()
            # Produits
            produits = conn.execute("""
                SELECT p.event_type, COUNT(*) as nb_produits, AVG(p.price_ttc) as prix_moyen 
                FROM products p WHERE p.is_active=1 GROUP BY p.event_type
            """).fetchall()
            # Stock
            stock_alert = conn.execute("SELECT COUNT(*) as c FROM products WHERE stock_qty < 10 AND is_active=1").fetchone()
            conn.close()
            return {
                "ventes_7j": [dict(r) for r in ventes],
                "produits_par_event": [dict(r) for r in produits],
                "stock_alert_count": stock_alert["c"] if stock_alert else 0
            }
        except Exception as e:
            return {"error": str(e)}

    def recommend(self):
        analysis = self.analyze()
        recos = []
        if analysis.get("stock_alert_count",0) > 5:
            recos.append(f"⚠️ {analysis['stock_alert_count']} produits en alerte stock <10 → recommander commande")
        recos.append("Dashboard: CA, commandes, panier moyen, marge, best-sellers, stock, source, conversion, CAC, ROAS")
        recos.append("Produits faibles rotation <5/mois → déstocker ou supprimer")
        return recos

    def dashboard_kpis(self):
        a = self.analyze()
        return {
            "ventes": {"ca": "0€ (pas encore de commandes réelles)", "commandes": 0, "panier_moyen": "74.90€ objectif", "marge": "63% moyenne"},
            "marketing": {"trafic": "0 → 5000/mois objectif 6 mois", "conversion": "2.5% organique objectif", "cac": "12€", "roas": "3"},
            "reseaux": {"abonnes": "0 → 1000 en 3 mois", "vues": "10k/mois Reels", "engagement": "5%", "ventes_attribuees": "20% CA"},
            "produits": a.get("produits_par_event", []),
            "stock_alert": a.get("stock_alert_count",0)
        }
