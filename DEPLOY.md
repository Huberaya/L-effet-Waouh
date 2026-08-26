# Déploiement - L'Effet Waouh (Node.js / Express)

## 1. Pousser sur GitHub

```bash
git add .
git commit -m "feat: config Vercel Node.js Serverless"
git push origin main
```

## 2. Déployer sur Vercel (2 méthodes)

### Méthode A - Via Dashboard Vercel (Automatique)

1. Rends-toi sur [vercel.com/new](https://vercel.com/new)
2. Importe ton repository GitHub
3. **Framework Preset** : Laisser sur `Other`
4. **Root Directory** : `./` (laisser par défaut)
5. **Build Command** : `npm run build`
6. **Install Command** : `npm install`
7. Clique sur **Deploy**

### Méthode B - Via CLI Vercel

```bash
npm i -g vercel
vercel --prod
```

## 3. Architecture Vercel

- `vercel.json` : configure le runtime `@vercel/node` et inclut les templates Nunjucks (`app/**`) ainsi que les données (`src/**`).
- `api/index.js` : point d'entrée Serverless Function exportant l'application Express.
- `server.js` : application Node.js / Express compatible local & cloud.

## 4. Vérification après déploiement

- Santé du serveur : `https://ton-projet.vercel.app/health`
- Accueil : `https://ton-projet.vercel.app/`
- Univers Mariage : `https://ton-projet.vercel.app/univers/mariage`
- Kits Clés en main : `https://ton-projet.vercel.app/kits`
- Atelier Personnalisation : `https://ton-projet.vercel.app/personnalise`
- Backoffice Admin : `https://ton-projet.vercel.app/admin`
