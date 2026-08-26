import express from 'express';
import nunjucks from 'nunjucks';
import cookieParser from 'cookie-parser';
import path from 'path';
import { fileURLToPath } from 'url';
import { store, BLOG_ARTICLES, SHIPPING_METHODS } from './src/data/catalog.js';
import { enrichProduct, enrichProducts } from './src/data/database.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

// Body & Cookie parsers
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

// Static assets
app.use('/static', express.static(path.join(process.cwd(), 'public', 'static')));
app.use('/static', express.static(path.join(__dirname, 'public', 'static')));
app.use('/static', express.static(path.join(process.cwd(), 'app', 'static')));
app.use('/static', express.static(path.join(__dirname, 'app', 'static')));
app.use('/images', express.static(path.join(process.cwd(), 'public', 'images')));
app.use('/images', express.static(path.join(process.cwd(), 'app', 'static', 'images')));
app.use(express.static(path.join(process.cwd(), 'public')));

// Configure Nunjucks Template Engine
const templateDirs = [
  path.join(__dirname, 'app', 'templates'),
  path.join(process.cwd(), 'app', 'templates')
];

const nunjucksEnv = nunjucks.configure(templateDirs, {
  autoescape: true,
  express: app,
  watch: false,
  noCache: true
});

// Custom Nunjucks filters
nunjucksEnv.addFilter('round', (num, decimals = 0) => {
  if (num === null || num === undefined || isNaN(num)) return '0';
  const factor = Math.pow(10, decimals);
  return (Math.round(Number(num) * factor) / factor).toFixed(decimals);
});

nunjucksEnv.addFilter('title', (str) => {
  if (!str) return '';
  return String(str).replace(/\w\S*/g, (txt) => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase());
});

nunjucksEnv.addFilter('slice', (arr, start, end) => {
  if (!arr) return [];
  if (typeof arr === 'string' || Array.isArray(arr)) {
    return arr.slice(start, end);
  }
  return arr;
});

nunjucksEnv.addFilter('int', (val) => parseInt(val, 10) || 0);

nunjucksEnv.addFilter('format', (val) => {
  if (typeof val === 'number') {
    return val.toFixed(2);
  }
  return String(val);
});

// Middleware to inject cart state and navigation locals
app.use((req, res, next) => {
  let token = req.cookies.waouh_cart_token;
  if (!token) {
    token = `cart_${Date.now()}_${Math.random().toString(36).slice(2, 10)}`;
    res.cookie('waouh_cart_token', token, { maxAge: 30 * 24 * 3600 * 1000, httpOnly: false });
  }
  req.cartToken = token;
  const cart = store.getOrCreateCart(token);
  const items = store.getCartItems(cart.id);
  const totalCount = items.reduce((acc, it) => acc + it.quantity, 0);

  res.locals.cart_count = totalCount;
  res.locals.cart_items = items;
  res.locals.current_path = req.path;
  res.locals.request = {
    path: req.path,
    url: { path: req.path, toString: () => req.url },
    query_params: { get: (k, d = '') => req.query[k] || d }
  };
  next();
});

// --- SHOP & CATALOG ROUTES ---

// 1. Home Page
app.get('/', (req, res) => {
  const universes = store.getUniverses();
  const rawFeatured = store.getFeaturedProducts(8);
  const featured = enrichProducts(rawFeatured);

  res.render('shop/home_premium.html', {
    universes,
    featured,
    current_universe: null
  });
});

// 2. Universe Landing Pages (/univers/:slug)
app.get('/univers/:slug', (req, res) => {
  const universe = store.getUniverseBySlug(req.params.slug);
  if (!universe) {
    return res.redirect('/explorer');
  }

  // Enrich all products in this universe
  const enrichedUniverse = {
    ...universe,
    products: enrichProducts(universe.products)
  };

  res.render('shop/universe.html', {
    universe: enrichedUniverse,
    current_universe: universe.slug,
    current_event: universe.id
  });
});

// 3. Explorer / Complete Catalog
app.get('/explorer', (req, res) => {
  const { event, filter, q, couleur, theme, age, price_range, custom_only, sort } = req.query;
  const universes = store.getUniverses();
  
  let products = store.filterProducts({ event, filter, q, couleur, theme, age, price_range, custom_only });
  products = enrichProducts(products);

  // Sorting
  if (sort === 'price-asc') {
    products.sort((a, b) => a.price_ttc - b.price_ttc);
  } else if (sort === 'price-desc') {
    products.sort((a, b) => b.price_ttc - a.price_ttc);
  }

  res.render('shop/explorer.html', {
    universes,
    products,
    current_universe: 'all',
    current_event: event || null,
    filter: filter || null,
    couleur: couleur || null,
    theme: theme || null,
    age: age || null,
    price_range: price_range || null,
    custom_only: custom_only || null,
    sort: sort || 'popular',
    query: q || ''
  });
});

// 4. Product Detail Page (/produit/:slug & /shop/p/:slug)
app.get(['/produit/:slug', '/shop/p/:slug'], (req, res) => {
  const product = store.getProductBySlug(req.params.slug);
  if (!product) {
    return res.redirect('/explorer');
  }

  const enriched = enrichProduct(product);
  const allProds = store.getAllProducts();
  const rawSimilar = allProds
    .filter(p => p.id !== enriched.id && (p.event_type === enriched.event_type || p.is_featured === 1))
    .slice(0, 4);
  const similar = enrichProducts(rawSimilar);

  res.render('shop/product_detail.html', {
    product: enriched,
    similar,
    current_universe: enriched.event_type.replace(/_/g, '-')
  });
});

// 5. Kits & Packs Clés en main (/kits)
app.get('/kits', (req, res) => {
  const all = store.getAllProducts();
  const kitsRaw = all.filter(p => 
    (p.slug && p.slug.includes('kit')) || 
    (p.name && p.name.toLowerCase().includes('kit')) || 
    p.price_ttc >= 29
  );
  const kits = enrichProducts(kitsRaw);

  res.render('shop/kits.html', {
    kits,
    current_path: '/kits'
  });
});

// 6. L'Atelier Personnalisation (/personnalise)
app.get('/personnalise', (req, res) => {
  const all = store.getAllProducts();
  const customRaw = all.filter(p => p.is_customizable === 1);
  const custom_products = enrichProducts(customRaw);

  res.render('shop/custom_atelier.html', {
    custom_products,
    current_path: '/personnalise'
  });
});

// 7. Intelligent Natural Search (/search)
app.get('/search', (req, res) => {
  const query = (req.query.q || '').trim();
  const rawResults = store.searchProducts(query);
  const results = enrichProducts(rawResults);

  const rawSuggested = results.length === 0 ? store.getFeaturedProducts(4) : [];
  const suggested = enrichProducts(rawSuggested);

  res.render('shop/search_results.html', {
    query,
    results,
    suggested
  });
});

// 8. Cart & Checkout
app.get('/cart', (req, res) => {
  const cart = store.getOrCreateCart(req.cartToken);
  const rawItems = store.getCartItems(cart.id);
  
  const items = rawItems.map(it => ({
    ...it,
    product: enrichProduct(it.product)
  }));

  const subtotal = items.reduce((acc, it) => acc + (it.quantity * it.price_ttc_at_add), 0);
  const roundedSubtotal = Math.round(subtotal * 100) / 100;
  const shipping = roundedSubtotal >= 59 ? 0 : 4.90;
  const total = Math.round((roundedSubtotal + shipping) * 100) / 100;

  const enrichedCart = {
    ...cart,
    items,
    subtotal_ttc: roundedSubtotal,
    shipping_cost: shipping,
    total_ttc: total
  };

  res.render('shop/cart.html', {
    cart: enrichedCart,
    shipping_methods: SHIPPING_METHODS
  });
});

app.post('/cart/add', (req, res) => {
  const { product_id, product_slug, variant_id, quantity, custom_text } = req.body;
  const cart = store.getOrCreateCart(req.cartToken);

  let pId = product_id;
  if (!pId && product_slug) {
    const p = store.getProductBySlug(product_slug);
    if (p) pId = p.id;
  }

  if (pId) {
    store.addToCart(cart.id, pId, variant_id, Number(quantity) || 1, custom_text || '');
  }

  const items = store.getCartItems(cart.id);
  const count = items.reduce((acc, it) => acc + it.quantity, 0);

  if (req.headers.accept && req.headers.accept.includes('application/json')) {
    return res.json({ ok: true, count });
  }

  res.redirect('/cart');
});

app.post('/cart/remove', (req, res) => {
  const { item_id } = req.body;
  const cart = store.getOrCreateCart(req.cartToken);
  if (item_id) {
    store.removeCartItem(cart.id, item_id);
  }
  if (req.headers.accept && req.headers.accept.includes('application/json')) {
    return res.json({ ok: true });
  }
  res.redirect('/cart');
});

app.post('/cart/remove/:id', (req, res) => {
  const cart = store.getOrCreateCart(req.cartToken);
  store.removeCartItem(cart.id, req.params.id);
  res.redirect('/cart');
});

app.post('/cart/clear', (req, res) => {
  const cart = store.getOrCreateCart(req.cartToken);
  store.clearCart(cart.id);
  if (req.headers.accept && req.headers.accept.includes('application/json')) {
    return res.json({ ok: true });
  }
  res.redirect('/cart');
});

// Checkout submission
app.post('/checkout', (req, res) => {
  const cart = store.getOrCreateCart(req.cartToken);
  const { customer_email } = req.body;

  const order = store.createOrder({
    cartId: cart.id,
    customerInfo: { email: customer_email || 'client@leffetwaouh.fr', first_name: 'Client', last_name: 'Privilégié' },
    shippingMethodCode: 'mondial_relay'
  });

  if (!order) {
    return res.redirect('/cart');
  }

  res.redirect(`/checkout/success/${order.number}`);
});

app.get('/checkout/success/:number', (req, res) => {
  const order = store.getOrder(req.params.number);
  if (!order) {
    return res.redirect('/explorer');
  }

  res.render('shop/success.html', {
    order,
    items: order.items || []
  });
});

// Legacy / Category Redirects
app.get('/shop', (req, res) => res.redirect('/explorer'));
app.get('/shop/c/:slug', (req, res) => {
  const slug = req.params.slug.replace(/_/g, '-');
  res.redirect(`/univers/${slug}`);
});
app.get(['/shop/event/:event_type', '/event/:event_type'], (req, res) => {
  const slug = req.params.event_type.replace(/_/g, '-');
  res.redirect(`/univers/${slug}`);
});

// 9. Blog Guides
app.get('/blog', (req, res) => {
  res.render('shop/blog.html', {
    articles: BLOG_ARTICLES
  });
});

app.get('/blog/:slug', (req, res) => {
  const slug = req.params.slug;
  const article = BLOG_ARTICLES.find(a => a.slug === slug);
  const relatedRaw = store.getFeaturedProducts(4);
  const related = enrichProducts(relatedRaw);

  res.render('shop/blog_article.html', {
    slug,
    article: article || { title: slug.replace(/-/g, ' '), desc: 'Guide et conseils L Effet Waouh' },
    related
  });
});

// 10. Admin Backoffice & Multi-Agents
const AGENTS = [
  { id: "ceo", name: "CEO Agent", role: "Stratégie & Arbitrage", status: "Active", desc: "Supervision globale, validation des prix et arbitrage rentabilité." },
  { id: "data", name: "Data Agent", role: "KPIs & Tracking", status: "Active", desc: "Analyse des ventes, calcul des marges moyennes et alertes stock." },
  { id: "catalogue", name: "Catalogue Agent", role: "Gestion Produits", status: "Active", desc: "Dédoublonnage, enrichissement des visuels et création des kits." },
  { id: "seo", name: "SEO Agent", role: "Positionnement & Mots-clés", status: "Active", desc: "Optimisation des balises, sitemap et articles de blog événementiels." },
  { id: "marketing", name: "Marketing Agent", role: "Campagnes & Conversion", status: "Active", desc: "Gestion des bannières promotionnelles et stratégie d'acquisition." },
  { id: "social", name: "Social Agent", role: "Réseaux Sociaux", status: "Active", desc: "Génération de scripts Reels/TikTok et calendrier de publication." },
  { id: "commercial", name: "Commercial Agent", role: "Devis & B2B", status: "Active", desc: "Gestion des demandes événementielles sur-mesure et grands comptes." },
  { id: "support", name: "Support Agent", role: "Service Client", status: "Active", desc: "Suivi des expéditions 48h Nantes et réponse aux questions fréquentes." },
  { id: "sourcing", name: "Sourcing Agent", role: "Fournisseurs & Marge", status: "Active", desc: "Négociation grossistes, optimisation des coûts et contrôle qualité." }
];

app.get('/admin', (req, res) => {
  const stats = store.getAdminStats();
  const ceo_recos = [
    "Prioriser les kits complets (panier moyen x3.7)",
    "Campagne Instagram Reels sur le ballon 90cm Gender Reveal",
    "Automatiser les relances paniers abandonnés",
    "Réapprovisionner les cierges magiques 40cm (best-seller été)",
    "Créer des variantes couleur sur les affiches personnalisées"
  ];

  res.render('admin/dashboard_v3.html', {
    stats,
    ceo_recos
  });
});

app.get('/admin/agents', (req, res) => {
  res.render('admin/agents.html', {
    agents: AGENTS
  });
});

app.get(['/admin/api/agents/:id/run', '/api/agents/:id/run'], (req, res) => {
  const agent = AGENTS.find(a => a.id === req.params.id);
  if (!agent) {
    return res.status(404).json({ error: "Agent not found" });
  }

  res.json({
    agent_id: agent.id,
    agent_name: agent.name,
    timestamp: new Date().toISOString(),
    status: "success",
    metrics_analyzed: {
      catalog_products: store.getAllProducts().length,
      stock_alerts: store.getAdminStats().stock_alert,
      average_order_value_target: "74.90€"
    },
    recommendation: `Action quotidienne effectuée avec succès pour ${agent.name}. Catalogue et flux optimisés.`
  });
});

// JSON API
app.get('/api/products', (req, res) => {
  res.json({ products: enrichProducts(store.getAllProducts()) });
});

app.get('/api/kpis', (req, res) => {
  res.json({ kpis: store.getAdminStats() });
});

// Healthcheck
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    version: 'v3-refonte-complete',
    uptime: process.uptime(),
    timestamp: new Date().toISOString()
  });
});

// Start Server (only when not run as a serverless function on Vercel)
if (!process.env.VERCEL) {
  app.listen(PORT, '0.0.0.0', () => {
    console.log(`L'Effet Waouh Server running at http://0.0.0.0:${PORT}`);
  });
}

export default app;
export { app };
