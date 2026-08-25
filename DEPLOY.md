# Déploiement - L'Effet Waouh V2

## 1. Pousser sur GitHub (à faire toi-même, token révoqué)

```bash
cd /home/user/L-effet-Waouh
git status
git log --oneline -2
# Si déjà commité, juste push:
git push origin main

# Si remote demande auth:
# - Va sur https://github.com/settings/tokens -> Generate new token (classic)
# - coche repo
# - git remote set-url origin https://TON_NOUVEAU_TOKEN@github.com/Huberaya/L-effet-Waouh.git
# - git push origin main
# - Puis révoque le token immédiatement après
```

## 2. Déployer sur Vercel (2 méthodes)

### Méthode A - Via Dashboard Vercel (recommandé, 2 min)

1. Va sur https://vercel.com/new
2. Import Git Repository -> `Huberaya/L-effet-Waouh`
3. Framework Preset: **Other**
4. Root Directory: `./` (laisser vide)
5. Build Command: vide (Vercel détecte Python via vercel.json)
6. Variables d'environnement (Settings -> Environment Variables):
   ```
   DATABASE_URL=sqlite:////tmp/waouh_v2.db
   # Pour prod avec Postgres persistant (recommandé):
   # DATABASE_URL=postgresql://user:pass@host/db
   # Tu peux créer une DB gratuite sur https://neon.tech ou Vercel Postgres
   ```
7. Deploy -> Vercel va build `api/index.py`
8. Ton site sera sur `https://l-effet-waouh.vercel.app`

### Méthode B - Via CLI Vercel

```bash
npm i -g vercel
cd /home/user/L-effet-Waouh
vercel --prod
# Réponds aux questions, link au repo GitHub
```

## 3. Structure Vercel

```
vercel.json -> route tout vers api/index.py
api/index.py -> import app.main:app + auto-init DB dans /tmp
app/ -> FastAPI + templates + static
sql/ -> schema + seeds auto-exécutés si DB vide (cold start Vercel)
```

**Note importante SQLite sur Vercel:**
- Vercel filesystem est éphémère -> `/tmp/waouh_v2.db` est recréé à chaque cold start
- Pour l'instant, on auto-seed 30 produits à chaque démarrage (OK pour demo)
- Pour prod, passe à Postgres:
  - Crée DB sur Neon.tech (gratuit)
  - Ajoute DATABASE_URL dans Vercel Env
  - Le code bascule automatiquement sur Postgres

## 4. Test local avant deploy

```bash
pip install -r requirements.txt
python scripts/init_db.py
uvicorn app.main:app --reload --port 8000
# http://localhost:8000
# http://localhost:8000/api/products (JSON)
```

## 5. Après deploy

- Teste: https://ton-projet.vercel.app/health
- Teste: https://ton-projet.vercel.app/shop/event/gender_reveal
- Admin: https://ton-projet.vercel.app/admin-v2

## 6. Domaine custom

Dans Vercel Dashboard -> Settings -> Domains -> Add `leffetwaouh.fr`
