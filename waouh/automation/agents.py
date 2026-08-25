#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Équipe d'agents IA — L'Effet Waouh.
Lit la base de données réelle, re-scoring des leads, calcul des KPI,
génération du rapport quotidien (reports/latest.md + reports/kpis.json).
Lancement : python3 automation/agents.py
"""
import os, sqlite3, json, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "waouh.db")
REPORTS = os.path.join(BASE, "reports")
os.makedirs(REPORTS, exist_ok=True)
NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")

PIPELINE = ["Nouveau lead", "Qualifié", "Contacté", "Réponse", "Rendez-vous",
            "Proposition", "Négociation", "Client", "Fidélisation"]
SECTOR_KW = ["mariage", "wedding", "planner", "traiteur", "lieu", "domaine", "photographe",
             "fleuriste", "dj", "salle", "réception", "reception", "déco", "deco", "animation",
             "événementiel", "evenementiel", "château", "chateau"]

def con():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; return c

def one(sql, args=()):
    r = con().execute(sql, args).fetchone(); return r[0] if r else 0

def score(source, sector, email, phone, website):
    sc = 0
    if email and "@" in email: sc += 15
    if phone: sc += 10
    if website: sc += 10
    if sector:
        for k in SECTOR_KW:
            if k in sector.lower(): sc += 15; break
    src = (source or "").lower()
    if src == "site": sc += 20
    elif src == "partenariat": sc += 25
    elif src == "prospection": sc += 10
    elif src == "social": sc += 15
    return min(sc, 100)

def run():
    c = con()
    # 1) re-scoring automatique des leads
    for l in c.execute("SELECT * FROM leads").fetchall():
        s = score(l["source"], l["sector"] or "", l["email"] or "", l["phone"] or "", l["website"] or "")
        c.execute("UPDATE leads SET score=? WHERE id=?", (s, l["id"]))
    c.commit()

    # 2) KPI business
    ca_encaisse = one("SELECT COALESCE(SUM(amount),0) FROM invoices WHERE status IN ('payée','paye','acompte')")
    ca_devis = one("SELECT COALESCE(SUM(amount),0) FROM invoices WHERE status='brouillon'")
    n_clients = one("SELECT COUNT(*) FROM users WHERE role='client'")
    n_leads = one("SELECT COUNT(*) FROM leads")
    n_bookings = one("SELECT COUNT(*) FROM bookings")
    panier = (one("SELECT AVG(total) FROM bookings WHERE status NOT IN ('annulé','annule')") or 0)
    hot = c.execute("SELECT * FROM leads WHERE score>=70 AND status NOT IN ('Client','Fidélisation') ORDER BY score DESC").fetchall()
    devis_attente = c.execute("SELECT b.*, i.number FROM bookings b LEFT JOIN invoices i ON i.booking_id=b.id WHERE b.status='devis'").fetchall()
    leads_nouveaux = c.execute("SELECT * FROM leads WHERE status='Nouveau lead' ORDER BY id DESC").fetchall()
    n_erreurs = one("SELECT COUNT(*) FROM events WHERE kind='error'")
    n_emails = one("SELECT COUNT(*) FROM outbox WHERE status='queued'")
    c.close()

    # 3) rapport multi-agents
    L = []
    L.append("# Rapport quotidien — " + TODAY)
    L.append("")
    L.append("## 🤖 Agent CEO")
    L.append(f"- CA encaissé : **{ca_encaisse:,.0f} €** · Devis en attente : **{ca_devis:,.0f} €**")
    L.append(f"- Clients : {n_clients} · Réservations : {n_bookings} · Panier moyen : ~{panier:,.0f} €")
    L.append(f"- Marge estimée (75 % du CA) : **{ca_encaisse*0.75:,.0f} €**")
    L.append("")
    L.append("## 📈 Agent Commercial")
    L.append(f"- Leads actifs : {n_leads} · Leads chauds (score ≥ 70) : {len(hot)}")
    for l in hot[:10]:
        L.append(f"  - 🔥 #{l['id']} {l['contact'] or l['company'] or 'Sans nom'} — score {l['score']} — {l['status']} — {l['email'] or 'sans e-mail'}")
    if not hot: L.append("  - Aucun lead chaud pour l'instant.")
    L.append(f"- Devis à relancer : {len(devis_attente)}")
    for b in devis_attente[:10]:
        L.append(f"  - 💰 Devis {b['number']} — {b['name']} — {b['event_date']} — {b['total']} €")
    L.append("")
    L.append("## 📣 Agent Social Media")
    n_posts = one("SELECT COUNT(*) FROM posts")
    L.append(f"- Contenus en file de publication : {n_posts}")
    L.append("- Recommandation : publier 1 Reel/jour + 3 Stories/jour ; réutiliser les vidéos de prestations comme preuve sociale.")
    L.append("")
    L.append("## 🔎 Agent SEO")
    L.append("- Recommandation : publier 1 article de blog/semaine (mots-clés : « photobooth 360 location », « livre d'or audio mariage », « animation mariage originale »).")
    L.append("")
    L.append("## 🛎️ Agent Support")
    L.append(f"- Nouveaux leads à traiter sous 24 h : {len(leads_nouveaux)}")
    L.append("")
    L.append("## 📊 Agent Data")
    L.append(f"- E-mails en attente d'envoi (SMTP) : {n_emails} · Erreurs système : {n_erreurs}")
    L.append("")
    L.append("## 🚨 Alertes nécessitant intervention humaine")
    alerts = []
    if hot: alerts.append(f"{len(hot)} lead(s) chaud(s) à contacter en priorité.")
    if devis_attente: alerts.append(f"{len(devis_attente)} devis en attente de relance.")
    if n_emails: alerts.append("SMTP non connecté : les e-mails sont en file d'attente locale.")
    if n_erreurs: alerts.append(f"{n_erreurs} erreur(s) système à vérifier.")
    L.append("\n".join("- " + a for a in alerts) if alerts else "- Rien à signaler.")
    report = "\n".join(L) + "\n"

    with open(os.path.join(REPORTS, "latest.md"), "w", encoding="utf-8") as f:
        f.write(report)
    with open(os.path.join(REPORTS, "daily-" + TODAY + ".md"), "w", encoding="utf-8") as f:
        f.write(report)
    kpis = {"date": TODAY, "ca_encaisse": ca_encaisse, "ca_devis": ca_devis, "clients": n_clients,
            "leads": n_leads, "bookings": n_bookings, "panier_moyen": panier, "leads_chauds": len(hot)}
    with open(os.path.join(REPORTS, "kpis.json"), "w", encoding="utf-8") as f:
        json.dump(kpis, f, ensure_ascii=False, indent=2)

    print(report)

if __name__ == "__main__":
    run()
