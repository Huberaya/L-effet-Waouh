# DASHBOARD + AGENTS IA - V3

## Dashboard Ventes

**URL:** /admin/dashboard

**KPIs:**
- CA jour/semaine/mois, commandes, panier moyen, marge
- Produits best-sellers (CA, qty), faibles rotations (<5/mois)
- Stock alerte <10, rupture
- Source trafic, conversion, CAC, ROAS
- Email: ouverture, clic, conversion
- Réseaux: abonnés, vues, engagement, clics, ventes

**Tables:**
- `v_orders_daily` déjà dans schema
- Requêtes: SELECT SUM(total_ttc) FROM orders WHERE status IN ('paid',...) GROUP BY date

---

## Dashboard Marketing

- Trafic: GA4/Plausible API
- Source: utm_source, referrer
- Conversion: commandes / visiteurs
- CAC: pub spend / commandes
- ROAS: CA / pub spend

---

## Dashboard Réseaux (quand comptes créés)

- Instagram Graph API, TikTok API, Pinterest API
- Abonnés, vues Reels, engagement, clics lien bio, ventes attribuées

---

## Dashboard Produits

- Best-sellers, marge par produit, stock
- Alerte: stock <10, marge <50%, rotation faible

---

## AGENTS IA (9 agents comme demandé)

### 1. AGENT CEO — Business / Rentabilité
- Rôle: analyse CA, marge, panier, LTV, CAC, propose actions
- Input: orders, products, marketing spend
- Output: rapport hebdo + reco (ex: augmenter prix kit 30 ans, baisser pub GR si ROAS <2)
- Tech: Python + LLM + SQL

### 2. AGENT SOURCING — Fournisseurs / Produits
- Rôle: veille fournisseurs FR/EU/Alibaba, compare prix/MOQ/délais/qualité, propose nouveaux produits
- Input: web_search fournisseurs, Faire API, Alibaba
- Output: tableau comparatif + reco achat
- Déjà fait: analyse Artiflor, P'Tit Clown, Faire, Alibaba Patimate

### 3. AGENT CATALOGUE — Fiches produits SEO
- Rôle: génère titres optimisés, descriptions bénéfices, FAQ, meta, tags
- Input: produit brut + best-sellers Amazon/Etsy
- Output: fiche complète V3 (Parfait pour, dimensions, contenu pack, FAQ)
- Tech: LLM + template

### 4. AGENT SEO — Contenu blog/guides
- Rôle: écrit articles 2000 mots SEO (idées GR, organiser Baby Shower...)
- Input: mot-clé, produits liés
- Output: article + schema.org + produits intégrés
- 10 articles piliers déjà définis dans SEO_STRATEGIE.md

### 5. AGENT MARKETING — Acquisition pub
- Rôle: prépare campagnes Meta/TikTok/Google Shopping/Pinterest Ads, audiences, créas, textes, landing, tracking, remarketing
- Input: produits best-sellers, marges, personas
- Output: campagnes prêtes, sans dépenser budget sans autorisation (comme demandé)
- Ne dépense rien sans autorisation humaine

### 6. AGENT SOCIAL MEDIA — Publications
- Rôle: crée contenu Reels/carrousels/Stories/inspirations/démos/produits/avant-après/idées/UGC/saisonnier
- Input: produits, tendances TikTok/Instagram (sans copie illégale)
- Output: calendrier éditorial + visuels + légendes + hashtags
- Analyse tendances via web_search, mais crée original

### 7. AGENT COMMERCIAL — Prospects/Clients CRM
- Rôle: gère leads, relance panier abandonné, upsell, fidélisation
- Input: users, orders, events
- Output: emails personnalisés, segmentation, reco cross-sell

### 8. AGENT SUPPORT — Réponses simples
- Rôle: répond questions simples (délai, livraison, personnalisation, retours)
- Input: FAQ, commandes
- Output: réponse auto <2h, escalade si complexe
- Tech: LLM + base connaissance

### 9. AGENT DATA — Performances
- Rôle: analyse données ventes, marketing, réseaux, produits, propose optimisations
- Input: toutes tables
- Output: dashboard + alertes + reco

---

## Implémentation technique

**Structure:**
```
/app/agents/
  ceo.py
  sourcing.py
  catalogue.py
  seo.py
  marketing.py
  social.py
  commercial.py
  support.py
  data.py
  base.py (classe mère)
```

**Base Agent:**
```python
class BaseAgent:
  def __init__(self, db_conn, llm_client):
  def run_daily(self): # tâche quotidienne
  def analyze(self): # analyse
  def recommend(self): # reco
```

**Cron:** via Vercel Cron ou GitHub Actions daily

---

## Transparence (comme demandé)

Toujours distinguer:
- 🟢 FAIT: réel, en base, déployé
- 🟡 EN COURS: dev en cours
- 🔵 ACTION HUMAINE REQUISE: lien officiel direct, OAuth/API, jamais demander mdp en clair
- 🔴 IMPOSSIBLE: techniquement impossible seul

Ne jamais prétendre créé/publié/ajouté/vendu/abonnés si pas réel.

---

## Next

🟢 FAIT: Définition 9 agents, KPIs dashboard, vues SQL v_orders_daily, v_product_stock
🟡 EN COURS: Implémentation dashboard /admin, agents base classes
🔵 ACTION HUMAINE:
- Créer comptes sociaux (Instagram, TikTok, Pinterest, Meta Business)
- Ouvrir Brevo/Resend pour emails
- Connecter GA4/Plausible
- Stripe pour paiement (si pas déjà)
