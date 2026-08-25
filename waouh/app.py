#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
L'EFFET WAOUH — Plateforme web complète (site + CRM + espace client + dashboard CEO)
Zéro dépendance externe : serveur HTTP stdlib + SQLite.
Lancement : python3 app.py  (port 8080, bind 0.0.0.0)
"""
import os, re, json, html, time, secrets, sqlite3, urllib.parse, hashlib, subprocess, datetime, smtplib
from email.mime.text import MIMEText
from email.header import Header
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "waouh.db")
VISUELS_DIR = os.path.join(os.path.dirname(BASE), "visuels")
PORT = int(os.environ.get("PORT", "8080"))
HOST = "0.0.0.0"

SITE_NAME = "L'Effet Waouh"
SITE_EMAIL = "contact@leffetwaouh.fr"

PIPELINE = ["Nouveau lead", "Qualifié", "Contacté", "Réponse", "Rendez-vous",
            "Proposition", "Négociation", "Client", "Fidélisation"]

PACKS = {
    "sortie": {"nom": "Sortie de Mairie", "prix": 199,
               "desc": "Bulles + confettis + opérateur (30 min) pour une sortie de mairie inoubliable."},
    "soiree": {"nom": "Pack Soirée Waouh", "prix": 890,
               "desc": "Photobooth 360 + livre d'or audio + néon « Mr & Mrs » + opérateur (6 h)."},
    "full":   {"nom": "Pack Full Waouh", "prix": 1490,
               "desc": "Pack Soirée + miroir magique + cierges magiques + canons confettis + opérateur (8 h)."},
}

ALACARTE = [
    ("Photobooth 360 (6 h, opérateur inclus)", 550),
    ("Miroir magique", 600),
    ("Livre d'or audio (téléphone vintage)", 99),
    ("Néon « Mr & Mrs »", 150),
    ("Lettres géantes lumineuses « LOVE »", 250),
    ("Bulles & confettis (sortie de mairie)", 150),
    ("Canons à confettis CO2", 250),
    ("Cierges magiques (sparkler exit)", 180),
    ("Piscine à balles LED", 300),
    ("Heure supplémentaire opérateur", 60),
]

NOW = lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# ---------------------------------------------------------------- base de données
def db():
    c = sqlite3.connect(DB_PATH, timeout=20)
    c.row_factory = sqlite3.Row
    try:
        c.execute("PRAGMA journal_mode=WAL")
    except Exception:
        pass
    return c

def hash_pw(pw):
    salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, 120_000)
    return salt.hex() + "$" + dk.hex()

def check_pw(pw, stored):
    try:
        salt, dk = stored.split("$")
        return hashlib.pbkdf2_hmac("sha256", pw.encode(), bytes.fromhex(salt), 120_000).hex() == dk
    except Exception:
        return False

def init_db():
    con = db()
    con.executescript("""
    CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE NOT NULL, name TEXT,
      phone TEXT, password_hash TEXT NOT NULL, role TEXT NOT NULL DEFAULT 'client',
      created_at TEXT);
    CREATE TABLE IF NOT EXISTS sessions(token TEXT PRIMARY KEY, user_id INTEGER, expires INTEGER);
    CREATE TABLE IF NOT EXISTS leads(
      id INTEGER PRIMARY KEY AUTOINCREMENT, company TEXT, contact TEXT, sector TEXT,
      email TEXT, phone TEXT, website TEXT, socials TEXT, source TEXT, status TEXT,
      score INTEGER DEFAULT 0, first_contact TEXT, last_interaction TEXT,
      next_action TEXT, notes TEXT, potential TEXT, created_at TEXT);
    CREATE TABLE IF NOT EXISTS bookings(
      id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, name TEXT, email TEXT,
      phone TEXT, event_date TEXT, venue TEXT, pack TEXT, options TEXT, total REAL,
      status TEXT, created_at TEXT);
    CREATE TABLE IF NOT EXISTS invoices(
      id INTEGER PRIMARY KEY AUTOINCREMENT, booking_id INTEGER, number TEXT,
      amount REAL, status TEXT, created_at TEXT);
    CREATE TABLE IF NOT EXISTS outbox(
      id INTEGER PRIMARY KEY AUTOINCREMENT, to_email TEXT, subject TEXT, body TEXT,
      kind TEXT, status TEXT, created_at TEXT);
    CREATE TABLE IF NOT EXISTS posts(
      id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT, title TEXT, content TEXT,
      status TEXT, scheduled_at TEXT, stats TEXT, created_at TEXT);
    CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY, value TEXT);
    CREATE TABLE IF NOT EXISTS events(
      id INTEGER PRIMARY KEY AUTOINCREMENT, kind TEXT, payload TEXT, created_at TEXT);
    """)
    cur = con.execute("SELECT id FROM users WHERE role='admin'")
    if cur.fetchone() is None:
        pw = secrets.token_urlsafe(10)
        con.execute("INSERT INTO users(email,name,password_hash,role,created_at) VALUES(?,?,?,?,?)",
                    ("admin@leffetwaouh.fr", "Admin", hash_pw(pw), "admin", NOW()))
        with open(os.path.join(BASE, ".admin_credentials"), "w") as f:
            f.write("admin@leffetwaouh.fr\n" + pw + "\n")
    con.commit(); con.close()

def log_event(kind, payload=""):
    con = db()
    con.execute("INSERT INTO events(kind,payload,created_at) VALUES(?,?,?)", (kind, payload, NOW()))
    con.commit(); con.close()

def get_setting(key, default=""):
    r = db().execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
    return r["value"] if r else default

def set_setting(key, value):
    con = db()
    con.execute("INSERT INTO settings(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, value))
    con.commit(); con.close()

# ---------------------------------------------------------------- e-mail (outbox + SMTP optionnel)
def send_email(to, subject, body, kind="info"):
    con = db()
    con.execute("INSERT INTO outbox(to_email,subject,body,kind,status,created_at) VALUES(?,?,?,?,?,?)",
                (to, subject, body, kind, "queued", NOW()))
    con.commit(); con.close()
    # Tentative d'envoi réel si SMTP configuré (sinon : file d'attente locale)
    host = get_setting("smtp_host")
    if host:
        try:
            msg = MIMEText(body, "plain", "utf-8")
            msg["Subject"] = Header(subject, "utf-8")
            msg["From"] = get_setting("smtp_from", SITE_EMAIL)
            msg["To"] = to
            with smtplib.SMTP(host, int(get_setting("smtp_port", "587")), timeout=10) as s:
                s.starttls()
                s.login(get_setting("smtp_user"), get_setting("smtp_pass"))
                s.send_message(msg)
            con = db()
            con.execute("UPDATE outbox SET status='sent' WHERE id=(SELECT MAX(id) FROM outbox)")
            con.commit(); con.close()
        except Exception as e:
            log_event("smtp_error", str(e))

# ---------------------------------------------------------------- scoring
SECTOR_KW = ["mariage", "wedding", "planner", "wedding planner", "traiteur", "lieu", "domaine",
             "photographe", "fleuriste", "dj", "salle", "réception", "reception", "déco", "deco",
             "animation", "événementiel", "evenementiel", "château", "chateau"]
def score_lead(source, sector, email, phone, website):
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

# ---------------------------------------------------------------- helpers HTML
def esc(s):
    return html.escape(str(s or ""))

def md_to_html(text):
    out, in_list = [], False
    for line in text.split("\n"):
        s = line.rstrip()
        if s.startswith("### "): out.append("<h3>" + esc(s[4:]) + "</h3>")
        elif s.startswith("## "): out.append("<h2>" + esc(s[3:]) + "</h2>")
        elif s.startswith("# "): out.append("<h2>" + esc(s[2:]) + "</h2>")
        elif s.startswith("- "):
            if not in_list: out.append("<ul>"); in_list = True
            out.append("<li>" + esc(s[2:]) + "</li>")
        elif s == "":
            if in_list: out.append("</ul>"); in_list = False
        else:
            if in_list: out.append("</ul>"); in_list = False
            out.append("<p>" + esc(s) + "</p>")
    if in_list: out.append("</ul>")
    return "\n".join(out)

CSS = """
:root{--cream:#FAF6F0;--ink:#2F2A25;--terra:#B0764A;--terra2:#C67B4F;--gold:#D9A441;--gold2:#E8B26A;--sage:#7A8B6F;--line:#E7DED2;--soft:#F3EAE0}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6}
a{color:inherit;text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 22px}
h1,h2,h3,h4,.serif{font-family:Georgia,'Times New Roman',serif;line-height:1.15}
/* topbar */
.topbar{position:sticky;top:0;z-index:100;background:rgba(250,246,240,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.topbar .in{max-width:1080px;margin:0 auto;padding:12px 22px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.brand{font-family:Georgia,serif;font-weight:700;font-size:20px;color:var(--ink)}
.brand .spark{color:var(--gold)}
.brand small{display:block;font-family:-apple-system,sans-serif;font-size:9.5px;letter-spacing:2.2px;color:var(--terra);font-weight:700;text-transform:uppercase}
.nav{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.nav a{font-size:14px;font-weight:500;color:#5a4f42}
.nav a:hover{color:var(--terra)}
.nav a.on{color:var(--terra);font-weight:700}
/* boutons */
.btn{display:inline-block;background:var(--terra);color:#fff;padding:12px 22px;border-radius:999px;font-weight:700;font-size:15px;border:1px solid var(--terra);cursor:pointer;transition:.15s}
.btn:hover{background:var(--terra2);border-color:var(--terra2);transform:translateY(-1px)}
.btn.gold{background:var(--gold);border-color:var(--gold);color:#fff}
.btn.gold:hover{background:var(--gold2);border-color:var(--gold2)}
.btn.ghost{background:transparent;color:var(--terra);border:1px solid var(--terra)}
.btn.ghost:hover{background:var(--soft)}
.btn.small{padding:8px 16px;font-size:13.5px}
.btn.danger{background:#9c3b2e;border-color:#9c3b2e}
/* hero de page interne */
.pagehero{background:linear-gradient(150deg,#2F2A25 0%,#4a3a2c 60%,#6b4a2f 100%);color:#fff;padding:60px 0 52px;text-align:center}
.pagehero .kick{display:inline-block;color:#E8B26A;font-size:11px;letter-spacing:2.5px;text-transform:uppercase;font-weight:700;margin-bottom:10px}
.pagehero h1{font-size:clamp(30px,4.5vw,46px);margin-bottom:10px}
.pagehero p{color:#efe3d2;max-width:620px;margin:0 auto;font-size:16px}
/* sections */
section{padding:60px 0}
section h2{font-size:clamp(26px,3.5vw,36px);margin-bottom:10px}
section h2 em{color:var(--terra);font-style:italic}
section .sub{color:#6b5f52;max-width:660px;margin-bottom:28px;font-size:16px}
.center{text-align:center}
.center .sub{margin-left:auto;margin-right:auto}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px;box-shadow:0 6px 24px rgba(47,42,37,.05)}
.card h3{margin-bottom:8px;font-size:20px}
.card p{color:#5c5246;font-size:14.5px}
.card .ico{font-size:32px;margin-bottom:10px}
/* packs */
.pack{background:#fff;border:1px solid var(--line);border-radius:20px;padding:26px;border-top:4px solid var(--gold);box-shadow:0 8px 28px rgba(47,42,37,.07)}
.pack .price{font-family:Georgia,serif;font-size:34px;color:var(--terra);margin:8px 0}
.pack .price small{font-size:14px;font-family:system-ui;color:#6b5f52}
.pack ul{list-style:none;margin:0 0 16px}
.pack li{padding:4px 0;font-size:14px;color:#4a4035}
.pack li::before{content:"✓ ";color:var(--sage);font-weight:800}
/* badge & pill */
.badge{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;color:var(--terra);background:var(--soft);padding:4px 10px;border-radius:999px}
.pill{display:inline-block;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:600;background:var(--soft);color:var(--terra)}
.pill.ok,.pill.paid{background:#EAF3EA;color:#2E7D43}
.pill.wait{background:#FDF1DD;color:#9A6A1F}
.pill.new{background:#EAEAF3;color:#3d3d7a}
/* tables */
.table{width:100%;border-collapse:collapse;background:#fff;border-radius:14px;overflow:hidden;border:1px solid var(--line)}
.table th,.table td{padding:11px 13px;border-bottom:1px solid var(--line);text-align:left;font-size:14px}
.table th{background:#F6EFE6;font-size:11.5px;text-transform:uppercase;letter-spacing:.5px;color:#6b5f52}
/* stats */
.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
.stat{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px}
.stat .n{font-family:Georgia,serif;font-size:30px;color:var(--terra)}
.stat .l{font-size:12.5px;color:#6b5f52}
/* forms */
input,select,textarea{width:100%;padding:12px 13px;border:1px solid var(--line);border-radius:11px;font-size:14.5px;background:#fff;margin-bottom:13px;font-family:inherit}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--terra)}
label{font-size:13px;font-weight:600;color:#5a4f42}
.formcard{background:#fff;border:1px solid var(--line);border-radius:20px;padding:30px;box-shadow:0 10px 34px rgba(47,42,37,.07)}
/* alert */
.alert{border-radius:12px;padding:14px 16px;margin-bottom:16px;font-size:14px}
.alert.ok{background:#EAF3EA;color:#2E7D43;border:1px solid #CBE3CE}
.alert.warn{background:#FDF1DD;color:#9A6A1F;border:1px solid #F1DEB8}
.alert.err{background:#F9E6E3;color:#9c3b2e;border:1px solid #EFC9C3}
/* carrousel */
.serv{background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:0 8px 28px rgba(47,42,37,.07);display:flex;flex-direction:column}
.carousel{position:relative;aspect-ratio:4/3;overflow:hidden;background:#1d150e}
.carousel .track{display:flex;height:100%;transition:transform .45s ease}
.carousel .track img{width:100%;height:100%;object-fit:cover;flex:0 0 100%;display:block}
.carousel .navbtn{position:absolute;top:50%;transform:translateY(-50%);width:36px;height:36px;border-radius:50%;background:rgba(24,15,10,.55);border:1px solid rgba(255,255,255,.4);color:#fff;font-size:17px;cursor:pointer;z-index:3;line-height:1;display:flex;align-items:center;justify-content:center}
.carousel .navbtn:hover{background:rgba(24,15,10,.8)}
.carousel .prev{left:10px}.carousel .next{right:10px}
.carousel .dots{position:absolute;bottom:10px;left:0;right:0;display:flex;gap:6px;justify-content:center;z-index:3}
.carousel .dots span{width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,.45);cursor:pointer}
.carousel .dots span.on{background:var(--gold)}
.carousel .counter{position:absolute;top:10px;right:12px;z-index:3;background:rgba(24,15,10,.6);color:#fff;font-size:11px;font-weight:700;padding:3px 9px;border-radius:999px}
.serv .sinfo{padding:20px 22px;flex:1;display:flex;flex-direction:column}
.serv .sinfo h3{font-size:20px;margin-bottom:6px}
.serv .sinfo p{color:#5c5246;font-size:14px;flex:1}
.serv .sinfo .prix{font-family:Georgia,serif;font-size:22px;color:var(--terra);margin-top:10px}
.serv .sinfo .prix small{font-size:13px;font-family:system-ui;color:#6b5f52}
.serv .sinfo .cta{margin-top:12px}
/* FAQ accordion */
.faq{max-width:780px;margin:0 auto}
.faq .q{background:#fff;border:1px solid var(--line);border-radius:14px;margin-bottom:10px;overflow:hidden}
.faq .q button{width:100%;text-align:left;background:none;border:none;padding:17px 20px;font-size:15.5px;font-weight:600;color:var(--ink);cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:inherit}
.faq .q button::after{content:"+";font-size:22px;color:var(--terra);font-weight:400}
.faq .q.open button::after{content:"−"}
.faq .a{display:none;padding:0 20px 18px;color:#5c5246;font-size:14.5px}
.faq .q.open .a{display:block}
/* CTA final */
.final{background:linear-gradient(150deg,#2F2A25 0%,#4a3a2c 55%,#6b4a2f 100%);color:#fff;text-align:center;padding:64px 22px}
.final h2{font-size:clamp(28px,4vw,44px);margin-bottom:12px}
.final h2 em{color:var(--gold2)}
.final p{color:#e6d9c6;max-width:560px;margin:0 auto 24px;font-size:16.5px}
.final .cta{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
/* footer */
footer{background:#2F2A25;color:#cdc2b2;padding:44px 0;font-size:14px}
footer a{color:#E8B26A}
footer .cols{display:flex;gap:46px;flex-wrap:wrap}
footer b{color:#fff}
footer .note{margin-top:26px;font-size:12px;color:#8d8172;border-top:1px solid #3a332c;padding-top:18px}
/* article */
.article{max-width:760px;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:20px;padding:38px}
.article h2{margin:22px 0 10px}
.article p,.article li{color:#4a4035;font-size:15.5px}
.article ul{padding-left:20px;margin:10px 0}
@media(max-width:820px){.grid3,.grid2,.kpi{grid-template-columns:1fr}}
"""


SUBTITLES = {
    "services": "Photobooth 360, livre d'or audio, néons, cierges magiques… tout se loue à la journée, livré et installé.",
    "tarifs": "Des formules clé en main, opérateur inclus, sans engagement. Devis gratuit sous 24 h.",
    "blog": "Conseils, tendances et inspirations pour un mariage waouh.",
    "faq": "Tout ce qu'il faut savoir avant de réserver. Une autre question ? Écrivez-nous.",
    "contact": "Une question, un projet, un partenariat ? Réponse sous 24 h ouvrées.",
    "reservation": "Décrivez votre projet en 2 minutes : devis immédiat, zéro engagement.",
}

def page(user, title, body, active=""):
    hero_title = title.split(" — ")[0]
    nav_links = [
        ("/", "Accueil", "home"), ("/services", "Services", "services"),
        ("/tarifs", "Tarifs", "tarifs"), ("/blog", "Blog", "blog"),
        ("/faq", "FAQ", "faq"), ("/contact", "Contact", "contact"),
    ]
    links = ""
    for href, label, key in nav_links:
        cls = ' class="on"' if active == key else ""
        links += f'<a href="{href}"{cls}>{label}</a>'
    if user:
        if user["role"] == "admin":
            links += '<a href="/admin">Admin</a>'
        links += '<a href="/espace">Espace client</a><a href="/logout">Déconnexion</a>'
    else:
        links += '<a href="/login">Connexion</a><a class="btn small" href="/reservation">Réserver</a>'
    sub = SUBTITLES.get(active, "Animations & gadgets de mariage livrés clé en main.")
    final_cta = ""
    if active in ("services", "tarifs", "blog", "faq", "contact"):
        final_cta = """
<div class="final">
  <h2>Votre date est <em>précieuse</em>. Réservez-la.</h2>
  <p>Devis gratuit sous 24 h, zéro engagement. Les samedis partent vite.</p>
  <div class="cta"><a class="btn gold" href="/reservation">Réserver mon animation</a><a class="btn ghost" style="color:#fff;border-color:#fff" href="/contact">Poser une question</a></div>
</div>"""
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} · {SITE_NAME}</title>
<meta name="description" content="Location d'animations et de gadgets pour mariages : photobooth 360, livre d'or audio, néons, cierges magiques. Livré et installé clé en main.">
<style>{CSS}</style></head><body>
<div class="topbar"><div class="in">
  <a href="/" class="brand"><span class="spark">✦</span> L'Effet Waouh<small>Animations &amp; gadgets de mariage</small></a>
  <div class="nav">{links}</div>
</div></div>
<div class="pagehero"><div class="wrap">
  <span class="kick">✦ L'Effet Waouh · Animations de mariage</span>
  <h1>{esc(hero_title)}</h1>
  <p>{esc(sub)}</p>
</div></div>
{body}
{final_cta}
<footer><div class="wrap">
  <div class="cols">
    <div><b>L'Effet Waouh</b><br>Animations &amp; gadgets de mariage<br>Paris &amp; Île-de-France — livraison France entière</div>
    <div><b>Navigation</b><br><a href="/services">Services</a> · <a href="/tarifs">Tarifs</a> · <a href="/blog">Blog</a> · <a href="/faq">FAQ</a> · <a href="/contact">Contact</a></div>
    <div><b>Légal</b><br><a href="/mentions-legales">Mentions légales</a> · <a href="/cgv">CGV</a> · <a href="/confidentialite">Confidentialité</a></div>
    <div><b>Contact</b><br><a href="mailto:contact@leffetwaouh.fr">contact@leffetwaouh.fr</a><br>Réponse sous 24 h ouvrées</div>
  </div>
  <div class="note">© 2026 L'Effet Waouh — « On installe, on anime, vous profitez. »</div>
</div></footer>
<script>
document.querySelectorAll('.faq .q button').forEach(function(b){{b.addEventListener('click',function(){{b.parentElement.classList.toggle('open');}});}});
document.querySelectorAll('.carousel').forEach(function(c){{
  var track=c.querySelector('.track'), slides=track.children, n=slides.length, i=0, t=null;
  var dots=c.querySelector('.dots'), counter=c.querySelector('.counter');
  for(var k=0;k<n;k++){{var d=document.createElement('span'); if(k===0)d.className='on'; (function(k){{d.onclick=function(){{go(k)}}}})(k); dots.appendChild(d);}}
  function go(x){{i=((x%n)+n)%n; track.style.transform='translateX(-'+(i*100)+'%)';
    dots.querySelectorAll('span').forEach(function(dd,j){{dd.classList.toggle('on',j===i)}});
    if(counter) counter.textContent=(i+1)+'/'+n;}}
  c.querySelector('.next').onclick=function(){{go(i+1)}};
  c.querySelector('.prev').onclick=function(){{go(i-1)}};
  function play(){{clearInterval(t); t=setInterval(function(){{go(i+1)}},3600)}};
  c.addEventListener('mouseenter',function(){{clearInterval(t)}});
  c.addEventListener('mouseleave',play);
  play();
}});
try{{var obs=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.style.opacity=1;e.target.style.transform='none';obs.unobserve(e.target);}}}});}},{{threshold:.08}});
document.querySelectorAll('section,.formcard,.card,.serv').forEach(function(s){{s.style.opacity=0;s.style.transform='translateY(16px)';s.style.transition='opacity .6s ease, transform .6s ease';obs.observe(s);}});}}catch(e){{}}
</script>
</body></html>"""

def redirect(self, path):
    self.send_response(302); self.send_header("Location", path); self.end_headers()

def serve_bytes(self, b, ctype):
    self.send_response(200); self.send_header("Content-Type", ctype)
    self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

# ---------------------------------------------------------------- handler
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def current_user(self):
        cookie = self.headers.get("Cookie", "")
        m = re.search(r"session=([^;]+)", cookie)
        if not m: return None
        r = db().execute("SELECT u.* FROM sessions s JOIN users u ON u.id=s.user_id WHERE s.token=? AND s.expires>?",
                         (m.group(1), int(time.time()))).fetchone()
        return r

    def session_token(self):
        cookie = self.headers.get("Cookie", "")
        m = re.search(r"session=([^;]+)", cookie)
        return m.group(1) if m else ""

    def require(self, user, role=None, login_path="/login"):
        if not user:
            redirect(self, login_path); return None
        if role and user["role"] != role:
            self.send_error(403); return None
        return user

    def do_GET(self):
        try: self.route("GET")
        except Exception as e:
            log_event("error", f"{self.path} -> {e}")
            self.send_response(500); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
            self.wfile.write(b"<h1>Erreur serveur</h1><p>Consultez les logs.</p>")

    def do_POST(self):
        try: self.route("POST")
        except Exception as e:
            log_event("error", f"{self.path} -> {e}")
            self.send_response(500); self.end_headers()

    def form(self):
        ln = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(ln).decode("utf-8", "replace") if ln else ""
        return {k: v[0] for k, v in urllib.parse.parse_qs(raw).items()}

    # ---------------------------------------------------------------- routage
    def route(self, method):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        user = self.current_user()
        if method == "GET":
            if path.startswith("/img/"):
                return self.serve_img(path[5:])
            if path == "/": return self.home(user)
            if path == "/services": return self.services(user)
            if path == "/tarifs": return self.tarifs(user)
            if path == "/faq": return self.faq(user)
            if path == "/blog": return self.blog(user)
            if path.startswith("/blog/"): return self.blog_post(user, path[6:])
            if path == "/contact": return self.contact(user)
            if path == "/reservation": return self.reservation(user)
            if path == "/login": return self.login(user)
            if path == "/register": return self.register(user)
            if path == "/logout": return self.logout()
            if path == "/espace": return self.espace(user)
            if path == "/mentions-legales": return self.legal(user, "legal/mentions-legales.md", "Mentions légales")
            if path == "/cgv": return self.legal(user, "legal/cgv.md", "CGV")
            if path == "/confidentialite": return self.legal(user, "legal/confidentialite.md", "Politique de confidentialité")
            if path == "/admin": return self.admin(user)
            if path == "/controle": return self.controle(user)
            if path == "/admin/leads": return self.admin_leads(user)
            if path.startswith("/admin/leads/"): return self.admin_lead(user, path.split("/")[-1])
            if path == "/admin/bookings": return self.admin_bookings(user)
            if path == "/admin/outbox": return self.admin_outbox(user)
            if path == "/admin/agents": return self.admin_agents(user)
            if path == "/admin/settings": return self.admin_settings(user)
            return self.send_error(404)
        if method == "POST":
            if path == "/reservation": return self.reservation_post(user)
            if path == "/login": return self.login_post()
            if path == "/register": return self.register_post()
            if path == "/espace/profil": return self.profil_post(user)
            if path == "/contact": return self.contact_post()
            if path.startswith("/admin/leads/"): return self.admin_lead_post(user, path.split("/")[-1])
            if path.startswith("/admin/bookings/"): return self.admin_booking_post(user, path.split("/")[-1])
            if path == "/admin/settings": return self.admin_settings_post(user)
            if path == "/admin/agents/run": return self.admin_agents_run(user)
            return self.send_error(404)

    # ---------------------------------------------------------------- pages publiques
    def home(self, user):
        p = os.path.join(BASE, "site", "landing.html")
        if os.path.isfile(p):
            b = open(p, "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers(); self.wfile.write(b)
            return
        body = f"""
<div class="hero"><div class="wrap">
  <span class="badge" style="background:rgba(255,255,255,.12);color:#E8B26A">Photobooth 360 · Livre d'or audio · Néons · Cierges magiques</span>
  <h1 style="margin-top:16px">Le matériel d'animation qui crée <em>l'effet Waouh</em> à votre mariage</h1>
  <p class="lead">Vous rêvez d'un mariage dont tout le monde parle, plein de moments « instagrammables » ? On loue, on livre, on installe, on anime — vous, vous profitez.</p>
  <div class="cta"><a class="btn gold" href="/reservation">Réserver mon animation</a><a class="btn ghost" style="color:#fff;border-color:#fff" href="/tarifs">Voir les packs</a></div>
</div></div>
<section><div class="wrap">
  <h2>Le problème</h2>
  <p class="sub">Un mariage générique : des invités qui s'ennuient entre deux plats, peu de souvenirs à partager, des animations coûteuses à acheter pour une seule journée.</p>
  <div class="grid3">
    <div class="card"><h3>Notre solution</h3><p>Un parc de matériel tendance, toujours aligné sur TikTok/Instagram, loué à la journée avec livraison, montage et opérateur.</p></div>
    <div class="card"><h3>Les bénéfices</h3><p>Des invités émerveillés, des centaines de photos/vidéos partagées, et un budget maîtrisé : on loue, on n'achète pas.</p></div>
    <div class="card"><h3>Pourquoi nous</h3><p>Spécialistes des animations « effet waouh », opérateur inclus, matériel testé, garantie : si l'effet n'est pas là, on s'engage.</p></div>
  </div>
</div></section>
<section style="background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap">
  <h2>Comment ça marche</h2>
  <p class="sub">3 étapes, 2 minutes de votre temps.</p>
  <div class="grid3">
    <div class="card"><h3>1. Vous réservez</h3><p>Choisissez votre pack ou vos gadgets à la carte, indiquez la date et le lieu.</p></div>
    <div class="card"><h3>2. On prépare</h3><p>Devis immédiat, confirmation, matériel réservé et testé avant le jour J.</p></div>
    <div class="card"><h3>3. On installe &amp; on anime</h3><p>Livraison, montage, opérateur présent, démontage et restitution. Vous profitez.</p></div>
  </div>
</div></section>
<section><div class="wrap">
  <h2>Des chiffres qui parlent</h2>
  <div class="grid3">
    <div class="card"><h3 style="color:var(--terra)">+800 €</h3><p>de photos et vidéos partagées en moyenne par mariage grâce à nos animations.</p></div>
    <div class="card"><h3 style="color:var(--terra)">×6</h3><p>c'est le retour sur investissement typique d'une location : le matériel est amorti en 5-6 prestations.</p></div>
    <div class="card"><h3 style="color:var(--terra)">100 %</h3><p>de nos packs incluent un opérateur : aucun stress logistique pour vous.</p></div>
  </div>
  <div style="margin-top:26px"><a class="btn" href="/reservation">Je veux cet effet waouh →</a></div>
</div></section>
"""
        self.ok(page(user, "Animations de mariage — L'Effet Waouh", body, "home"))

    def services(self, user):
        servs = [
            ("Photobooth 360", "Vidéos slow-motion 360° partagées en QR code. L'effet foule garanti, l'animation star des Reels.", 550, "6 h, opérateur inclus",
             ["02-photobooth-360.jpg", "01-hero.jpg", "09-premiere-danse.jpg", "12-installation.jpg"]),
            ("Miroir magique", "Miroir à selfie tactile : impressions, animations, messages. Le premium du photobooth.", 600, "la soirée",
             ["07-miroir-magique.jpg", "07-miroir-magique-v1.jpg", "07-miroir-magique-v2.jpg", "07-miroir-magique-v3.jpg"]),
            ("Livre d'or audio", "Téléphone vintage : vos invités laissent un message vocal. Le gadget viral 2026.", 99, "le week-end",
             ["03-livre-or-audio.jpg", "10-vin-honneur.jpg", "03-livre-or-audio-v1.jpg", "10-vin-honneur-v1.jpg"]),
            ("Néon « Mr & Mrs »", "Enseigne LED personnalisée : le fond de photo de toutes vos soirées.", 150, "le week-end",
             ["04-neon.jpg", "01-hero.jpg", "10-vin-honneur.jpg", "04-neon-v1.jpg"]),
            ("Lettres géantes « LOVE »", "Décor lumineux iconique, le coin photo qui attire tout le monde.", 250, "le week-end",
             ["04-neon-v2.jpg", "01-hero-v1.jpg", "10-vin-honneur-v2.jpg", "04-neon-v3.jpg"]),
            ("Cierges magiques", "Le tunnel d'étincelles de fin de soirée. La photo iconique du mariage.", 180, "le soir (extérieur)",
             ["05-cierges-magiques.jpg", "05-cierges-magiques-v1.jpg", "05-cierges-magiques-v2.jpg", "05-cierges-magiques-v3.jpg"]),
            ("Bulles & confettis", "La sortie de mairie effet cinéma : nuage de bulles et pluie de confettis.", 150, "la sortie de mairie",
             ["06-bulles-confettis.jpg", "06-bulles-confettis-v1.jpg", "06-bulles-confettis-v2.jpg", "06-bulles-confettis-v3.jpg"]),
            ("Canons à confettis CO2", "Explosion de couleurs synchronisée pour la première danse.", 250, "la première danse",
             ["09-premiere-danse.jpg", "09-premiere-danse-v1.jpg", "09-premiere-danse-v2.jpg", "09-premiere-danse-v3.jpg"]),
            ("Piscine à balles LED", "Le coin lounge lumineux qui fait le tour des Reels. Carton garanti.", 300, "la soirée",
             ["08-piscine-balles.jpg", "08-piscine-balles-v1.jpg", "08-piscine-balles-v2.jpg", "08-piscine-balles-v3.jpg"]),
        ]
        cards = ""
        for name, desc, prix, unit, imgs in servs:
            slides = "".join(f'<img src="/img/{esc(f)}" alt="{esc(name)}" loading="lazy">' for f in imgs)
            cards += f'''<div class="serv">
<div class="carousel"><div class="track">{slides}</div>
<span class="counter">1/{len(imgs)}</span>
<button class="navbtn prev">‹</button><button class="navbtn next">›</button>
<div class="dots"></div>
</div>
<div class="sinfo"><h3>{esc(name)}</h3><p>{esc(desc)}</p>
<div class="prix">{prix} € <small>/ {esc(unit)}</small></div>
<a class="btn small" href="/reservation">Réserver cette animation</a>
</div></div>'''
        body = f"""<section><div class="wrap">
<div class="center"><h2>Nos animations &amp; <em>gadgets</em></h2>
<p class="sub">Tout se loue à la journée, livré et installé (opérateur inclus dans les packs). Faites défiler les photos de chaque animation.</p></div>
<div class="grid3">{cards}</div>
<p style="text-align:center;color:#9b8f80;font-size:12.5px;margin-top:22px">Photos d'illustration (visuels de démonstration) — remplacées par nos photos réelles de prestations.</p>
<div style="margin-top:26px;text-align:center"><a class="btn gold" href="/reservation">Demander un devis</a></div>
</div></section>"""
        self.ok(page(user, "Services — L'Effet Waouh", body, "services"))

    def tarifs(self, user):
        packs = ""
        for key in ["sortie", "soiree", "full"]:
            p = PACKS[key]
            hot = ' style="border-top-color:var(--gold)"' if key == "soiree" else ""
            flag = ' <span class="badge" style="background:var(--gold);color:#fff">Le + choisi</span>' if key == "soiree" else ""
            packs += f'<div class="pack"{hot}><h3>{esc(p["nom"])}{flag}</h3><div class="price">{p["prix"]} € <small>tout compris</small></div><p>{esc(p["desc"])}</p><a class="btn small" href="/reservation?pack={key}" style="margin-top:12px">Réserver</a></div>'
        rows = "".join(f'<tr><td>{esc(n)}</td><td style="text-align:right"><strong>{p} €</strong></td></tr>' for n, p in ALACARTE)
        body = f"""<section><div class="wrap">
<div class="center"><h2>Nos <em>packs</em></h2><p class="sub">Des formules clé en main, opérateur inclus.</p></div>
<div class="grid3">{packs}</div>
<h2 style="margin-top:48px">À la carte</h2>
<p class="sub">Chaque animation se loue seule, à la journée.</p>
<table class="table">{rows}</table>
<h2 style="margin-top:48px">Professionnels</h2>
<div class="card"><div class="ico">🤝</div><h3>Abonnement « Waouh Partenaire » — 29 €/mois</h3>
<p>Wedding planners, lieux de réception, traiteurs : -15 % sur tout le catalogue, créneaux prioritaires en haute saison, et commission de recommandation.</p>
<a class="btn small" href="/contact" style="margin-top:12px">Devenir partenaire</a></div>
</div></section>"""
        self.ok(page(user, "Tarifs — L'Effet Waouh", body, "tarifs"))

    def faq(self, user):
        q = [
            ("Comment réserver ?", "Remplissez le formulaire de réservation : vous recevez un devis immédiat et un lien de confirmation. Un acompte de 30 % sécurise la date."),
            ("Livrez-vous partout en France ?", "Oui. Les petits objets (livre d'or audio, néons) s'expédient en point relais. Les gros équipements (photobooth, miroir) se livrent en Île-de-France ; partout ailleurs sur devis."),
            ("Un opérateur est-il inclus ?", "Oui dans tous les packs. À la carte, l'opérateur est en option (60 €/heure)."),
            ("Que se passe-t-il en cas de casse ?", "Une caution est demandée (montant selon le matériel) et restituée après vérification. Le matériel est assuré ; les consommables (confettis, cierges, papier) sont facturés séparément."),
            ("Peut-on personnaliser le néon ?", "Oui : les néons aux prénoms des mariés sont proposés en option à l'achat (vous le gardez en souvenir)."),
            ("Et s'il pleut le jour J ?", "Toutes nos animations peuvent être repliées en intérieur (sauf cierges magiques, réservés à l'extérieur). On prévoit toujours un plan B."),
        ]
        items = "".join(f'<div class="q"><button>{esc(a)}</button><div class="a">{esc(b)}</div></div>' for a, b in q)
        body = f'<section><div class="wrap"><div class="center"><h2>Questions <em>fréquentes</em></h2><p class="sub">Tout ce qu\'il faut savoir avant de réserver.</p></div><div class="faq">{items}</div></div></section>'
        self.ok(page(user, "FAQ — L'Effet Waouh", body, "faq"))

    def contact(self, user):
        body = """<section><div class="wrap">
<div class="grid2" style="align-items:start">
<div>
<div class="card"><div class="ico">✉️</div><h3>Par e-mail</h3><p>contact@leffetwaouh.fr<br>Réponse sous 24 h ouvrées.</p></div>
<div class="card" style="margin-top:18px"><div class="ico">💬</div><h3>Pour les pros</h3><p>Wedding planners, lieux, traiteurs : découvrez l'offre Partenaire (-15 %, commission).</p></div>
<div class="card" style="margin-top:18px"><div class="ico">📍</div><h3>Zone d'intervention</h3><p>Paris &amp; Île-de-France — livraison France entière pour les petits objets.</p></div>
</div>
<div class="formcard">
<h2 style="font-size:26px;margin-bottom:6px">Écrivez-nous</h2>
<p class="sub" style="font-size:14px">Une question, un projet, un partenariat.</p>
<form method="post" action="/contact">
<label>Nom</label><input name="name" required>
<label>E-mail</label><input type="email" name="email" required>
<label>Message</label><textarea name="message" rows="5" required></textarea>
<button class="btn gold" type="submit">Envoyer</button>
</form></div>
</div>
</div></section>"""
        self.ok(page(user, "Contact — L'Effet Waouh", body, "contact"))

    def contact_post(self):
        f = self.form()
        send_email(SITE_EMAIL, f"Message de {f.get('name')} ({f.get('email')})", f.get("message", ""), "contact")
        log_event("contact", f.get("email", ""))
        self.alert_page("Merci ! Votre message a bien été envoyé. Nous revenons vers vous sous 24 h.", "ok", "/contact")

    def blog(self, user):
        entries = []
        bdir = os.path.join(BASE, "content", "blog")
        if os.path.isdir(bdir):
            for fn in sorted(os.listdir(bdir)):
                if fn.endswith(".md"):
                    t = open(os.path.join(bdir, fn), encoding="utf-8").read()
                    title = t.split("\n", 1)[0].lstrip("# ").strip()
                    first = [l for l in t.split("\n") if l and not l.startswith("#")][:1]
                    entries.append((fn[:-3], title, first[0] if first else ""))
        cards = "".join(f'<div class="card"><h3><a href="/blog/{esc(s)}">{esc(t)}</a></h3><p>{esc(d)}</p></div>' for s, t, d in entries)
        body = f'<section><div class="wrap"><h2>Le blog</h2><p class="sub">Conseils, tendances et inspirations pour un mariage waouh.</p><div class="grid3">{cards}</div></div></section>'
        self.ok(page(user, "Blog — L'Effet Waouh", body, "blog"))

    def blog_post(self, user, slug):
        p = os.path.join(BASE, "content", "blog", slug + ".md")
        if not os.path.isfile(p): return self.send_error(404)
        t = open(p, encoding="utf-8").read()
        title = t.split("\n", 1)[0].lstrip("# ").strip()
        body = f'<section><div class="wrap"><div class="article">{md_to_html(t)}<div style="margin-top:26px"><a class="btn" href="/reservation">Réserver mon animation</a></div></div></div></section>'
        self.ok(page(user, title + " — L'Effet Waouh", body, "blog"))

    def legal(self, user, path, title):
        p = os.path.join(BASE, path)
        txt = open(p, encoding="utf-8").read() if os.path.isfile(p) else "Document en préparation."
        body = f'<section><div class="wrap"><div class="article">{md_to_html(txt)}</div></div></section>'
        self.ok(page(user, title + " — L'Effet Waouh", body))

    def reservation(self, user):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        presel = q.get("pack", [""])[0]
        opts = "".join(f'<label style="display:flex;align-items:center;gap:8px;font-weight:500;margin-bottom:8px"><input type="checkbox" name="opt" value="{esc(n)}" style="width:auto;margin:0"> {esc(n)} ({p} €)</label>' for n, p in ALACARTE[:9])
        packopts = "".join(f'<option value="{k}" {"selected" if k==presel else ""}>{esc(PACKS[k]["nom"])} — {PACKS[k]["prix"]} €</option>' for k in PACKS)
        body = f"""<section><div class="wrap" style="max-width:680px">
<div class="formcard">
<h2 style="font-size:28px;margin-bottom:6px">Réserver mon animation</h2>
<p class="sub" style="font-size:14px">Devis immédiat, sans engagement. Réponse sous 24 h.</p>
<form method="post" action="/reservation">
<label>Nom complet</label><input name="name" required>
<div class="grid2" style="gap:14px"><div><label>E-mail</label><input type="email" name="email" required></div><div><label>Téléphone</label><input name="phone"></div></div>
<div class="grid2" style="gap:14px"><div><label>Date de l'événement</label><input type="date" name="date" required></div><div><label>Lieu (ville / salle)</label><input name="venue"></div></div>
<label>Pack souhaité</label><select name="pack">{packopts}<option value="carte">À la carte</option></select>
<label>Options supplémentaires</label><div style="background:#FBF7F1;border:1px solid var(--line);border-radius:12px;padding:14px">{opts}</div>
<label>Message (optionnel)</label><textarea name="message" rows="3"></textarea>
<button class="btn gold" type="submit" style="width:100%">Recevoir mon devis</button>
</form></div>
</div></section>"""
        self.ok(page(user, "Réserver — L'Effet Waouh", body, "reservation"))

    def reservation_post(self, user):
        f = self.form()
        email = f.get("email", "")
        pack_key = f.get("pack", "carte")
        opts = f.get("opt", []) if hasattr(f, "getlist") else [f.get("opt")] if f.get("opt") else []
        total = PACKS[pack_key]["prix"] if pack_key in PACKS else 0
        opt_names = opts if isinstance(opts, list) else [opts]
        for o in opt_names:
            for n, p in ALACARTE:
                if n == o: total += p
        con = db()
        cur = con.execute("INSERT INTO leads(company,contact,sector,email,phone,source,status,score,first_contact,last_interaction,next_action,potential,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("", f.get("name", ""), "", email, f.get("phone", ""), "site", "Nouveau lead",
             score_lead("site", "", email, f.get("phone", ""), ""), NOW(), NOW(),
             "Envoyer devis sous 24h", "Moyen", NOW()))
        lead_id = cur.lastrowid
        cur.execute("INSERT INTO bookings(user_id,name,email,phone,event_date,venue,pack,options,total,status,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (user["id"] if user else None, f.get("name", ""), email, f.get("phone", ""), f.get("date", ""),
             f.get("venue", ""), PACKS.get(pack_key, {}).get("nom", "À la carte"), ", ".join(opt_names), total, "devis", NOW()))
        booking_id = cur.lastrowid
        num = "W" + datetime.datetime.now().strftime("%Y%m") + f"-{booking_id:04d}"
        cur.execute("INSERT INTO invoices(booking_id,number,amount,status,created_at) VALUES(?,?,?,?,?)", (booking_id, num, total, "brouillon", NOW()))
        con.commit(); con.close()
        send_email(email, f"Votre devis {num} — L'Effet Waouh",
                   f"Bonjour {f.get('name','')},\n\nMerci pour votre demande ! Votre devis {num} ({total} €) est en préparation.\nNotre équipe vous répond sous 24 h pour confirmer la disponibilité.\n\nÀ très vite,\nL'Effet Waouh", "devis")
        send_email(SITE_EMAIL, f"Nouvelle demande de devis {num} ({total} €)", f"Lead #{lead_id} — {f.get('name')} ({email}) — {f.get('date')} — {PACKS.get(pack_key,{}).get('nom','À la carte')}", "lead_alert")
        log_event("lead_created", f"lead#{lead_id}")
        self.alert_page(f"✅ Demande enregistrée ! Votre devis <strong>{esc(num)}</strong> ({total} €) vous a été envoyé par e-mail. Réponse sous 24 h.", "ok", "/espace")

    # ---------------------------------------------------------------- auth
    def login(self, user):
        body = """<section><div class="wrap" style="max-width:460px">
<div class="formcard">
<h2 style="font-size:28px;margin-bottom:6px">Connexion</h2>
<p class="sub" style="font-size:14px">Accédez à votre espace client.</p>
<form method="post" action="/login">
<label>E-mail</label><input type="email" name="email" required>
<label>Mot de passe</label><input type="password" name="password" required>
<button class="btn" type="submit" style="width:100%">Se connecter</button>
</form><p style="margin-top:14px;font-size:14px">Pas encore de compte ? <a href="/register" style="color:var(--terra);font-weight:600">Créer un compte</a></p>
</div></div></section>"""
        self.ok(page(user, "Connexion — L'Effet Waouh", body))

    def login_post(self):
        f = self.form()
        r = db().execute("SELECT * FROM users WHERE email=?", (f.get("email", "").strip().lower(),)).fetchone()
        if r and check_pw(f.get("password", ""), r["password_hash"]):
            token = secrets.token_urlsafe(32)
            con = db()
            con.execute("INSERT INTO sessions(token,user_id,expires) VALUES(?,?,?)", (token, r["id"], int(time.time()) + 30*86400))
            con.commit(); con.close()
            self.send_response(302)
            self.send_header("Location", "/admin" if r["role"] == "admin" else "/espace")
            self.send_header("Set-Cookie", f"session={token}; Path=/; HttpOnly; SameSite=Lax")
            self.end_headers(); return
        self.alert_page("Identifiants incorrects.", "err", "/login")

    def register(self, user):
        body = """<section><div class="wrap" style="max-width:460px">
<div class="formcard">
<h2 style="font-size:28px;margin-bottom:6px">Créer un compte</h2>
<p class="sub" style="font-size:14px">Suivez vos devis, factures et réservations.</p>
<form method="post" action="/register">
<label>Nom</label><input name="name" required>
<label>E-mail</label><input type="email" name="email" required>
<label>Téléphone</label><input name="phone">
<label>Mot de passe</label><input type="password" name="password" required minlength="8">
<button class="btn" type="submit" style="width:100%">Créer mon compte</button>
</form></div></div></section>"""
        self.ok(page(user, "Inscription — L'Effet Waouh", body))

    def register_post(self):
        f = self.form()
        email = f.get("email", "").strip().lower()
        if db().execute("SELECT id FROM users WHERE email=?", (email,)).fetchone():
            self.alert_page("Un compte existe déjà avec cet e-mail.", "err", "/register")
            return
        con = db()
        con.execute("INSERT INTO users(email,name,phone,password_hash,role,created_at) VALUES(?,?,?,?,?,?)",
                    (email, f.get("name", ""), f.get("phone", ""), hash_pw(f.get("password", "")), "client", NOW()))
        uid = con.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()["id"]
        token = secrets.token_urlsafe(32)
        con.execute("INSERT INTO sessions(token,user_id,expires) VALUES(?,?,?)", (token, uid, int(time.time()) + 30*86400))
        con.commit(); con.close()
        send_email(email, "Bienvenue chez L'Effet Waouh ✨",
                   "Bienvenue ! Votre espace client est prêt. Vous pouvez suivre vos devis, factures et réservations à tout moment.\n\nL'Effet Waouh", "welcome")
        self.send_response(302); self.send_header("Location", "/espace")
        self.send_header("Set-Cookie", f"session={token}; Path=/; HttpOnly; SameSite=Lax")
        self.end_headers()

    def logout(self):
        token = self.session_token()
        if token:
            con = db(); con.execute("DELETE FROM sessions WHERE token=?", (token,)); con.commit(); con.close()
        redirect(self, "/")

    # ---------------------------------------------------------------- espace client
    def espace(self, user):
        if not user: return redirect(self, "/login")
        con = db()
        bookings = con.execute("SELECT b.*, i.number, i.status AS inv_status FROM bookings b LEFT JOIN invoices i ON i.booking_id=b.id WHERE b.email=? ORDER BY b.id DESC", (user["email"],)).fetchall()
        out = con.execute("SELECT * FROM outbox WHERE to_email=? ORDER BY id DESC LIMIT 5", (user["email"],)).fetchall()
        con.close()
        rows = "".join(f'<tr><td>{esc(b["number"] or "—")}</td><td>{esc(b["event_date"])}</td><td>{esc(b["pack"])}</td><td style="text-align:right">{b["total"]} €</td><td><span class="pill wait">{esc(b["status"])}</span></td></tr>' for b in bookings)
        msgs = "".join(f'<div class="card"><h3 style="font-size:16px">{esc(m["subject"])}</h3><p style="font-size:13px;color:#6b5f52">{esc(m["created_at"])}</p><p style="font-size:13.5px;white-space:pre-wrap">{esc(m["body"])}</p></div>' for m in out)
        body = f"""<section><div class="wrap">
<h2>Bonjour {esc(user["name"] or "")} 👋</h2>
<p class="sub">Votre espace client — réservations, factures et messages.</p>
<div class="grid2">
<div class="card"><h3>Mes réservations</h3>
{'<table class="table" style="margin-top:8px"><tr><th>Devis</th><th>Date</th><th>Pack</th><th>Total</th><th>Statut</th></tr>' + rows + '</table>' if rows else '<p>Aucune réservation pour l’instant.</p>'}
<div style="margin-top:12px"><a class="btn small" href="/reservation">Nouvelle réservation</a></div></div>
<div class="card"><h3>Mes derniers messages</h3>{msgs or '<p>Aucun message.</p>'}</div>
</div></div></section>"""
        self.ok(page(user, "Espace client — L'Effet Waouh", body, "espace"))

    def profil_post(self, user):
        if not user: return redirect(self, "/login")
        f = self.form()
        con = db()
        con.execute("UPDATE users SET name=?, phone=? WHERE id=?", (f.get("name", ""), f.get("phone", ""), user["id"]))
        con.commit(); con.close()
        self.alert_page("Profil mis à jour.", "ok", "/espace")

    # ---------------------------------------------------------------- ADMIN
    def controle(self, user):
        p = os.path.join(BASE, "controle", "centre-de-controle.html")
        if os.path.isfile(p):
            b = open(p, "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers(); self.wfile.write(b)
        else:
            self.send_error(404)

    def admin(self, user):
        if not self.require(user, "admin"): return
        con = db()
        ca = con.execute("SELECT COALESCE(SUM(amount),0) a FROM invoices WHERE status IN ('payée','paye','acompte')").fetchone()["a"]
        ca_pend = con.execute("SELECT COALESCE(SUM(amount),0) a FROM invoices WHERE status='brouillon'").fetchone()["a"]
        n_clients = con.execute("SELECT COUNT(*) c FROM users WHERE role='client'").fetchone()["c"]
        n_leads = con.execute("SELECT COUNT(*) c FROM leads").fetchone()["c"]
        n_bookings = con.execute("SELECT COUNT(*) c FROM bookings").fetchone()["c"]
        hot = con.execute("SELECT COUNT(*) c FROM leads WHERE score>=70 AND status NOT IN ('Client','Fidélisation')").fetchone()["c"]
        queued = con.execute("SELECT COUNT(*) c FROM outbox WHERE status='queued'").fetchone()["c"]
        errors = con.execute("SELECT COUNT(*) c FROM events WHERE kind='error'").fetchone()["c"]
        con.close()
        alerts = []
        if hot: alerts.append(f"{hot} prospect(s) chaud(s) à contacter (score ≥ 70).")
        if ca_pend: alerts.append(f"{ca_pend:.0f} € de devis en attente de paiement.")
        if queued: alerts.append(f"{queued} e-mail(s) en file d'attente (SMTP non connecté).")
        if errors: alerts.append(f"{errors} erreur(s) système dans les logs.")
        alert_html = "".join(f'<div class="alert warn">⚠️ {esc(a)}</div>' for a in alerts) or '<div class="alert ok">✅ Tout est sous contrôle.</div>'
        body = f"""<section><div class="wrap">
<h2>Dashboard CEO</h2>
{alert_html}
<div class="kpi">
<div class="stat"><div class="n">{ca:,.0f} €</div><div class="l">Chiffre d'affaires encaissé</div></div>
<div class="stat"><div class="n">{ca_pend:,.0f} €</div><div class="l">Devis en attente</div></div>
<div class="stat"><div class="n">{n_bookings}</div><div class="l">Réservations</div></div>
<div class="stat"><div class="n">{n_leads}</div><div class="l">Leads ({hot} chauds)</div></div>
</div>
<div class="grid2">
<div class="card"><h3>Actions rapides</h3>
<p><a href="/admin/leads">→ Gérer les leads (CRM)</a></p>
<p><a href="/admin/bookings">→ Gérer les réservations &amp; factures</a></p>
<p><a href="/admin/outbox">→ Voir les e-mails ({queued} en attente)</a></p>
<p><a href="/admin/agents">→ Lancer les agents IA (rapport du jour)</a></p>
<p><a href="/admin/settings">→ Configurer SMTP / Stripe</a></p>
<p><a href="/controle">→ Centre de contrôle (création des comptes)</a></p>
</div>
<div class="card"><h3>Pipeline commercial</h3>
<table class="table">{self.pipeline_rows()}</table>
</div>
</div></div></section>"""
        self.ok(page(user, "Dashboard CEO — L'Effet Waouh", body, "admin"))

    def pipeline_rows(self):
        rows = ""
        for st in PIPELINE:
            c = db().execute("SELECT COUNT(*) c FROM leads WHERE status=?", (st,)).fetchone()["c"]
            rows += f'<tr><td>{esc(st)}</td><td style="text-align:right"><strong>{c}</strong></td></tr>'
        return rows

    def admin_leads(self, user):
        if not self.require(user, "admin"): return
        leads = db().execute("SELECT * FROM leads ORDER BY score DESC, id DESC").fetchall()
        rows = "".join(f'''<tr><td>{l["id"]}</td><td>{esc(l["contact"] or l["company"] or "—")}</td><td>{esc(l["email"])}</td>
<td><span class="pill">{esc(l["status"])}</span></td><td><strong>{l["score"]}</strong></td>
<td>{esc(l["source"])}</td><td><a href="/admin/leads/{l["id"]}">Ouvrir</a></td></tr>''' for l in leads)
        body = f"""<section><div class="wrap"><h2>CRM — Leads</h2>
<div class="alert ok">Pipeline : Nouveau lead → Qualifié → Contacté → Réponse → Rendez-vous → Proposition → Négociation → Client → Fidélisation</div>
<table class="table"><tr><th>#</th><th>Nom</th><th>E-mail</th><th>Statut</th><th>Score</th><th>Source</th><th></th></tr>{rows}</table>
</div></section>"""
        self.ok(page(user, "Leads — L'Effet Waouh", body, "admin"))

    def admin_lead(self, user, lid):
        if not self.require(user, "admin"): return
        l = db().execute("SELECT * FROM leads WHERE id=?", (lid,)).fetchone()
        if not l: return self.send_error(404)
        opts = "".join(f'<option value="{esc(s)}" {"selected" if s==l["status"] else ""}>{esc(s)}</option>' for s in PIPELINE)
        body = f"""<section><div class="wrap" style="max-width:640px">
<h2>Lead #{l["id"]} — {esc(l["contact"] or l["company"] or "Sans nom")}</h2>
<form method="post" action="/admin/leads/{l["id"]}">
<label>Statut</label><select name="status">{opts}</select>
<label>Score (0-100)</label><input type="number" name="score" value="{l["score"]}">
<label>Potentiel commercial</label><input name="potential" value="{esc(l["potential"] or "")}" placeholder="Élevé / Moyen / Faible">
<label>Prochaine action</label><input name="next_action" value="{esc(l["next_action"] or "")}">
<label>Notes</label><textarea name="notes" rows="4">{esc(l["notes"] or "")}</textarea>
<button class="btn" type="submit">Enregistrer</button>
</form>
<div class="card" style="margin-top:16px"><h3>Détails</h3>
<p>E-mail : {esc(l["email"] or "—")} · Tél : {esc(l["phone"] or "—")}<br>
Site : {esc(l["website"] or "—")} · Réseaux : {esc(l["socials"] or "—")}<br>
Secteur : {esc(l["sector"] or "—")} · Source : {esc(l["source"] or "—")}<br>
Premier contact : {esc(l["first_contact"] or "—")} · Dernière interaction : {esc(l["last_interaction"] or "—")}</p></div>
</div></section>"""
        self.ok(page(user, f"Lead #{lid} — L'Effet Waouh", body, "admin"))

    def admin_lead_post(self, user, lid):
        if not self.require(user, "admin"): return
        f = self.form()
        con = db()
        con.execute("UPDATE leads SET status=?, score=?, potential=?, next_action=?, notes=?, last_interaction=? WHERE id=?",
                     (f.get("status", "Nouveau lead"), int(f.get("score", 0) or 0), f.get("potential", ""),
                      f.get("next_action", ""), f.get("notes", ""), NOW(), lid))
        con.commit(); con.close()
        log_event("lead_updated", f"lead#{lid} -> {f.get('status')}")
        redirect(self, "/admin/leads")

    def admin_bookings(self, user):
        if not self.require(user, "admin"): return
        bs = db().execute("""SELECT b.*, i.number, i.status inv FROM bookings b
                             LEFT JOIN invoices i ON i.booking_id=b.id ORDER BY b.id DESC""").fetchall()
        rows = "".join(f'''<tr><td>{esc(b["number"] or "—")}</td><td>{esc(b["name"])}</td><td>{esc(b["event_date"])}</td>
<td>{esc(b["pack"])}</td><td style="text-align:right">{b["total"]} €</td><td><span class="pill wait">{esc(b["status"])}</span></td>
<td><form method="post" action="/admin/bookings/{b["id"]}" style="display:flex;gap:6px">
<select name="status" style="width:auto;margin:0">{self.status_opts(b["status"])}</select>
<button class="btn small">OK</button></form></td></tr>''' for b in bs)
        body = f'<section><div class="wrap"><h2>Réservations &amp; factures</h2><table class="table"><tr><th>Devis</th><th>Client</th><th>Date</th><th>Pack</th><th>Total</th><th>Statut</th><th>Changer</th></tr>{rows}</table></div></section>'
        self.ok(page(user, "Réservations — L'Effet Waouh", body, "admin"))

    def status_opts(self, cur):
        return "".join(f'<option value="{esc(s)}" {"selected" if s==cur else ""}>{esc(s)}</option>' for s in ["devis", "acompte", "payé", "paye", "confirmé", "confirme", "terminé", "termine", "annulé", "annule"])

    def admin_booking_post(self, user, bid):
        if not self.require(user, "admin"): return
        f = self.form()
        st = f.get("status", "devis")
        con = db()
        con.execute("UPDATE bookings SET status=? WHERE id=?", (st, bid))
        con.execute("UPDATE invoices SET status=? WHERE booking_id=?", (st, bid))
        con.commit(); con.close()
        log_event("booking_updated", f"booking#{bid} -> {st}")
        redirect(self, "/admin/bookings")

    def admin_outbox(self, user):
        if not self.require(user, "admin"): return
        ms = db().execute("SELECT * FROM outbox ORDER BY id DESC LIMIT 100").fetchall()
        rows = "".join(f'<tr><td>{m["id"]}</td><td>{esc(m["to_email"])}</td><td>{esc(m["subject"])}</td><td>{esc(m["kind"])}</td><td><span class="pill {"ok" if m["status"]=="sent" else "wait"}">{esc(m["status"])}</span></td><td>{esc(m["created_at"])}</td></tr>' for m in ms)
        body = f'<section><div class="wrap"><h2>E-mails (outbox)</h2><div class="alert warn">⚠️ Les e-mails sont stockés localement tant que SMTP n\'est pas connecté (menu Réglages).</div><table class="table"><tr><th>#</th><th>Destinataire</th><th>Objet</th><th>Type</th><th>Statut</th><th>Date</th></tr>{rows}</table></div></section>'
        self.ok(page(user, "E-mails — L'Effet Waouh", body, "admin"))

    def admin_agents(self, user):
        if not self.require(user, "admin"): return
        report_path = os.path.join(BASE, "reports", "latest.md")
        report = open(report_path, encoding="utf-8").read() if os.path.isfile(report_path) else "Aucun rapport généré pour l'instant."
        body = f"""<section><div class="wrap">
<h2>Agents IA</h2><p class="sub">Le rapport ci-dessous est généré par l'équipe d'agents (CEO, Commercial, Social, SEO, Data) à partir des données réelles de la base.</p>
<a class="btn" href="/admin/agents/run">▶️ Lancer les agents maintenant</a>
<div class="card" style="margin-top:18px">{md_to_html(report)}</div>
</div></section>"""
        self.ok(page(user, "Agents IA — L'Effet Waouh", body, "admin"))

    def admin_agents_run(self, user):
        if not self.require(user, "admin"): return
        try:
            r = subprocess.run(["python3", os.path.join(BASE, "automation", "agents.py")],
                               capture_output=True, text=True, timeout=120, cwd=BASE)
            log_event("agents_ran", r.stdout[-400:] if r.stdout else r.stderr[-400:])
        except Exception as e:
            log_event("agents_error", str(e))
        redirect(self, "/admin/agents")

    def admin_settings(self, user):
        if not self.require(user, "admin"): return
        body = f"""<section><div class="wrap" style="max-width:640px">
<h2>Réglages</h2>
<form method="post" action="/admin/settings">
<h3>E-mail (SMTP)</h3>
<label>Hôte SMTP</label><input name="smtp_host" value="{esc(get_setting('smtp_host'))}" placeholder="smtp.gmail.com">
<label>Port</label><input name="smtp_port" value="{esc(get_setting('smtp_port','587'))}">
<label>Utilisateur</label><input name="smtp_user" value="{esc(get_setting('smtp_user'))}">
<label>Mot de passe (mot de passe d'application)</label><input type="password" name="smtp_pass" value="{esc(get_setting('smtp_pass'))}">
<label>Adresse d'expédition</label><input name="smtp_from" value="{esc(get_setting('smtp_from', SITE_EMAIL))}">
<h3>Paiement (Stripe)</h3>
<label>Clé secrète Stripe</label><input name="stripe_sk" value="{esc(get_setting('stripe_sk'))}" placeholder="sk_live_...">
<button class="btn" type="submit">Enregistrer</button>
</form></div></section>"""
        self.ok(page(user, "Réglages — L'Effet Waouh", body, "admin"))

    def admin_settings_post(self, user):
        if not self.require(user, "admin"): return
        f = self.form()
        for k in ["smtp_host", "smtp_port", "smtp_user", "smtp_pass", "smtp_from", "stripe_sk"]:
            if f.get(k): set_setting(k, f[k])
        log_event("settings_updated", "SMTP/Stripe")
        self.alert_page("Réglages enregistrés.", "ok", "/admin/settings")

    # ---------------------------------------------------------------- utilitaires réponse
    def serve_img(self, name):
        if not re.match(r"^[A-Za-z0-9._-]+$", name):
            self.send_error(404); return
        p = os.path.join(VISUELS_DIR, name)
        if not os.path.isfile(p):
            self.send_error(404); return
        ext = os.path.splitext(name)[1].lower()
        ctype = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png" if ext == ".png" else "application/octet-stream"
        b = open(p, "rb").read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "public, max-age=86400")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers(); self.wfile.write(b)

    def ok(self, html_str):
        b = html_str.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers(); self.wfile.write(b)

    def alert_page(self, msg, kind, back):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        body = page(None, "Message", f'<section><div class="wrap" style="max-width:560px"><div class="alert {kind}">{msg}</div><a class="btn" href="{back}">Continuer</a></div></section>')
        b = body.encode("utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers(); self.wfile.write(b)

def main():
    init_db()
    print(f"✅ L'Effet Waouh démarré sur http://{HOST}:{PORT}")
    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    srv.serve_forever()

if __name__ == "__main__":
    main()
