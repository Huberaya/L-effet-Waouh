# CRM + EMAIL + AUTOMATION - V3

## CRM Structure

### Table `users` enrichie
- id, email, name, phone, role
- + event_type (dernier événement acheté), event_date, source (instagram/tiktok/google), panier_moyen, frequence, LTV, comportement (pages vues)

### Table `orders` = historique
- Jointure pour calculer LTV, fréquence, panier moyen

### Table `events` (tracking comportement)
- kind: page_view, add_to_cart, search, personalize_start, checkout_start, purchase
- payload JSON: {product_id, event_type, query, personalization_fields}

### Segmentation
- Par événement: mariage, GR, naissance, baby shower, baptême, anniversaire
- Par date événement: ex mariage dans 3 mois → relance déco table
- Par panier moyen: <30€ (petit), 30-75€ (moyen), >75€ (premium kits)
- Par source: Instagram, TikTok, Pinterest, Google organique, direct
- Par comportement: visiteur, prospect (email capté), panier abandonné, client 1x, fidèle 2x+

---

## Email Automation (7 flux)

### 1. Bienvenue (après inscription newsletter)
- J0: Bienvenue + 10% BIENVENUE10 + best-sellers
- J2: Histoire marque + personnalisation
- J5: Kits complets + témoignages

### 2. Panier abandonné (après 1h, 24h, 72h)
- 1h: Rappel panier + photo produits + livraison gratuite dès 75€
- 24h: +10% WAOUH10 + urgence stock
- 72h: Dernier rappel + alternative kit

### 3. Navigation abandonnée (après vue produit sans ajout)
- J1: Vous avez regardé [produit] + produits similaires + avis

### 4. Post-achat (confirmation → livraison → avis → cross-sell)
- Immédiat: Confirmation commande + récap + délai
- Préparation: Votre commande est préparée à Nantes 📦
- Expédition: Tracking + vidéo tuto montage
- Livraison J+1: Livré ! Comment s'est passé votre événement? Photo?
- J+7: Demande avis vérifié + 10% prochaine commande
- J+14: Cross-sell selon événement: ex mariage → lune de miel? naissance → baptême?

### 5. Anniversaires & saisonnalité
- Anniversaire client (date naissance si renseignée): -15% + bougie chiffre offerte
- 1 an après naissance: Kit 1 an
- Saison: Noël, St Valentin, Fête des Mères/Pères, rentrée (diplôme)

### 6. Relance inactifs (90j sans achat)
- On vous a manqué? Nouveautés + best-sellers + -10%

### 7. Nouveautés & promos (newsletter hebdo)
- Nouveaux produits, thèmes anniversaire 2024, idées déco blog

---

## Templates Email (structure)

**Objet:** court, bénéfice, emoji
**Preheader:** complément objet
**Body:**
- Header logo + nav 9 entrées
- Hero image événement
- 3 bullets bénéfices
- Produits (2-4) avec CTA
- Preuve sociale (avis)
- Footer confiance + désabonnement

**Ton:** chaleureux, pas spam, personnalisé prénom + événement

---

## Automation Visiteur → Fidélisation

```
Visiteur (landing blog/SEO)
  ↓ email pop-up 10%
Prospect (email capté)
  ↓ panier
Panier (add_to_cart)
  ↓ checkout
Commande (pending)
  ↓ paiement Stripe
Paiement (paid)
  ↓ préparation Nantes 24h
Préparation (preparing)
  ↓ expédition + tracking
Expédition (shipped)
  ↓ livraison
Livraison (delivered)
  ↓ demande avis J+7
Avis (review)
  ↓ cross-sell J+14
Fidélisation (loyal)
  ↓ nouvelle commande (LTV)
```

Chaque étape = event dans `events` + email auto + mise à jour CRM

---

## Tech

- **Email:** Resend.com ou Brevo (ex Sendinblue) FR, API, templates MJML
- **CRM:** Table users + orders + events, dashboard admin
- **Tracking:** Plausible ou GA4 + events JS
- **Pop-up:** 10% après 30s ou exit intent, seulement si pas déjà client

---

## Action humaine requise

🔵 Ouvrir compte Brevo https://www.brevo.com/fr/ (gratuit 300 emails/j) + API key
🔵 Ouvrir compte Resend https://resend.com/ alternative
🔵 Configurer domaine SPF/DKIM pour délivrabilité
🟡 EN COURS: Tables events, email templates MJML à créer
