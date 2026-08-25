#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur de prospection B2B — L'Effet Waouh.
Lit prospection/cibles.csv → score → ajoute au CRM → rédige des messages
personnalisés → place les e-mails en file d'attente (outbox, non envoyés sans SMTP).
Conforme RGPD : B2B uniquement, opt-out, aucune liste achetée, pas de scraping.
Usage : python3 automation/prospect_engine.py
"""
import os, csv, sqlite3, datetime, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "waouh.db")
CSV_PATH = os.path.join(BASE, "prospection", "cibles.csv")
NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

SECTOR_KW = ["mariage", "wedding", "planner", "traiteur", "lieu", "domaine", "photographe",
             "fleuriste", "dj", "salle", "réception", "reception", "déco", "deco", "animation",
             "événementiel", "evenementiel", "château", "chateau"]

def score(source, sector, email, phone, website):
    sc = 15  # base prospection
    if email and "@" in email: sc += 15
    if phone: sc += 10
    if website: sc += 10
    if sector:
        for k in SECTOR_KW:
            if k in sector.lower(): sc += 20; break
    return min(sc, 100)

def message(contact, entreprise, secteur):
    return f"""Objet : {entreprise} — l'animation clé en main pour vos mariages

Bonjour {contact},

Je me permets de vous écrire car votre activité ({secteur}) accueille des mariages qui méritent des animations à la hauteur.

Nous sommes L'Effet Waouh, spécialiste de la location d'animations de mariage livrées clé en main : photobooth 360, livre d'or audio, néons personnalisés, cierges magiques — avec opérateur inclus.

Concrètement, pour vous :
- Un seul interlocuteur pour toutes les animations de vos événements ;
- -15 % sur tout le catalogue via notre offre Partenaire ;
- Une commission de recommandation sur chaque prestation.

Seriez-vous disponible 15 minutes la semaine prochaine pour voir si une collaboration a du sens ?

Bien cordialement,
L'Effet Waouh — contact@leffetwaouh.fr
(Pour ne plus recevoir de messages : répondre « STOP »)"""

def run():
    if not os.path.isfile(CSV_PATH):
        print("❌ prospection/cibles.csv introuvable. Créez-le (colonnes : entreprise,contact,secteur,email,telephone,site,reseaux).")
        return
    con = sqlite3.connect(DB, timeout=20)
    con.row_factory = sqlite3.Row
    added, skipped, messages = 0, 0, []
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            email = (row.get("email") or "").strip()
            entreprise = (row.get("entreprise") or "").strip()
            if entreprise.startswith("#") or (not entreprise and not email):
                continue
            exists = con.execute("SELECT id FROM leads WHERE email=? AND email!=''", (email,)).fetchone()
            if exists:
                skipped += 1; continue
            contact = (row.get("contact") or "").strip() or "Madame, Monsieur"
            secteur = (row.get("secteur") or "").strip()
            s = score("prospection", secteur, email, row.get("telephone", ""), row.get("site", ""))
            cur = con.execute("""INSERT INTO leads(company,contact,sector,email,phone,website,socials,source,status,score,first_contact,last_interaction,next_action,potential,created_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (entreprise, contact, secteur, email, row.get("telephone", ""), row.get("site", ""),
                 row.get("reseaux", ""), "prospection", "Nouveau lead", s, NOW, NOW,
                 "Envoyer premier contact (séquence 1/4)", "À qualifier", NOW))
            lead_id = cur.lastrowid
            con.execute("INSERT INTO outbox(to_email,subject,body,kind,status,created_at) VALUES(?,?,?,?,?,?)",
                        (email, f"{entreprise} — l'animation clé en main pour vos mariages",
                         message(contact, entreprise, secteur), "prospection", "queued", NOW))
            added += 1
            messages.append(f"### {entreprise} — {contact}\n\n{message(contact, entreprise, secteur)}\n")
    con.commit(); con.close()
    with open(os.path.join(BASE, "prospection", "messages_pretes.md"), "w", encoding="utf-8") as f:
        f.write("# Messages de prospection préparés\n\n" + "\n---\n\n".join(messages))
    print(f"✅ {added} nouveaux leads ajoutés au CRM · {skipped} doublons ignorés")
    print(f"📧 {added} e-mails placés en file d'attente (envoyés uniquement quand SMTP est connecté)")

if __name__ == "__main__":
    run()
