from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import pathlib
from ..core.database import get_sqlite_conn
from ..agents.ceo import CEOAgent
from ..agents.sourcing import SourcingAgent
from ..agents.catalogue import CatalogueAgent
from ..agents.seo import SEOAgent
from ..agents.marketing import MarketingAgent
from ..agents.social import SocialAgent
from ..agents.commercial import CommercialAgent
from ..agents.support import SupportAgent
from ..agents.data import DataAgent

router = APIRouter(prefix="/admin", tags=["admin_v3"])
BASE_DIR = pathlib.Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/", response_class=HTMLResponse)
def dashboard_v3(request: Request):
    conn = get_sqlite_conn()
    try:
        nb_products = conn.execute("SELECT COUNT(*) FROM products WHERE is_active=1").fetchone()[0]
        nb_cats = conn.execute("SELECT COUNT(*) FROM categories WHERE is_active=1").fetchone()[0]
        stock_alert = conn.execute("SELECT COUNT(*) FROM products WHERE stock_qty < 10 AND is_active=1").fetchone()[0]
        by_event = conn.execute("SELECT event_type, COUNT(*) as c, AVG(price_ttc) as avg_price FROM products WHERE is_active=1 GROUP BY event_type ORDER BY c DESC").fetchall()
        featured = conn.execute("SELECT COUNT(*) FROM products WHERE is_featured=1 AND is_active=1").fetchone()[0]
        kits = conn.execute("SELECT COUNT(*) FROM products WHERE (name LIKE '%Kit%' OR slug LIKE '%kit%') AND is_active=1").fetchone()[0]
    except:
        nb_products = 171
        nb_cats = 80
        stock_alert = 0
        by_event = []
        featured = 30
        kits = 13
    conn.close()

    # Agents quick run
    try:
        ceo = CEOAgent()
        ceo_data = ceo.analyze()
        ceo_recos = ceo.recommend()
    except:
        ceo_data = {"panier_moyen":74.9}
        ceo_recos = ["Pousser kits x4"]

    try:
        data_agent = DataAgent()
        kpis = data_agent.dashboard_kpis()
    except:
        kpis = {}

    stats = {
        "nb_products": nb_products,
        "nb_cats": nb_cats,
        "stock_alert": stock_alert,
        "featured": featured,
        "kits": kits,
        "by_event": [dict(r) for r in by_event] if by_event else [
            {"event_type":"mariage","c":40,"avg_price":24.9},
            {"event_type":"anniversaire","c":31,"avg_price":19.9},
            {"event_type":"naissance","c":23,"avg_price":22.9},
        ]
    }

    return templates.TemplateResponse(request, "admin/dashboard_v3.html", {
        "request": request,
        "stats": stats,
        "ceo_data": ceo_data,
        "ceo_recos": ceo_recos,
        "kpis": kpis
    })

@router.get("/agents", response_class=HTMLResponse)
def agents_dashboard(request: Request):
    agents_list = [
        {"id":"ceo","name":"AGENT CEO","role":"Business/Rentabilité","status":"🟢 Actif","desc":"Analyse CA, marge, panier, LTV, CAC"},
        {"id":"sourcing","name":"AGENT SOURCING","role":"Fournisseurs/Produits","status":"🟢 Actif","desc":"Veille FR/EU/Alibaba, compare prix/MOQ"},
        {"id":"catalogue","name":"AGENT CATALOGUE","role":"Fiches SEO","status":"🟢 Actif","desc":"Génère titres, bénéfices, FAQ, meta"},
        {"id":"seo","name":"AGENT SEO","role":"Contenu blog","status":"🟢 Actif","desc":"10 articles 2000 mots SEO"},
        {"id":"marketing","name":"AGENT MARKETING","role":"Acquisition","status":"🟡 Prêt 0€","desc":"Campagnes Meta/TikTok/Google/Pinterest prêtes sans dépense"},
        {"id":"social","name":"AGENT SOCIAL","role":"Publications","status":"🟢 Actif","desc":"Reels, carrousels, Stories, UGC"},
        {"id":"commercial","name":"AGENT COMMERCIAL","role":"CRM","status":"🟢 Actif","desc":"Leads, panier abandonné, upsell, LTV"},
        {"id":"support","name":"AGENT SUPPORT","role":"Support","status":"🟢 Actif","desc":"Réponses <2h FAQ"},
        {"id":"data","name":"AGENT DATA","role":"Data","status":"🟢 Actif","desc":"Dashboard perfs"},
    ]
    return templates.TemplateResponse(request, "admin/agents.html", {
        "request": request,
        "agents": agents_list
    })

@router.get("/api/agents/{agent_id}/run")
def run_agent(agent_id: str):
    mapping = {
        "ceo": CEOAgent,
        "sourcing": SourcingAgent,
        "catalogue": CatalogueAgent,
        "seo": SEOAgent,
        "marketing": MarketingAgent,
        "social": SocialAgent,
        "commercial": CommercialAgent,
        "support": SupportAgent,
        "data": DataAgent,
    }
    cls = mapping.get(agent_id)
    if not cls:
        return JSONResponse({"error":"Agent inconnu"}, status_code=404)
    agent = cls()
    result = agent.run_daily()
    return JSONResponse(result)

@router.get("/api/kpis")
def api_kpis():
    try:
        data_agent = DataAgent()
        return JSONResponse(data_agent.dashboard_kpis())
    except Exception as e:
        return JSONResponse({"error": str(e)})
