#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit la landing page marketing de L'Effet Waouh (images intégrées en base64)."""
import base64, io, os
from PIL import Image

VISUELS = "visuels"
OUT_DIR = "waouh/site"
OUT = os.path.join(OUT_DIR, "landing.html")
os.makedirs(OUT_DIR, exist_ok=True)

def datauri(name, max_w=1100, q=74):
    p = os.path.join(VISUELS, name)
    im = Image.open(p).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

I = {k: datauri(v) for k, v in {
    "hero": "01-hero.jpg", "pb360": "02-photobooth-360.jpg", "audio": "03-livre-or-audio.jpg",
    "neon": "04-neon.jpg", "cierges": "05-cierges-magiques.jpg", "bulles": "06-bulles-confettis.jpg",
    "miroir": "07-miroir-magique.jpg", "balles": "08-piscine-balles.jpg", "danse": "09-premiere-danse.jpg",
    "vindhonneur": "10-vin-honneur.jpg", "install": "12-installation.jpg", "sans": "13-sans-animation.jpg",
}.items()}

def card(img, name, prix, tag=""):
    t = f'<span class="gtag">{tag}</span>' if tag else ""
    return f'''<div class="gcard">
  <div class="gimg"><img src="{img}" alt="{name}"><span class="gprix">{prix} €</span>{t}</div>
  <div class="gbody"><h4>{name}</h4><a href="/reservation" class="glink">Réserver →</a></div>
</div>'''

gallery = "".join([
    card(I["pb360"], "Photobooth 360", "550", "Star des Reels"),
    card(I["miroir"], "Miroir magique", "600", "Premium"),
    card(I["audio"], "Livre d'or audio", "99", "Viral 2026"),
    card(I["neon"], "Néon « Mr & Mrs »", "150", "Sur toutes les photos"),
    card(I["cierges"], "Cierges magiques", "180", "La photo iconique"),
    card(I["bulles"], "Bulles & confettis", "150", "Sortie de mairie"),
    card(I["balles"], "Piscine à balles LED", "300", "Coin insta"),
    card(I["danse"], "Canons à confettis CO2", "250", "Première danse"),
])

html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>L'Effet Waouh — Animations & gadgets de mariage livrés clé en main</title>
<meta name="description" content="Photobooth 360, livre d'or audio, néons, cierges magiques : les animations qui rendent votre mariage inoubliable. Livraison, installation et opérateur inclus. Devis gratuit sous 24 h.">
<style>
:root{{--cream:#FAF6F0;--ink:#2F2A25;--terra:#B0764A;--terra2:#C67B4F;--gold:#D9A441;--gold2:#E8B26A;--sage:#7A8B6F;--line:#E7DED2;--soft:#F3EAE0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6}}
a{{text-decoration:none;color:inherit}}
h1,h2,h3,h4{{font-family:Georgia,'Times New Roman',serif;line-height:1.15}}
.wrap{{max-width:1120px;margin:0 auto;padding:0 22px}}
/* ---------- topbar ---------- */
.topbar{{position:sticky;top:0;z-index:100;background:rgba(250,246,240,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
.topbar .in{{max-width:1120px;margin:0 auto;padding:12px 22px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}}
.brand{{font-family:Georgia,serif;font-weight:700;font-size:20px;color:var(--ink)}}
.brand .spark{{color:var(--gold)}}
.brand small{{display:block;font-family:-apple-system,sans-serif;font-size:9.5px;letter-spacing:2.2px;color:var(--terra);font-weight:700;text-transform:uppercase}}
.nav{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}}
.nav a{{font-size:14px;font-weight:500;color:#5a4f42}}
.nav a:hover{{color:var(--terra)}}
.btn{{display:inline-block;background:var(--terra);color:#fff;padding:12px 22px;border-radius:999px;font-weight:700;font-size:15px;border:1px solid var(--terra);cursor:pointer;transition:.15s}}
.btn:hover{{background:var(--terra2);border-color:var(--terra2);transform:translateY(-1px)}}
.btn.gold{{background:var(--gold);border-color:var(--gold);color:#fff}}
.btn.gold:hover{{background:var(--gold2);border-color:var(--gold2)}}
.btn.ghost{{background:transparent;color:#fff;border-color:rgba(255,255,255,.7)}}
.btn.ghost:hover{{background:rgba(255,255,255,.12)}}
.btn.small{{padding:9px 16px;font-size:14px}}
/* ---------- hero ---------- */
.hero{{position:relative;min-height:92vh;display:flex;align-items:center;color:#fff;overflow:hidden}}
.hero .bg{{position:absolute;inset:0}}
.hero .bg img{{width:100%;height:100%;object-fit:cover;display:block;animation:kenburns 22s ease-in-out infinite alternate}}
@keyframes kenburns{{from{{transform:scale(1)}}to{{transform:scale(1.1)}}}}
.hero .shade{{position:absolute;inset:0;background:linear-gradient(115deg,rgba(24,15,10,.82) 0%,rgba(24,15,10,.45) 55%,rgba(24,15,10,.25) 100%)}}
.hero .content{{position:relative;z-index:2;max-width:1120px;margin:0 auto;padding:60px 22px;width:100%}}
.hero .kick{{display:inline-block;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);color:#E8B26A;font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:7px 14px;border-radius:999px;margin-bottom:18px}}
.hero h1{{font-size:clamp(34px,5.6vw,64px);max-width:780px;margin-bottom:18px;text-shadow:0 2px 30px rgba(0,0,0,.35)}}
.hero h1 em{{color:var(--gold2);font-style:italic}}
.hero p.lead{{font-size:clamp(16px,2vw,20px);max-width:620px;color:#f0e6d6;margin-bottom:28px}}
.hero .cta{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:26px}}
.chips{{display:flex;gap:10px;flex-wrap:wrap}}
.chip{{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);color:#fff;font-size:13px;padding:7px 13px;border-radius:999px;backdrop-filter:blur(4px)}}
.chip b{{color:#E8B26A}}
/* ---------- bandeau chiffres ---------- */
.stats{{background:var(--ink);color:#fff;padding:34px 0}}
.stats .wrap{{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}}
.stat{{text-align:center;flex:1;min-width:130px}}
.stat .n{{font-family:Georgia,serif;font-size:34px;color:var(--gold2)}}
.stat .l{{font-size:13px;color:#cdbfae;max-width:160px;margin:0 auto}}
/* ---------- sections ---------- */
section{{padding:72px 0}}
section.alt{{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}}
h2.sec{{font-size:clamp(28px,4vw,42px);margin-bottom:12px}}
h2.sec em{{color:var(--terra);font-style:italic}}
.sub{{color:#6b5f52;max-width:660px;margin-bottom:34px;font-size:16.5px}}
.center{{text-align:center}}
.center .sub{{margin-left:auto;margin-right:auto}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.grid2{{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}}
.card{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px;box-shadow:0 6px 24px rgba(47,42,37,.05)}}
.card h3{{font-size:21px;margin-bottom:8px}}
.card p{{color:#5c5246;font-size:14.8px}}
.card .num{{display:inline-flex;width:34px;height:34px;border-radius:50%;background:var(--soft);color:var(--terra);font-weight:800;align-items:center;justify-content:center;margin-bottom:12px}}
/* ---------- galerie ---------- */
.ggrid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}
.gcard{{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;transition:.2s;box-shadow:0 4px 16px rgba(47,42,37,.06)}}
.gcard:hover{{transform:translateY(-5px);box-shadow:0 16px 38px rgba(47,42,37,.16)}}
.gimg{{position:relative;height:190px;overflow:hidden}}
.gimg img{{width:100%;height:100%;object-fit:cover;display:block;transition:.35s}}
.gcard:hover .gimg img{{transform:scale(1.08)}}
.gprix{{position:absolute;left:10px;bottom:10px;background:rgba(24,15,10,.78);color:#fff;font-weight:700;font-size:13px;padding:5px 11px;border-radius:999px}}
.gtag{{position:absolute;top:10px;right:10px;background:var(--gold);color:#fff;font-size:10.5px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;padding:4px 9px;border-radius:999px}}
.gbody{{padding:13px 15px;display:flex;justify-content:space-between;align-items:center}}
.gbody h4{{font-size:15px;font-family:Georgia,serif}}
.glink{{color:var(--terra);font-weight:700;font-size:13px;white-space:nowrap}}
/* ---------- film ---------- */
.film{{position:relative;border-radius:22px;overflow:hidden;box-shadow:0 24px 60px rgba(24,15,10,.35);aspect-ratio:16/9;background:#000}}
.film .slide{{position:absolute;inset:0;opacity:0;transition:opacity 1s ease}}
.film .slide.on{{opacity:1}}
.film .slide img{{width:100%;height:100%;object-fit:cover;animation:kenburns 9s linear infinite}}
.film .cap{{position:absolute;left:0;right:0;bottom:0;padding:70px 30px 26px;background:linear-gradient(180deg,transparent,rgba(15,9,5,.88));color:#fff}}
.film .cap .time{{display:inline-block;background:var(--gold);color:#fff;font-weight:800;font-size:12px;letter-spacing:1px;padding:4px 11px;border-radius:999px;margin-bottom:9px}}
.film .cap h3{{font-size:clamp(20px,3vw,30px);margin-bottom:4px}}
.film .cap p{{font-size:15px;color:#efe4d2}}
.film .progress{{position:absolute;left:0;top:0;right:0;height:4px;background:rgba(255,255,255,.15)}}
.film .progress .bar{{height:100%;width:0;background:var(--gold);transition:width .2s linear}}
.film .ctrl{{position:absolute;top:14px;right:14px;z-index:5;display:flex;gap:8px}}
.film .ctrl button{{background:rgba(24,15,10,.6);border:1px solid rgba(255,255,255,.3);color:#fff;width:38px;height:38px;border-radius:50%;cursor:pointer;font-size:15px}}
.film .dots{{position:absolute;top:18px;left:18px;z-index:5;display:flex;gap:6px}}
.film .dots span{{width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,.4);cursor:pointer}}
.film .dots span.on{{background:var(--gold)}}
.filmnote{{text-align:center;color:#9b8f80;font-size:12.5px;margin-top:14px}}
/* ---------- timeline ---------- */
.tl{{display:grid;gap:0}}
.tlitem{{display:grid;grid-template-columns:120px 1fr;gap:22px;padding:22px 0;border-top:1px solid var(--line);align-items:start}}
.tlitem:first-child{{border-top:none}}
.tlitem .heure{{font-family:Georgia,serif;font-size:26px;color:var(--terra);font-weight:700}}
.tlitem .tim{{width:100%;aspect-ratio:16/10;border-radius:14px;overflow:hidden}}
.tlitem .tim img{{width:100%;height:100%;object-fit:cover;display:block}}
.tlitem h3{{font-size:20px;margin-bottom:4px}}
.tlitem p{{color:#5c5246;font-size:14.5px}}
.tlitem .reco{{display:inline-block;margin-top:9px;background:var(--soft);color:var(--terra);font-weight:700;font-size:13px;padding:6px 13px;border-radius:999px}}
/* ---------- packs ---------- */
.pack{{position:relative;background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 8px 28px rgba(47,42,37,.07)}}
.pack .pimg{{height:170px;overflow:hidden}}
.pack .pimg img{{width:100%;height:100%;object-fit:cover;display:block;transition:.35s}}
.pack:hover .pimg img{{transform:scale(1.07)}}
.pack .pbody{{padding:22px;display:flex;flex-direction:column;flex:1}}
.pack .pbody h3{{font-size:21px;margin-bottom:4px}}
.pack .prix{{font-family:Georgia,serif;font-size:32px;color:var(--terra);margin:6px 0 10px}}
.pack .prix small{{font-size:14px;font-family:system-ui;color:#6b5f52}}
.pack ul{{list-style:none;margin:0 0 16px}}
.pack li{{padding:4px 0;font-size:14px;color:#4a4035}}
.pack li::before{{content:"✓ ";color:var(--sage);font-weight:800}}
.pack.hot{{border:2px solid var(--gold)}}
.pack .flag{{position:absolute;top:12px;right:-40px;transform:rotate(45deg);background:var(--gold);color:#fff;font-size:11px;font-weight:800;letter-spacing:1px;padding:6px 46px;text-transform:uppercase}}
/* ---------- avant/après ---------- */
.avap{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.avap .pane{{position:relative;border-radius:20px;overflow:hidden;height:360px}}
.avap .pane img{{width:100%;height:100%;object-fit:cover;display:block}}
.avap .pane .lab{{position:absolute;left:0;right:0;bottom:0;padding:46px 20px 18px;background:linear-gradient(180deg,transparent,rgba(15,9,5,.86));color:#fff}}
.avap .pane .lab b{{font-size:17px;display:block;margin-bottom:2px}}
.avap .pane .lab span{{font-size:13.5px;color:#e4d8c4}}
/* ---------- avis ---------- */
.avis{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px}}
.avis .stars{{color:var(--gold);letter-spacing:2px;font-size:17px;margin-bottom:10px}}
.avis p{{font-size:15px;color:#4a4035;font-style:italic}}
.avis .who{{margin-top:12px;font-weight:700;font-size:14px}}
.avis .who span{{display:block;font-weight:500;color:#8a7d6d;font-size:12.5px}}
/* ---------- garanties ---------- */
.gar{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}
.gar .g{{text-align:center;padding:20px 14px;background:#fff;border:1px solid var(--line);border-radius:16px}}
.gar .ico{{font-size:30px;margin-bottom:8px}}
.gar .g b{{font-size:14.5px;display:block;margin-bottom:4px}}
.gar .g span{{font-size:12.8px;color:#6b5f52}}
/* ---------- FAQ ---------- */
.faq{{max-width:780px;margin:0 auto}}
.faq .q{{background:#fff;border:1px solid var(--line);border-radius:14px;margin-bottom:10px;overflow:hidden}}
.faq .q button{{width:100%;text-align:left;background:none;border:none;padding:17px 20px;font-size:15.5px;font-weight:600;color:var(--ink);cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:inherit}}
.faq .q button::after{{content:"+";font-size:22px;color:var(--terra);font-weight:400}}
.faq .q.open button::after{{content:"−"}}
.faq .a{{display:none;padding:0 20px 18px;color:#5c5246;font-size:14.5px}}
.faq .q.open .a{{display:block}}
/* ---------- CTA final ---------- */
.final{{background:linear-gradient(150deg,#2F2A25 0%,#4a3a2c 55%,#6b4a2f 100%);color:#fff;text-align:center;padding:80px 22px}}
.final h2{{font-size:clamp(30px,4.5vw,48px);margin-bottom:14px}}
.final h2 em{{color:var(--gold2)}}
.final p{{color:#e6d9c6;max-width:560px;margin:0 auto 28px;font-size:17px}}
.final .cta{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}
/* ---------- footer ---------- */
footer{{background:var(--ink);color:#cdbfae;padding:44px 0;font-size:14px}}
footer .cols{{display:flex;gap:46px;flex-wrap:wrap}}
footer b{{color:#fff}}
footer a{{color:var(--gold2)}}
footer .note{{margin-top:26px;font-size:12px;color:#8d8172;border-top:1px solid #3a332c;padding-top:18px}}
@media(max-width:900px){{.ggrid{{grid-template-columns:repeat(2,1fr)}}.grid3,.grid2,.gar{{grid-template-columns:1fr}}.avap{{grid-template-columns:1fr}}.tlitem{{grid-template-columns:1fr}}}}
@media(max-width:560px){{.ggrid{{grid-template-columns:1fr 1fr}}.nav a{{font-size:13px}}}}
</style>
</head>
<body>

<div class="topbar"><div class="in">
  <a href="#" class="brand"><span class="spark">✦</span> L'Effet Waouh<small>Animations & gadgets de mariage</small></a>
  <div class="nav">
    <a href="#galerie">Nos animations</a>
    <a href="#film">Le film</a>
    <a href="#jourj">Jour J</a>
    <a href="#packs">Packs</a>
    <a href="#faq">FAQ</a>
    <a class="btn small" href="/reservation">Réserver</a>
  </div>
</div></div>

<!-- ================= HERO ================= -->
<div class="hero">
  <div class="bg"><img src="{I['hero']}" alt="Réception de mariage avec photobooth 360 et néon"></div>
  <div class="shade"></div>
  <div class="content">
    <span class="kick">Photobooth 360 · Livre d'or audio · Néons · Cierges magiques</span>
    <h1>Le mariage dont vos invités <em>parleront encore</em> dans dix ans.</h1>
    <p class="lead">Les animations qui font le buzz, livrées chez vous et opérées de A à Z. Vous n'avez qu'une seule chose à faire : <b>profiter</b>.</p>
    <div class="cta">
      <a class="btn gold" href="/reservation">Réserver mon animation</a>
      <a class="btn ghost" href="#film">▶ Voir le film</a>
    </div>
    <div class="chips">
      <span class="chip">🎬 <b>Film d'ambiance</b> inclus dans la visite</span>
      <span class="chip">🚚 Livraison + installation <b>incluses</b></span>
      <span class="chip">👤 Opérateur <b>inclus</b> dans tous les packs</span>
      <span class="chip">💬 Devis gratuit <b>sous 24 h</b></span>
    </div>
  </div>
</div>

<!-- ================= BANDEAU CHIFFRES ================= -->
<div class="stats"><div class="wrap">
  <div class="stat"><div class="n">100 %</div><div class="l">des packs avec opérateur présent</div></div>
  <div class="stat"><div class="n">2 min</div><div class="l">pour réserver en ligne</div></div>
  <div class="stat"><div class="n">24 h</div><div class="l">pour recevoir votre devis</div></div>
  <div class="stat"><div class="n">0</div><div class="l">stress logistique le jour J</div></div>
</div></div>

<!-- ================= PROBLÈME / SOLUTION ================= -->
<section><div class="wrap">
  <div class="center"><h2 class="sec">Un mariage réussi, <em>ça se voit sur les visages</em>.</h2>
  <p class="sub">Sans animations, une réception retombe après le dîner : piste vide, invités qui repartent tôt, peu de photos à partager. Voici comment on règle ça.</p></div>
  <div class="grid3">
    <div class="card"><div class="num">1</div><h3>Le problème</h3><p>Des invités qui s'ennuient entre deux plats, une soirée qui s'essouffle, et des souvenirs qui se résument à quelques photos posées.</p></div>
    <div class="card"><div class="num">2</div><h3>Notre solution</h3><p>Des animations « effet waouh » placées aux bons moments : sortie de mairie, vin d'honneur, première danse, fin de soirée. Livrées, installées, opérées.</p></div>
    <div class="card"><div class="num">3</div><h3>Le résultat</h3><p>Des invités émerveillés, des centaines de photos et vidéos partagées, et vous qui profitez de chaque minute sans rien gérer.</p></div>
  </div>
</div></section>

<!-- ================= GALERIE ================= -->
<section class="alt" id="galerie"><div class="wrap">
  <div class="center"><h2 class="sec">Ça ressemble à quoi ? <em>Regardez.</em></h2>
  <p class="sub">Chaque animation est pensée pour créer un moment fort et des images magnifiques. Survolez, imaginez-la chez vous.</p></div>
  <div class="ggrid">{gallery}</div>
</div></section>

<!-- ================= FILM ================= -->
<section id="film"><div class="wrap">
  <div class="center"><h2 class="sec">Le film <em>de votre journée</em>, minute par minute.</h2>
  <p class="sub">Regardez comment chaque animation s'enchaîne naturellement dans un mariage — de la mairie à la fin de soirée.</p></div>
  <div class="film" id="filmBox">
    <div class="progress"><div class="bar" id="filmBar"></div></div>
    <div class="dots" id="filmDots"></div>
    <div class="ctrl"><button id="filmPlay" title="Lecture/Pause">❚❚</button></div>
    <div class="slide on"><img src="{I['bulles']}" alt="Sortie de mairie"><div class="cap"><span class="time">09:30 — La sortie de mairie</span><h3>Le premier « waouh » de la journée</h3><p>Une pluie de bulles et de confettis au moment du oui : l'effet cinéma qui lance la fête.</p></div></div>
    <div class="slide"><img src="{I['vindhonneur']}" alt="Vin d'honneur"><div class="cap"><span class="time">16:00 — Le vin d'honneur</span><h3>Les premiers éclats de rire</h3><p>Le livre d'or audio et le néon « Mr &amp; Mrs » captent les voix et les sourires de vos proches.</p></div></div>
    <div class="slide"><img src="{I['danse']}" alt="Première danse"><div class="cap"><span class="time">22:00 — La première danse</span><h3>Le moment que tout le monde filme</h3><p>Canons à confettis synchronisés, photobooth 360 qui tourne : l'instant devient viral.</p></div></div>
    <div class="slide"><img src="{I['cierges']}" alt="Sparkler exit"><div class="cap"><span class="time">23:30 — La fin de soirée</span><h3>La photo iconique</h3><p>Le tunnel de cierges magiques : l'image encadrée sur la cheminée, partagée cent fois.</p></div></div>
  </div>
  <p class="filmnote">🎬 Film d'ambiance réalisé à partir de nos visuels. Les vidéos réelles de nos prestations viendront s'y ajouter dès la première saison — chaque animation est pensée pour être <b>filmée</b>.</p>
</div></section>

<!-- ================= JOUR J ================= -->
<section class="alt" id="jourj"><div class="wrap">
  <div class="center"><h2 class="sec">Comment ça s'intègre <em>dans votre mariage</em> ?</h2>
  <p class="sub">Un déroulé type, heure par heure. On place chaque animation au moment où elle a le plus d'impact — et on s'occupe de tout.</p></div>
  <div class="tl">
    <div class="tlitem"><div class="heure">09:30</div><div><div class="tim"><img src="{I['bulles']}" alt="Sortie de mairie"></div><h3>Sortie de mairie</h3><p>Machines à bulles + canons à confettis positionnés avant votre arrivée. Le signal est donné au photographe : 3 minutes chrono, effet garanti.</p><span class="reco">🎈 Pack Sortie de Mairie — 199 €</span></div></div>
    <div class="tlitem"><div class="heure">16:00</div><div><div class="tim"><img src="{I['vindhonneur']}" alt="Vin d'honneur"></div><h3>Vin d'honneur</h3><p>Le livre d'or audio trône près du bar : vos invités laissent des messages vocaux. Le néon « Mr &amp; Mrs » devient le fond de toutes les photos.</p><span class="reco">📞 Livre d'or audio — 99 € · Néon — 150 €</span></div></div>
    <div class="tlitem"><div class="heure">22:00</div><div><div class="tim"><img src="{I['danse']}" alt="Première danse"></div><h3>Première danse</h3><p>Canons à confettis CO2 synchronisés sur la musique, photobooth 360 prêt à tourner : l'instant devient le clou du spectacle.</p><span class="reco">🎥 Photobooth 360 — 550 € · Canons — 250 €</span></div></div>
    <div class="tlitem"><div class="heure">23:30</div><div><div class="tim"><img src="{I['cierges']}" alt="Sparkler exit"></div><h3>Fin de soirée</h3><p>Le tunnel de cierges magiques clôt la soirée en apothéose. On fournit, on coordonne, on sécurise : vous traversez, le photographe shoote.</p><span class="reco">✨ Sparkler exit — 180 €</span></div></div>
  </div>
</div></section>

<!-- ================= PACKS ================= -->
<section id="packs"><div class="wrap">
  <div class="center"><h2 class="sec">Trois façons de dire <em>oui</em>.</h2>
  <p class="sub">Des formules clé en main, opérateur inclus. Réservez en 2 minutes, recevez votre devis sous 24 h.</p></div>
  <div class="grid3">
    <div class="pack"><div class="pimg"><img src="{I['bulles']}" alt="Pack Sortie de Mairie"></div><div class="pbody"><h3>Sortie de Mairie</h3><div class="prix">199 € <small>tout compris</small></div><ul><li>Bulles + confettis</li><li>Opérateur 30 min</li><li>Installation &amp; signal photographe</li></ul><a class="btn small" href="/reservation">Réserver</a></div></div>
    <div class="pack hot"><span class="flag">Le + choisi</span><div class="pimg"><img src="{I['pb360']}" alt="Pack Soirée Waouh"></div><div class="pbody"><h3>Soirée Waouh</h3><div class="prix">890 € <small>tout compris</small></div><ul><li>Photobooth 360 (6 h)</li><li>Livre d'or audio</li><li>Néon « Mr &amp; Mrs »</li><li>Opérateur dédié</li></ul><a class="btn" href="/reservation">Réserver</a></div></div>
    <div class="pack"><div class="pimg"><img src="{I['danse']}" alt="Pack Full Waouh"></div><div class="pbody"><h3>Full Waouh</h3><div class="prix">1 490 € <small>tout compris</small></div><ul><li>Pack Soirée + miroir magique</li><li>Cierges magiques</li><li>Canons à confettis</li><li>Opérateur 8 h</li></ul><a class="btn small" href="/reservation">Réserver</a></div></div>
  </div>
  <p class="center" style="margin-top:26px"><a class="btn ghost" style="color:var(--terra);border-color:var(--terra)" href="/tarifs">Voir le détail des tarifs à la carte →</a></p>
</div></section>

<!-- ================= AVANT / APRÈS ================= -->
<section class="alt"><div class="wrap">
  <div class="center"><h2 class="sec">La même salle. <em>Deux ambiances.</em></h2></div>
  <div class="avap">
    <div class="pane"><img src="{I['sans']}" alt="Sans animation"><div class="lab"><b>Sans animations</b><span>Une piste qui se vide à 23 h, des invités qui repartent tôt.</span></div></div>
    <div class="pane"><img src="{I['danse']}" alt="Avec L'Effet Waouh"><div class="lab"><b>Avec L'Effet Waouh</b><span>Une piste pleine jusqu'au bout, des souvenirs partout.</span></div></div>
  </div>
</div></section>

<!-- ================= AVIS ================= -->
<section><div class="wrap">
  <div class="center"><h2 class="sec">Ils ont tenté <em>l'effet waouh</em>.</h2></div>
  <div class="grid3">
    <div class="avis"><div class="stars">★★★★★</div><p>« Le photobooth 360 a fait l'unanimité. Nos invités en parlent encore des mois après. »</p><div class="who">Camille &amp; Julien<span>Mariage à Paris, juin</span></div></div>
    <div class="avis"><div class="stars">★★★★★</div><p>« Le livre d'or audio, c'est le meilleur investissement de notre mariage. Les voix de nos grands-parents, pour toujours. »</p><div class="who">Léa &amp; Hugo<span>Mariage en Yvelines, septembre</span></div></div>
    <div class="avis"><div class="stars">★★★★★</div><p>« Opérateur adorable, tout était installé à notre arrivée. On n'a eu à penser à rien. »</p><div class="who">Sarah &amp; Maxime<span>Mariage à Bordeaux, mai</span></div></div>
  </div>
  <p class="filmnote">Témoignages types à titre d'illustration — remplacés par vos avis réels (Google / Mariages.net) dès les premières prestations.</p>
</div></section>

<!-- ================= GARANTIES ================= -->
<section class="alt"><div class="wrap">
  <div class="center"><h2 class="sec">Pourquoi vous pouvez <em>nous faire confiance</em>.</h2></div>
  <div class="gar">
    <div class="g"><div class="ico">👤</div><b>Opérateur inclus</b><span>Présent sur place, il gère tout le jour J.</span></div>
    <div class="g"><div class="ico">🚚</div><b>Livraison &amp; montage</b><span>Installation et démontage à notre charge.</span></div>
    <div class="g"><div class="ico">🛡️</div><b>Assuré &amp; testé</b><span>Matériel vérifié avant chaque événement.</span></div>
    <div class="g"><div class="ico">🌦️</div><b>Plan B météo</b><span>Tout se replie en intérieur si besoin.</span></div>
  </div>
</div></section>

<!-- ================= FAQ ================= -->
<section id="faq"><div class="wrap">
  <div class="center"><h2 class="sec">Les questions <em>qu'on nous pose tout le temps</em>.</h2></div>
  <div class="faq">
    <div class="q open"><button>Combien ça coûte vraiment ?</button><div class="a">De 99 € (livre d'or audio) à 1 490 € (pack complet). Le photobooth 360 se loue 550 € la soirée, opérateur inclus. Le devis est gratuit et immédiat.</div></div>
    <div class="q"><button>Un opérateur est-il vraiment inclus ?</button><div class="a">Oui, dans tous les packs. À la carte, il est en option (60 €/heure). C'est lui qui installe, anime et veille sur le matériel.</div></div>
    <div class="q"><button>Et si le lieu est en dehors de Paris ?</button><div class="a">Les petits objets (livre d'or audio, néons) s'expédient partout en France. Les gros équipements se livrent en Île-de-France ; au-delà, sur devis.</div></div>
    <div class="q"><button>Peut-on personnaliser ?</button><div class="a">Oui : néons aux prénoms (à l'achat, vous le gardez), couleurs de confettis, message d'accueil du livre d'or audio à votre voix.</div></div>
    <div class="q"><button>Comment réserver ?</button><div class="a">Remplissez le formulaire en 2 minutes : devis immédiat + acompte de 30 % pour sécuriser la date. Solde 7 jours avant le jour J.</div></div>
  </div>
</div></section>

<!-- ================= CTA FINAL ================= -->
<div class="final">
  <h2>Votre date est <em>précieuse</em>. Réservez-la.</h2>
  <p>Les samedis de la saison partent vite. Décrivez votre projet en 2 minutes : devis gratuit, réponse sous 24 h, zéro engagement.</p>
  <div class="cta">
    <a class="btn gold" href="/reservation">Réserver mon animation</a>
    <a class="btn ghost" href="/contact">Poser une question</a>
  </div>
</div>

<footer><div class="wrap">
  <div class="cols">
    <div><b>L'Effet Waouh</b><br>Animations &amp; gadgets de mariage<br>Paris &amp; Île-de-France — livraison France entière</div>
    <div><b>Navigation</b><br><a href="#galerie">Animations</a> · <a href="#film">Film</a> · <a href="#packs">Packs</a> · <a href="/blog">Blog</a> · <a href="/faq">FAQ</a></div>
    <div><b>Légal</b><br><a href="/mentions-legales">Mentions légales</a> · <a href="/cgv">CGV</a> · <a href="/confidentialite">Confidentialité</a></div>
    <div><b>Contact</b><br><a href="mailto:contact@leffetwaouh.fr">contact@leffetwaouh.fr</a><br>Réponse sous 24 h ouvrées</div>
  </div>
  <div class="note">© 2026 L'Effet Waouh — Les visuels et témoignages de cette page sont des illustrations à valeur de démonstration ; ils seront remplacés par des photos et avis réels issus des prestations.</div>
</div></footer>

<script>
// ---------- film ----------
var slides = document.querySelectorAll('.film .slide');
var dotsWrap = document.getElementById('filmDots');
var bar = document.getElementById('filmBar');
var playBtn = document.getElementById('filmPlay');
var i = 0, playing = true, timer = null, dur = 5200, tick = 50;
for (var k=0;k<slides.length;k++){{(function(k){{var s=document.createElement('span');if(k===0)s.className='on';s.onclick=function(){{go(k)}};dotsWrap.appendChild(s);}})(k);}}
function go(n){{i=((n%slides.length)+slides.length)%slides.length;
  slides.forEach(function(s,x){{s.classList.toggle('on',x===i);}});
  dotsWrap.querySelectorAll('span').forEach(function(d,x){{d.classList.toggle('on',x===i);}});
  var t0=Date.now();
  clearInterval(timer);
  timer=setInterval(function(){{var p=Math.min(100,(Date.now()-t0)/dur*100);bar.style.width=p+'%';if(p>=100&&playing){{go(i+1);}}}},tick);
}}
function toggle(){{playing=!playing;playBtn.textContent=playing?'❚❚':'▶';
  if(playing)go(i);else clearInterval(timer);}}
playBtn.onclick=toggle;
go(0);

// ---------- FAQ ----------
document.querySelectorAll('.faq .q button').forEach(function(b){{
  b.addEventListener('click',function(){{b.parentElement.classList.toggle('open');}});
}});

// ---------- reveal ----------
try{{
  var obs=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.style.opacity=1;e.target.style.transform='none';obs.unobserve(e.target);}}}});}},{{threshold:.12}});
  document.querySelectorAll('section,.final,.film').forEach(function(s){{s.style.opacity=0;s.style.transform='translateY(18px)';s.style.transition='opacity .7s ease, transform .7s ease';obs.observe(s);}});
}}catch(e){{}}
</script>
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("OK ->", OUT, f"{os.path.getsize(OUT)/1024:.0f} Ko")
