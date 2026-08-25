from .base import BaseAgent

class SourcingAgent(BaseAgent):
    """Fournisseurs / Produits"""
    def analyze(self):
        conn = self.get_conn()
        try:
            low_stock = conn.execute("SELECT sku, name, stock_qty FROM products WHERE stock_qty < 10 AND is_active=1 ORDER BY stock_qty LIMIT 10").fetchall()
            no_sales = conn.execute("""
                SELECT p.sku, p.name, p.stock_qty FROM products p 
                LEFT JOIN order_items oi ON oi.product_id=p.id 
                WHERE oi.id IS NULL AND p.is_active=1 LIMIT 10
            """).fetchall()
            conn.close()
            return {
                "low_stock": [dict(r) for r in low_stock],
                "no_sales": [dict(r) for r in no_sales],
                "fournisseurs": [
                    {"name":"P'Tit Clown FR","moq":1,"delai":"48h","marge":"55%","url":"https://www.ptitclown.com"},
                    {"name":"Artiflor FR","moq":"50€","delai":"72h","marge":"60%","url":"https://www.artiflor.fr"},
                    {"name":"Faire EU","moq":"200€","delai":"5j","marge":"65%","url":"https://www.faire.com"},
                    {"name":"Patimate Alibaba","moq":"50pcs","delai":"15j","marge":"74%","url":"https://www.alibaba.com"},
                ]
            }
        except Exception as e:
            return {"error": str(e)}

    def recommend(self):
        a = self.analyze()
        recos = []
        if a.get("low_stock"):
            recos.append(f"Commander {len(a['low_stock'])} produits en rupture imminente: {', '.join([x['sku'] for x in a['low_stock'][:3]])}")
        recos.append("Tester Alibaba seulement si best-seller validé >50 ventes/mois + échantillon qualité")
        recos.append("Priorité FR/EU pour cashflow 48h-5j, pas AliExpress direct client")
        return recos
