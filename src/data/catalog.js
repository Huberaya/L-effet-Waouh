import { enrichProduct, enrichProducts } from './database.js';

export const UNIVERSES = [
  {
    slug: "mariage",
    id: "mariage",
    name: "Mariage",
    tagline: "L'art de sublimer votre plus beau jour",
    subtitle: "Sortie de cérémonie féerique, dîner aux chandelles & décorations lumineuses",
    description: "Cierges magiques 40cm longue durée, arches de ballons blanc & or, rideaux LED 300 ampoules, livres d'or en bois gravé et contenants à dragées raffinés.",
    hero_image: "/static/images/09-premiere-danse-v1.jpg",
    mood_image: "/static/images/05-cierges-magiques-v1.jpg",
    accent: "#C5A880",
    guest_presets: [20, 50, 80, 100],
    themes: [
      { slug: "boheme-chic", name: "Bohème & Nature", icon: "🌾", desc: "Gaze de coton, eucalyptus et bois gravé" },
      { slug: "blanc-or", name: "Blanc & Or Chic", icon: "✨", desc: "Arches lumineuses, chrome gold et reflets chauds" },
      { slug: "feerie-nocturne", name: "Féerie Nocturne", icon: "🕯️", desc: "Cierges 40cm, néons LOVE et rideaux LED" }
    ],
    advice: [
      { title: "Sortie d'église ou de mairie", desc: "Prévoyez 1 cierge magique de 40cm et 20g de confettis biodégradables par invité pour des photos inoubliables." },
      { title: "Le coin Photobooth & Livre d'or", desc: "Installez un néon LED Mr & Mrs avec le livre d'or personnalisé sur une table nappée de gaze blanche." }
    ]
  },
  {
    slug: "gender-reveal",
    id: "gender_reveal",
    name: "Gender Reveal",
    tagline: "Le grand frisson de la révélation",
    subtitle: "Fille ou Garçon ? Créez un suspense magique et une explosion de joie",
    description: "Ballons géants 90cm opaques à éclater, fumigènes rose et bleu 60s intense, canons à confettis biodégradables et boîtes surprises XXL.",
    hero_image: "/static/images/products/gender-reveal-ballon-90cm-rose.jpg",
    mood_image: "/static/images/products/gender-reveal-fumigenes-rose-bleu.jpg",
    accent: "#D37589",
    guest_presets: [10, 20, 30],
    themes: [
      { slug: "rose-bleu-pastel", name: "Boy or Girl Pastel", icon: "🎈", desc: "Arche bicolore douce et ballons confettis" },
      { slug: "explosion-fumigene", name: "Révélation Éclatante", icon: "💨", desc: "Fumigènes denses pour photos extérieures sensationnelles" },
      { slug: "boite-mystere", name: "Boîte Surprise Envol", icon: "📦", desc: "Envolée de ballons hélium au déballage" }
    ],
    advice: [
      { title: "Comment réussir la vidéo de révélation ?", desc: "Privilégiez la lumière naturelle en fin d'après-midi et déclenchez les canons confettis et fumigènes au compte à rebours." },
      { title: "Animation des invités", desc: "Distribuez des badges Team Boy / Team Girl et des cartes à gratter pour faire participer tout le monde avant le grand moment." }
    ]
  },
  {
    slug: "baby-shower",
    id: "baby_shower",
    name: "Baby Shower",
    tagline: "Célébrer la future maman et l'arrivée de bébé",
    subtitle: "Une fête douce, cocooning et élégante entre proches",
    description: "Kits de décoration 70 pièces complets, arches pastel terracotta et eucalyptus, jeux & cartes pronostics et écharpes de reine.",
    hero_image: "/static/images/products/baby-shower-kit-fille-70pcs-real-web.jpg",
    mood_image: "/static/images/products/baby-shower-kit-garcon-70pcs.jpg",
    accent: "#A7BED3",
    guest_presets: [10, 15, 20],
    themes: [
      { slug: "terracotta-nature", name: "Terracotta & Sauge", icon: "🌿", desc: "Nuances végétales chaudes et chaleureuses" },
      { slug: "rose-poudre", name: "Rose Poudré & Or", icon: "🌸", desc: "Douceur florale et finitions dorées" },
      { slug: "bleu-nuage", name: "Bleu Ciel & Nuage", icon: "☁️", desc: "Ambiance aérienne et feutrée" }
    ],
    advice: [
      { title: "Moments forts du Baby Shower", desc: "Le jeu des pronostics de date/poids et l'ouverture des cadeaux autour d'un bar à douceurs bien décoré." }
    ]
  },
  {
    slug: "naissance",
    id: "naissance",
    name: "Naissance",
    tagline: "Bienvenue au monde, tout en délicatesse",
    subtitle: "Affiches personnalisées avec prénom, date et poids de naissance, bougies parfumées",
    description: "Des souvenirs éternels façonnés dans notre atelier : affiches de naissance minimalistes, guirlandes dorées et coffrets de bienvenue.",
    hero_image: "/static/images/products/naissance-affiche-personnalisee.jpg",
    mood_image: "/static/images/products/affiche-personnalisee-prenom.jpg",
    accent: "#E2A97E",
    guest_presets: [1, 5, 10],
    themes: [
      { slug: "minimaliste-art", name: "Minimaliste & Pureté", icon: "👶", desc: "Affiches aux lignes épurées et typographie élégante" },
      { slug: "dore-precieux", name: "Dorure & Souvenirs", icon: "⭐", desc: "Guirlandes dorées et bougies ambrées personnalisées" }
    ],
    advice: [
      { title: "Cadeau de naissance mémorable", desc: "L'affiche personnalisée encadrée avec le prénom, le poids et l'heure exacte reste le cadeau le plus touchant pour les jeunes parents." }
    ]
  },
  {
    slug: "bapteme",
    id: "bapteme",
    name: "Baptême",
    tagline: "Pureté, fleurs séchées et cadeaux d'invités raffinés",
    subtitle: "Célébrer le baptême avec des matières nobles et des attentions personnalisées",
    description: "Bougies en verre ambré gravées au prénom de l'enfant, fioles de fleurs séchées, contenants à dragées en plexi et magnets photo souvenirs.",
    hero_image: "/static/images/products/bapteme-bougie-verre-ambre-real-web.jpg",
    mood_image: "/static/images/products/bapteme-fiole-fleurs-sechees.jpg",
    accent: "#8B9D83",
    guest_presets: [15, 20, 30, 50],
    themes: [
      { slug: "fleurs-sechees-boheme", name: "Fleurs Séchées & Lin", icon: "💐", desc: "Fioles artisanales, brins d'eucalyptus et ficelle de lin" },
      { slug: "ambre-et-or", name: "Verre Ambré & Or", icon: "🕯️", desc: "Bougies cire végétale et lettrage doré personnalisé" },
      { slug: "epure-plexi", name: "Plexi & Transparence", icon: "💎", desc: "Contenants dragées modernes et magnets souvenirs" }
    ],
    advice: [
      { title: "Quantité de dragées à prévoir", desc: "Comptez une boîte ou fiole personnalisée par adulte (environ 5 à 7 dragées par fiole)." }
    ]
  },
  {
    slug: "anniversaire",
    id: "anniversaire",
    name: "Anniversaire",
    tagline: "Des décors thématiques immersifs de 1 à 99 ans",
    subtitle: "Kits 50 à 70 pièces prêts à monter : Licorne, Dinosaure, 30 Ans Rose Gold, Harry Potter...",
    description: "Tout pour transformer votre salon ou votre salle des fêtes en univers féerique sans stress : vaisselle coordonnée, arches de ballons, toppers de gâteau et guirlandes.",
    hero_image: "/static/images/products/anniversaire-licorne-70pcs-real-web.jpg",
    mood_image: "/static/images/products/anniversaire-30-ans-rose-gold.jpg",
    accent: "#B88E44",
    guest_presets: [10, 15, 20, 30],
    themes: [
      { slug: "enfants-magie", name: "Enfants : Licorne, Dinos, Espace", icon: "🦄", desc: "Décors féeriques et univers immersifs complets" },
      { slug: "adultes-chic", name: "Adultes : 20, 30, 40, 50 ans Rose Gold", icon: "🥂", desc: "Ballons chiffres géants, rideaux métallisés et confettis" },
      { slug: "glow-party", name: "Glow & Fluo Night", icon: "⚡", desc: "Ambiance boîte de nuit fluorescente ultra festive" }
    ],
    advice: [
      { title: "Temps de montage d'un kit anniversaire", desc: "Grâce à notre ruban d'arche pré-perforé et la notice illustrée fournie, assemblez votre décor complet en moins de 30 minutes." }
    ]
  }
];

export const CATEGORIES = UNIVERSES.map((u, i) => ({
  slug: u.slug,
  name: u.name,
  description: u.description,
  event_type: u.id,
  position: i + 1
}));

export const SHIPPING_METHODS = [
  { id: 1, code: "mondial_relay", name: "Point Relais (3-4 jours)", carrier: "Mondial Relay", price_ttc: 4.90, free_from: 59.0, is_active: 1, badge: "Économique" },
  { id: 2, code: "colissimo", name: "Colissimo Domicile 48h", carrier: "La Poste", price_ttc: 7.90, free_from: 75.0, is_active: 1, badge: "Le plus populaire" },
  { id: 3, code: "chrono", name: "Chronopost Express 24h", carrier: "Chronopost Nantes", price_ttc: 12.90, free_from: null, is_active: 1, badge: "Urgence / Dernier moment" }
];

export const BLOG_ARTICLES = [
  {
    slug: "reussir-sa-gender-reveal-guide-complet",
    title: "Comment organiser une Gender Reveal inoubliable : le guide 2026",
    desc: "Idées de révélation (fumigènes, ballon géant, boîte surprise), rétroplanning, budget et astuces photo.",
    event_type: "gender_reveal",
    read_time: "5 min",
    image: "/static/images/products/gender-reveal-ballon-90cm-rose.jpg",
    date: "Mars 2026"
  },
  {
    slug: "cierges-magiques-mariage-sortie-eglise",
    title: "Cierges magiques 40cm pour mariage : sécurité, timing et photos féeriques",
    desc: "Pourquoi choisir le format 40cm (durée 4 min), comment coordonner vos invités et réussir votre haie d'honneur.",
    event_type: "mariage",
    read_time: "4 min",
    image: "/static/images/05-cierges-magiques-v1.jpg",
    date: "Février 2026"
  },
  {
    slug: "cadeaux-invites-bapteme-tendance",
    title: "10 idées de cadeaux d'invités pour baptême qui changent des dragées classiques",
    desc: "Bougies parfumées en verre ambré, fioles de fleurs séchées et magnets photo personnalisés.",
    event_type: "bapteme",
    read_time: "6 min",
    image: "/static/images/products/bapteme-bougie-verre-ambre-real-web.jpg",
    date: "Janvier 2026"
  },
  {
    slug: "checklist-baby-shower-parfaite",
    title: "La checklist ultime pour préparer une Baby Shower sans stress",
    desc: "Des jeux qui plaisent à tout le monde, la décoration buffet et le livre des petits mots d'or.",
    event_type: "baby_shower",
    read_time: "5 min",
    image: "/static/images/products/baby-shower-kit-fille-70pcs-real-web.jpg",
    date: "Janvier 2026"
  }
];

export const RAW_PRODUCTS = [
  // --- GENDER REVEAL ---
  {
    id: 1, sku: "GR-BAL-90-001", slug: "ballon-eclatable-gender-reveal-90cm",
    name: "Ballon Géant Éclatable Gender Reveal 90cm + Confettis",
    short_desc: "Ballon noir 100% opaque 90cm avec confettis rose ou bleu au choix",
    long_desc: "Le best-seller absolu des Gender Reveals. Ballon en latex naturel extra-épais 90cm (36 pouces) garanti sans transparence. Livré avec 2 sachets de confettis de qualité supérieure (rose poudré et bleu ciel) et paille de remplissage. À percer avec une épingle pour un nuage féerique. 100% biodégradable.",
    price_ht: 8.33, price_ttc: 10.00, cost_price: 2.50, stock_qty: 150, weight_grams: 200,
    event_type: "gender_reveal", is_consumable: 1, is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["100% Opaque garanti", "Latex naturel biodégradable", "Nuage de confettis dense", "Notice et paille fournies"],
    specs: { "Diamètre": "90 cm (36 pouces)", "Matière": "Latex naturel", "Inclus": "1 ballon + confettis rose + confettis bleu", "Usage": "Intérieur ou extérieur" },
    variants: [
      { id: 1, sku: "GR-BAL-90-001-ROSE", name: "Rose Poudré (Fille)", attribute_type: "color", attribute_value: "rose", price_ttc: 10.00, stock_qty: 80 },
      { id: 2, sku: "GR-BAL-90-001-BLEU", name: "Bleu Ciel (Garçon)", attribute_type: "color", attribute_value: "bleu", price_ttc: 10.00, stock_qty: 70 }
    ]
  },
  {
    id: 2, sku: "GR-FUM-002", slug: "fumigenes-couleur-rose-bleu-lot-2",
    name: "Fumigènes à Main Couleur Gender Reveal - Lot de 2",
    short_desc: "Fumée ultra dense 60 secondes rose ou bleu, allumage par goupille",
    long_desc: "Créez une atmosphère spectaculaire pour vos photos et vidéos avec ce lot de 2 fumigènes à main 60 secondes. Fumée dense et vive. Déclenchement simple et sécurisé. Catégorie T1 (vente libre +18 ans). Attention, usage en extérieur uniquement.",
    price_ht: 12.42, price_ttc: 14.90, cost_price: 4.00, stock_qty: 80, weight_grams: 400,
    event_type: "gender_reveal", is_consumable: 1, is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Fumée intense 60s", "Allumage goupille sans briquet", "Ne tâche pas", "Parfait pour shooting photo"],
    specs: { "Durée": "60 secondes", "Portée fumée": "3 à 5 mètres", "Norme": "CE Catégorie T1", "Usage": "Extérieur uniquement" },
    variants: [
      { id: 3, sku: "GR-FUM-002-ROSE", name: "Lot 2x Rose Fille", attribute_type: "color", attribute_value: "rose", price_ttc: 14.90, stock_qty: 40 },
      { id: 4, sku: "GR-FUM-002-BLEU", name: "Lot 2x Bleu Garçon", attribute_type: "color", attribute_value: "bleu", price_ttc: 14.90, stock_qty: 40 },
      { id: 5, sku: "GR-FUM-002-MIX", name: "Pack Mixte 1 Rose + 1 Bleu (shooting)", attribute_type: "color", attribute_value: "mixte", price_ttc: 14.90, stock_qty: 20 }
    ]
  },
  {
    id: 3, sku: "GR-CAN-30-003", slug: "canon-confettis-gender-reveal-30cm",
    name: "Canon à Confettis & Poudre Holli Gender Reveal 30cm",
    short_desc: "Propulsion 6-8 mètres de confettis papier de soie et poudre colorée",
    long_desc: "Le double effet garanti : un jet de confettis festifs accompagné d'un nuage de poudre holli éclatant qui reste en suspension dans l'air. Tube de 30cm à rotation manuelle simple et sans danger.",
    price_ht: 3.25, price_ttc: 3.90, cost_price: 0.90, stock_qty: 300,
    event_type: "gender_reveal", is_consumable: 1, is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Double effet confettis + poudre", "Portée 8 mètres", "Papier biodégradable", "Déclenchement facile d'un quart de tour"],
    variants: [
      { id: 6, sku: "GR-CAN-30-003-ROSE-X1", name: "Rose x1", attribute_type: "pack_qty", attribute_value: "x1-rose", price_ttc: 3.90, stock_qty: 100 },
      { id: 7, sku: "GR-CAN-30-003-BLEU-X1", name: "Bleu x1", attribute_type: "pack_qty", attribute_value: "x1-bleu", price_ttc: 3.90, stock_qty: 100 },
      { id: 8, sku: "GR-CAN-30-003-ROSE-X3", name: "Lot 3x Rose (-10%)", attribute_type: "pack_qty", attribute_value: "x3-rose", price_ttc: 10.50, stock_qty: 50 },
      { id: 9, sku: "GR-CAN-30-003-BLEU-X3", name: "Lot 3x Bleu (-10%)", attribute_type: "pack_qty", attribute_value: "x3-bleu", price_ttc: 10.50, stock_qty: 50 }
    ]
  },
  {
    id: 4, sku: "GR-BOX-004", slug: "boite-surprise-gender-reveal-ballons",
    name: "Boîte Surprise Géante Gender Reveal à Ballons Hélium",
    short_desc: "Boîte blanche 60x60cm sérigraphiée avec ballons hélium à l'ouverture",
    long_desc: "Boîte rigide 60x60x60cm 'Boy or Girl ?' prête à être ouverte par les futurs parents. À l'ouverture des 4 battants, une grappe de ballons s'envole gracieusement vers le ciel.",
    price_ht: 20.75, price_ttc: 24.90, cost_price: 8.00, stock_qty: 25,
    event_type: "gender_reveal", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Dimensions XXL 60cm", "Effet waouh garanti", "Papier de soie & ruban inclus", "Réutilisable"]
  },
  {
    id: 7, sku: "GR-KIT-ARCHE-007", slug: "kit-arche-ballons-gender-reveal-85-pieces",
    name: "Kit Arche de Ballons Gender Reveal Pastel 85 Pièces",
    short_desc: "Arche complète rose poudré, bleu ciel, or chrome & guirlande Boy or Girl",
    long_desc: "Kit complet d'arche organique de ballons pour créer un superbe fond de photo. Comprend 40 ballons pastel rose/bleu, 20 blancs, 10 or confettis, 5 ballons métallisés spéciaux, ruban perforé 5m et pastilles de colle. Montage rapide sans hélium.",
    price_ht: 24.08, price_ttc: 28.90, cost_price: 9.00, stock_qty: 40,
    event_type: "gender_reveal", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["85 pièces coordonnées", "Sans besoin d'hélium", "Ruban de fixation 5m inclus", "Notice pas-à-pas illustrée"]
  },
  {
    id: 10, sku: "KIT-GR-410", slug: "kit-gender-reveal-premium-30-pers",
    name: "Kit Gender Reveal Prestige Tout-en-Un (30 Personnes)",
    short_desc: "La fête complète : Ballon 90cm + 4 Fumigènes + 6 Canons + Arche 85pcs + Badges",
    long_desc: "La solution clé en main ultime pour votre Gender Reveal : 1 ballon éclatable 90cm avec confettis, 4 fumigènes 60s, 6 canons à confettis, 1 arche 85 pièces, 30 badges pronostics Team Boy/Girl, 30 cartes à gratter et confettis de table. Économisez plus de 25% par rapport à l'achat unitaire.",
    price_ht: 107.42, price_ttc: 128.90, cost_price: 48.00, stock_qty: 15,
    event_type: "gender_reveal", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Formule complète 30 invités", "Économie immédiate de 35€", "Tout est prêt sans rien oublier", "Expédition 24h prioritaire"]
  },

  // --- MARIAGE ---
  {
    id: 12, sku: "MAR-ARCHE-100", slug: "arche-ballons-mariage-blanc-or-200pcs",
    name: "Grande Arche de Ballons Mariage Blanc & Or Chrome 200 Pièces",
    short_desc: "Arche somptueuse 3 mètres : ballons blancs mats, or miroir & confettis dorés",
    long_desc: "Transformez votre salle de réception ou votre entrée de cérémonie avec cette arche monumentale de 200 ballons. Nuances chic blanc satiné, or chrome brillant et ballons transparents remplis de confettis dorés. Ruban de guidage et pastilles adhésives inclus.",
    price_ht: 37.42, price_ttc: 44.90, cost_price: 16.00, stock_qty: 25,
    event_type: "mariage", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["200 ballons premium", "Rendu luxueux blanc & or", "Ruban d'arche 5m", "Tenue 48-72h gonflé à l'air"]
  },
  {
    id: 13, sku: "MAR-RIDEAU-101", slug: "rideau-lumineux-led-3x3m-chaud",
    name: "Rideau Lumineux LED 3x3m Blanc Chaud Féerique",
    short_desc: "Cascade de 300 micro-LED blanc chaud, 8 modes, télécommande & USB",
    long_desc: "Une tombée de lumière magique de 3m x 3m idéale en fond de table d'honneur, coin photobooth ou arche de cérémonie. Câble transparent discret, 8 modes d'animation lumineuse et variateur d'intensité avec télécommande incluse.",
    price_ht: 20.75, price_ttc: 24.90, cost_price: 8.00, stock_qty: 30,
    event_type: "mariage", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["300 micro-LED blanc chaud", "Dimensions 3x3m", "Télécommande 8 modes", "Consommation basse tension"]
  },
  {
    id: 14, sku: "MAR-LETTRES-102", slug: "lettres-lumineuses-love-40cm",
    name: "Lettres Lumineuses LOVE en Bois & LED 40cm",
    short_desc: "4 lettres volumétriques 40cm en bois blanc, ampoules blanc chaud vintage",
    long_desc: "L'accessoire iconique de la soirée de mariage. 4 lettres L-O-V-E de 40cm de haut avec ampoules LED chaleureuses. Fonctionne sur piles (pas de fil disgracieux). Crée un décor photo sublime et inoubliable.",
    price_ht: 74.08, price_ttc: 88.90, cost_price: 32.00, stock_qty: 12,
    event_type: "mariage", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Hauteur 40cm", "Bois robuste laqué blanc", "Sans fil (piles AA)", "Le point d'attraction photo"]
  },
  {
    id: 15, sku: "MAR-CIERGE-020", slug: "cierges-magiques-lot-50-40cm",
    name: "Cierges Magiques Étincelants 40cm - Lot de 50 (Durée 4min)",
    short_desc: "Cierges grand format 40cm pour haie d'honneur féerique, sans fumée",
    long_desc: "Le must-have des mariages d'aujourd'hui pour la sortie de mairie, l'ouverture de bal ou l'arrivée de la pièce montée. Durée exceptionnelle de 4 minutes complètes, permettant à tous les invités de s'allumer sereinement et aux photographes de capturer le cliché parfait. Étincelles dorées sans fumée toxique.",
    price_ht: 24.08, price_ttc: 28.90, cost_price: 9.00, stock_qty: 100, weight_grams: 500,
    event_type: "mariage", is_consumable: 1, is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Durée 4 minutes par cierge", "Longueur 40cm", "Sans fumée gênante", "Étincelles dorées intenses"],
    variants: [
      { id: 10, sku: "MAR-CIERGE-020-50", name: "Lot de 50 Cierges", attribute_type: "pack_qty", attribute_value: "50-pers", price_ttc: 28.90, stock_qty: 60 },
      { id: 11, sku: "MAR-CIERGE-020-100", name: "Lot de 100 Cierges (-15%)", attribute_type: "pack_qty", attribute_value: "100-pers", price_ttc: 48.90, stock_qty: 40 }
    ]
  },
  {
    id: 19, sku: "MAR-LIVRE-OR-025", slug: "livre-or-mariage-bois-personnalisable",
    name: "Livre d'Or Mariage en Bois Gravé Personnalisé",
    short_desc: "Couverture en bois naturel gravée aux prénoms des mariés & date du mariage",
    long_desc: "Un livre d'or noble et chaleureux au format 30x21cm. Couverture en bois de tilleul fin gravée au laser avec précision dans notre atelier nantais. Contient 60 pages (30 feuilles épaisses 250g/m²) pour recueillir les mots doux et photos Polaroïd de vos convives.",
    price_ht: 29.08, price_ttc: 34.90, cost_price: 11.00, stock_qty: 20,
    event_type: "mariage", is_featured: 1, is_active: 1, is_customizable: 1,
    highlights: ["Gravure laser personnalisée", "Bois naturel noble", "60 pages papier 250g", "Gravé avec amour à Nantes"]
  },
  {
    id: 20, sku: "MAR-NEON-027", slug: "neon-mr-mrs-led-60cm",
    name: "Néon LED Moderne 'Mr & Mrs' Blanc Chaud 60cm",
    short_desc: "Néon flexible nouvelle génération sur plaque acrylique transparente",
    long_desc: "Une lueur chaleureuse et élégante pour illuminer votre photobooth ou le fond de votre bar à cocktails. Tube LED silicone résistant, variateur de luminosité tactile inclus et chaîne de suspension.",
    price_ht: 74.08, price_ttc: 88.90, cost_price: 32.00, stock_qty: 10,
    event_type: "mariage", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Éclairage LED éco", "Variateur d'intensité", "Support plexi invisible", "Prêt à brancher"]
  },
  {
    id: 22, sku: "KIT-MAR-400", slug: "kit-mariage-essentiel-50-pers",
    name: "Kit Mariage Sortie de Cérémonie & Fête (50 Invités)",
    short_desc: "50 Cierges 40cm + 1kg Confettis Bio + 24 Tubes à Bulles Cœur + Livre d'or Bois",
    long_desc: "Le pack complet pour une sortie de mairie ou d'église féerique pour 50 invités : 50 cierges magiques 40cm, 1kg de confettis blancs biodégradables solubles à l'eau, 24 tubes à bulles bouchon cœur et 1 livre d'or personnalisé en bois.",
    price_ht: 74.08, price_ttc: 88.90, cost_price: 32.00, stock_qty: 20,
    event_type: "mariage", is_featured: 1, is_active: 1, is_customizable: 1,
    highlights: ["Pack 50 personnes", "Économie de 22€ vs achat séparé", "Livre d'or personnalisé inclus", "Confettis 100% biodégradables"]
  },

  // --- BAPTÊME ---
  {
    id: 28, sku: "BAP-BOUG-030", slug: "bougie-personnalisee-bapteme-verre-ambre-70g",
    name: "Bougies Parfumées Baptême Verre Ambré & Prénom Gravé (Lot de 10)",
    short_desc: "Cire de soja végétale parfum Fleur de Coton, verre ambré apothicaire chic",
    long_desc: "Offrez à vos parrains, marraines et invités un cadeau raffiné qui dure. Bougies de 70g coulées à la main avec de la cire de soja 100% végétale et parfum naturel de Grasse (Fleur de Coton). Étiquette en papier kraft texturé personnalisée avec prénom et date du baptême.",
    price_ht: 32.50, price_ttc: 39.00, cost_price: 14.00, stock_qty: 35,
    event_type: "bapteme", is_featured: 1, is_active: 1, is_customizable: 1,
    highlights: ["Cire 100% végétale soja", "Parfum délicat Fleur de Coton", "Étiquette personnalisée sur-mesure", "Lot de 10 bougies"]
  },
  {
    id: 29, sku: "BAP-DRAG-031", slug: "contenant-dragees-bapteme-plexi-lot-20",
    name: "Boîtes à Dragées Cube Plexiglas Transparent & Ruban (Lot de 20)",
    short_desc: "Cubes 5x5cm haute transparence avec ruban satin & étiquette dorée personnalisée",
    long_desc: "Élégance et modernité pour vos dragées. Boîtes cubiques en plexiglas brillant 5x5cm laissant admirer les dragées colorées. Livrées avec ruban au choix (blanc, sauge, rose poudré, or) et étiquette ronde personnalisée.",
    price_ht: 16.58, price_ttc: 19.90, cost_price: 6.50, stock_qty: 50,
    event_type: "bapteme", is_featured: 1, is_active: 1, is_customizable: 1,
    highlights: ["Plexiglas cristal ultra clair", "Dimensions 5x5x5 cm", "Ruban satin inclus", "Lot de 20 pièces"]
  },
  {
    id: 30, sku: "BAP-FIOLE-032", slug: "fiole-verre-fleurs-sechees-bapteme-lot-15",
    name: "Fioles de Fleurs Séchées & Dragées Baptême (Lot de 15)",
    short_desc: "Tubes en verre avec bouchon liège, mini bouquet séché & étiquette ficelle de lin",
    long_desc: "Une attention bohème et poétique adorée par les invités. Fioles en verre 10cm garnies d'un mini bouquet de fleurs séchées (gypsophile, lagurus, lin) avec bouchon de liège naturel et étiquette gravée.",
    price_ht: 24.08, price_ttc: 28.90, cost_price: 9.00, stock_qty: 40,
    event_type: "bapteme", is_featured: 1, is_active: 1, is_customizable: 1,
    highlights: ["Fleurs séchées naturelles durables", "Verre véritable et liège", "Format fiole 10cm", "Lot de 15 fioles"]
  },
  {
    id: 31, sku: "KIT-BAP-430", slug: "kit-bapteme-20-invites-complet",
    name: "Kit Baptême Bohème & Fleurs Séchées (20 Invités)",
    short_desc: "20 Boîtes dragées + 20 Fioles fleurs séchées + 1 Guirlande dorée + Livre d'or",
    long_desc: "Le pack harmonieux tout-en-un pour un baptême inoubliable de 20 convives : 20 fioles en verre garnies de fleurs séchées, 20 cubes dragées avec étiquette personnalisée, 1 guirlande dorée et 1 livre d'or personnalisé.",
    price_ht: 62.42, price_ttc: 74.90, cost_price: 26.00, stock_qty: 20,
    event_type: "bapteme", is_featured: 1, is_active: 1, is_customizable: 1,
    highlights: ["Pack 20 invités complet", "Matières nobles : bois, verre, lin", "Économie de 18€", "Prêt à installer"]
  },

  // --- NAISSANCE ---
  {
    id: 32, sku: "NAI-AFF-050", slug: "affiche-naissance-personnalisee-prenom-date",
    name: "Affiche de Naissance Personnalisée Épure & Constellation",
    short_desc: "Affiche A3/A4 imprimée sur papier d'art 300g avec prénom, date, heure, poids & taille",
    long_desc: "Créez une œuvre d'art unique pour décorer la chambre de bébé. Typographie délicate, carte du ciel étoilée du jour de la naissance et détails de naissance personnalisés. Imprimée sur papier d'art texturé haut de gamme à Nantes.",
    price_ht: 16.58, price_ttc: 19.90, cost_price: 5.00, stock_qty: 80,
    event_type: "naissance", is_featured: 1, is_active: 1, is_customizable: 1,
    highlights: ["Personnalisation prénom & mensurations", "Papier d'art vergé 300g/m²", "Format A4 ou A3", "Fabriqué en France"],
    variants: [
      { id: 20, sku: "NAI-AFF-A4", name: "Format A4 (21x29.7cm)", attribute_type: "size", attribute_value: "A4", price_ttc: 19.90, stock_qty: 50 },
      { id: 21, sku: "NAI-AFF-A3", name: "Format A3 (30x42cm)", attribute_type: "size", attribute_value: "A3", price_ttc: 24.90, stock_qty: 30 }
    ]
  },
  {
    id: 33, sku: "NAI-GUIR-051", slug: "guirlande-bienvenue-bebe-dore",
    name: "Guirlande Murale Lettrage Doré 'Bienvenue Bébé'",
    short_desc: "Guirlande dorée pailletée 2 mètres avec ruban satin ivoire",
    long_desc: "Une touche dorée festive et douce pour accueillir bébé à son retour de la maternité ou lors d'un goûter de bienvenue.",
    price_ht: 8.25, price_ttc: 9.90, cost_price: 2.20, stock_qty: 60,
    event_type: "naissance", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Lettres dorées pailletées", "Longueur 2 mètres", "Ne perd pas ses paillettes", "Prête à suspendre"]
  },

  // --- BABY SHOWER ---
  {
    id: 34, sku: "BS-KIT-FILLE-060", slug: "kit-deco-baby-shower-fille-70-pieces",
    name: "Kit Décoration Baby Shower Pastel Rose & Terracotta (70 Pièces)",
    short_desc: "Arche ballons 50pcs + Écharpe Future Maman + Bannière Baby Girl + Accessoires",
    long_desc: "Le kit complet clé en main pour célébrer l'arrivée d'une petite fille. Comprend une magnifique arche de ballons dégradés rose poudré et terracotta, l'écharpe en satin 'Mum to Be', la bannière dorée, 10 accessoires photobooth et le ruban de montage.",
    price_ht: 24.92, price_ttc: 29.90, cost_price: 9.50, stock_qty: 45,
    event_type: "baby_shower", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["70 pièces coordonnées", "Écharpe satin incluse", "Nuances douces terracotta", "Montage facile 20 min"]
  },
  {
    id: 35, sku: "BS-KIT-GARC-061", slug: "kit-deco-baby-shower-garcon-70-pieces",
    name: "Kit Décoration Baby Shower Douceur Bleu & Sauge (70 Pièces)",
    short_desc: "Arche ballons 50pcs + Écharpe satin + Bannière Baby Boy + 10 Accessoires photo",
    long_desc: "Tout pour une Baby Shower garçon élégante et apaisante : arche de ballons bleu nuage, vert sauge et blanc satiné, écharpe 'Mum to Be', bannière dorée et kit photobooth.",
    price_ht: 24.92, price_ttc: 29.90, cost_price: 9.50, stock_qty: 45,
    event_type: "baby_shower", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Harmonie bleu & sauge", "Bannière dorée pailletée", "Accessoires photobooth", "70 pièces au total"]
  },

  // --- ANNIVERSAIRE ---
  {
    id: 36, sku: "ANN-LIC-070", slug: "kit-anniversaire-licorne-70pcs",
    name: "Kit Anniversaire Licorne Féerique & Arc-en-Ciel (70 Pièces)",
    short_desc: "Déco complète : Arche ballons pastel, vaisselle licorne 10 enfants, guirlande & topper",
    long_desc: "Un anniversaire magique pour votre enfant sans courir dans 5 magasins. 70 pièces assorties : assiettes et gobelets licorne dorés pour 10 enfants, serviettes, nappe féerique, arche de 40 ballons pastel, guirlande Happy Birthday et cake topper licorne.",
    price_ht: 24.92, price_ttc: 29.90, cost_price: 9.50, stock_qty: 50,
    event_type: "anniversaire", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Pack complet pour 10 enfants", "Vaisselle carton FSC recyclable", "Arche ballons pastel incluse", "Thème licorne doré"]
  },
  {
    id: 37, sku: "ANN-30-071", slug: "kit-anniversaire-30-ans-rose-gold-50pcs",
    name: "Kit Anniversaire 30 Ans Rose Gold & Confettis (50 Pièces)",
    short_desc: "Chiffres géants '30' 86cm + Rideau métallisé + 30 Ballons + Écharpe '30 & Fabulous'",
    long_desc: "Fêtez vos 30 ans avec classe et éclat. Deux ballons chiffres géants '3' et '0' de 86cm gonflables à l'air ou à l'hélium, un grand rideau de fond métallisé rose gold pour vos photos, 30 ballons confettis assortis, une guirlande et l'écharpe pailletée.",
    price_ht: 20.75, price_ttc: 24.90, cost_price: 8.00, stock_qty: 40,
    event_type: "anniversaire", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Chiffres XXL 86cm", "Rideau de scène métallisé", "Écharpe 30 & Fabulous", "Couleur Rose Gold ultra tendance"]
  },
  {
    id: 38, sku: "ANN-DINO-072", slug: "kit-anniversaire-dinosaure-50pcs",
    name: "Kit Anniversaire Dinosaure Safari & Jungle (50 Pièces)",
    short_desc: "Arche ballons vert jungle & or + 4 Ballons dinosaures XXL + Guirlande",
    long_desc: "Embarquez les petits aventuriers dans une jungle jurassique ! Kit comprenant 4 grands ballons dinosaures (T-Rex, Tricératops), 40 ballons vert forêt et or, feuilles tropicales et guirlande d'anniversaire.",
    price_ht: 22.42, price_ttc: 26.90, cost_price: 8.50, stock_qty: 35,
    event_type: "anniversaire", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["4 Dinosaures XXL", "Feuilles tropicales déco", "Arche vert & or", "Pour 10 à 15 enfants"]
  },
  {
    id: 39, sku: "ANN-POTTER-073", slug: "kit-anniversaire-harry-potter-60pcs",
    name: "Kit Anniversaire École des Sorciers & Magie (60 Pièces)",
    short_desc: "Bannières maisons de sorciers, ballons or & bordeaux, cravates et lunettes rondes",
    long_desc: "Plongez vos invités dans la magie de Poudlard ! Kit complet avec fanions aux couleurs des maisons, vaisselle thématique sorcier pour 10 personnes, lunettes rondes, cravates et cake toppers vifs.",
    price_ht: 24.92, price_ttc: 29.90, cost_price: 9.50, stock_qty: 30,
    event_type: "anniversaire", is_featured: 1, is_active: 1, is_customizable: 0,
    highlights: ["Accessoires sorciers inclus", "Vaisselle pour 10 enfants", "Décoration murale immersive", "Ambiance magique garantie"]
  }
];

class InMemoryStore {
  constructor() {
    this.products = [...RAW_PRODUCTS];
    this.carts = new Map();
    this.cartItems = new Map();
    this.orders = new Map();
    this.nextCartItemId = 1;
    this.nextOrderId = 1001;
  }

  getAllProducts() {
    return enrichProducts(this.products);
  }

  getProductById(id) {
    const prod = this.products.find(p => p.id === Number(id));
    return prod ? enrichProduct(prod) : null;
  }

  getProductBySlug(slug) {
    const prod = this.products.find(p => p.slug === slug);
    return prod ? enrichProduct(prod) : null;
  }

  getUniverses() {
    return UNIVERSES.map(u => ({
      ...u,
      product_count: this.products.filter(p => p.event_type === u.id).length
    }));
  }

  getUniverseBySlug(slug) {
    const universe = UNIVERSES.find(u => u.slug === slug || u.id === slug);
    if (!universe) return null;
    return {
      ...universe,
      products: this.filterProducts({ event: universe.id }),
      product_count: this.products.filter(p => p.event_type === universe.id).length
    };
  }

  getFeaturedProducts(limit = 8) {
    const featured = this.products.filter(p => p.is_featured === 1);
    return enrichProducts(featured.slice(0, limit));
  }

  getCustomizableProducts() {
    return enrichProducts(this.products.filter(p => p.is_customizable === 1 || (p.name && p.name.toLowerCase().includes('personnalis'))));
  }

  getKits() {
    return enrichProducts(this.products.filter(p => (p.slug && p.slug.includes('kit')) || (p.name && p.name.includes('Kit')) || p.price_ttc >= 28));
  }

  // Smart Natural Search Parser
  parseNaturalQuery(query) {
    if (!query) return { raw: '', keywords: [], filters: {} };
    const q = query.toLowerCase().trim();
    const extracted = {
      event: null,
      color: null,
      theme: null,
      is_custom: false,
      is_kit: false,
      price_max: null,
      tags: []
    };

    // Events detection
    if (q.includes('mariage') || q.includes('mariés') || q.includes('cérémonie') || q.includes('mairie')) {
      extracted.event = 'mariage';
      extracted.tags.push('Univers Mariage');
    } else if (q.includes('gender reveal') || q.includes('gender') || q.includes('sexe') || q.includes('garçon ou fille') || q.includes('boy or girl')) {
      extracted.event = 'gender_reveal';
      extracted.tags.push('Gender Reveal');
    } else if (q.includes('baby shower') || q.includes('babyshower') || q.includes('future maman')) {
      extracted.event = 'baby_shower';
      extracted.tags.push('Baby Shower');
    } else if (q.includes('naissance') || q.includes('nouveau né') || q.includes('bébé')) {
      extracted.event = 'naissance';
      extracted.tags.push('Naissance');
    } else if (q.includes('bapteme') || q.includes('baptême') || q.includes('parrain') || q.includes('marraine') || q.includes('dragée')) {
      extracted.event = 'bapteme';
      extracted.tags.push('Baptême');
    } else if (q.includes('anniversaire') || q.includes('anniv') || q.includes('ans') || q.includes('bougies')) {
      extracted.event = 'anniversaire';
      extracted.tags.push('Anniversaire');
    }

    // Colors detection
    const colorMap = {
      'rose': 'Rose poudré',
      'bleu': 'Bleu ciel',
      'or': 'Or & Doré',
      'gold': 'Or & Doré',
      'blanc': 'Blanc satiné',
      'terracotta': 'Terracotta',
      'sauge': 'Vert sauge',
      'vert': 'Vert sauge',
      'noir': 'Noir'
    };
    for (const [key, label] of Object.entries(colorMap)) {
      if (q.includes(key)) {
        extracted.color = key;
        extracted.tags.push(label);
        break;
      }
    }

    // Themes
    const themeMap = {
      'licorne': 'Licorne',
      'dino': 'Dinosaure',
      'dinosaure': 'Dinosaure',
      'sorcier': 'Harry Potter',
      'potter': 'Harry Potter',
      'boheme': 'Bohème',
      'bohème': 'Bohème',
      '30 ans': '30 Ans'
    };
    for (const [key, label] of Object.entries(themeMap)) {
      if (q.includes(key)) {
        extracted.theme = key;
        extracted.tags.push(label);
        break;
      }
    }

    // Custom & Kits intent
    if (q.includes('personnalis') || q.includes('prénom') || q.includes('gravé') || q.includes('sur mesure')) {
      extracted.is_custom = true;
      extracted.tags.push('Personnalisation Atelier');
    }
    if (q.includes('kit') || q.includes('pack') || q.includes('complet') || q.includes('tout en un')) {
      extracted.is_kit = true;
      extracted.tags.push('Formule Kit');
    }

    return { raw: query, filters: extracted, tags: extracted.tags };
  }

  intelligentSearchScore(parsedQuery, product) {
    let score = 0;
    const name = (product.name || '').toLowerCase();
    const desc = (product.short_desc || '').toLowerCase() + ' ' + (product.long_desc || '').toLowerCase();
    const event = (product.event_type || '').toLowerCase();
    const slug = (product.slug || '').toLowerCase();
    const raw = typeof parsedQuery === 'string' ? parsedQuery.toLowerCase() : parsedQuery.raw.toLowerCase();
    const filters = typeof parsedQuery === 'object' ? parsedQuery.filters : {};

    if (filters.event && (event === filters.event || name.includes(filters.event))) {
      score += 40;
    }
    if (filters.color && (name.includes(filters.color) || desc.includes(filters.color) || slug.includes(filters.color))) {
      score += 30;
    }
    if (filters.theme && (name.includes(filters.theme) || desc.includes(filters.theme))) {
      score += 30;
    }
    if (filters.is_custom && (product.is_customizable || name.includes('personnalis'))) {
      score += 25;
    }
    if (filters.is_kit && (slug.includes('kit') || name.includes('Kit') || name.includes('Pack'))) {
      score += 25;
    }

    // Direct token matching
    const words = raw.split(/\s+/).filter(w => w.length > 2);
    for (const w of words) {
      if (name.includes(w)) score += 15;
      else if (desc.includes(w)) score += 5;
    }

    if (product.is_featured) score += 5;
    return score;
  }

  searchProducts(query) {
    const all = this.getAllProducts();
    if (!query || !query.trim()) {
      return { products: all.slice(0, 30), parsed: null };
    }
    const parsed = this.parseNaturalQuery(query);
    const scored = [];
    for (const p of all) {
      const s = this.intelligentSearchScore(parsed, p);
      if (s > 0) {
        scored.push({ score: s, product: p });
      }
    }
    scored.sort((a, b) => b.score - a.score);
    return {
      products: scored.map(item => item.product),
      parsed
    };
  }

  filterProducts({ event, filter, q, couleur, theme, age, price_range, custom_only, in_stock_only, sort }) {
    let prods = this.getAllProducts();

    if (event && event !== 'all') {
      if (event === 'kits') {
        prods = prods.filter(p => (p.slug && p.slug.includes('kit')) || (p.name && p.name.includes('Kit')) || p.price_ttc >= 28);
      } else if (event === 'personnalise') {
        prods = prods.filter(p => p.is_customizable === 1 || (p.name && p.name.toLowerCase().includes('personnalis')));
      } else {
        prods = prods.filter(p => p.event_type === event);
      }
    }

    if (filter) {
      if (filter === 'kits') {
        prods = prods.filter(p => (p.slug && p.slug.includes('kit')) || (p.name && p.name.includes('Kit')) || p.price_ttc >= 28);
      } else if (filter === 'perso') {
        prods = prods.filter(p => p.is_customizable === 1 || (p.name && p.name.toLowerCase().includes('personnalis')));
      } else if (filter === 'best-sellers') {
        prods = prods.filter(p => p.is_featured === 1);
      } else if (filter === 'cadeaux') {
        prods = prods.filter(p => p.price_ttc <= 35 && (p.is_customizable || p.event_type === 'bapteme' || p.event_type === 'naissance'));
      }
    }

    if (q) {
      const searchRes = this.searchProducts(q);
      prods = searchRes.products;
    }

    if (couleur) {
      const c = couleur.toLowerCase();
      prods = prods.filter(p => (p.name && p.name.toLowerCase().includes(c)) || (p.slug && p.slug.includes(c)));
    }

    if (theme) {
      const t = theme.toLowerCase();
      prods = prods.filter(p => (p.name && p.name.toLowerCase().includes(t)) || (p.slug && p.slug.includes(t)));
    }

    if (custom_only === '1' || custom_only === true) {
      prods = prods.filter(p => p.is_customizable === 1 || (p.name && p.name.toLowerCase().includes('personnalis')));
    }

    if (in_stock_only === '1' || in_stock_only === true) {
      prods = prods.filter(p => p.stock_qty > 0);
    }

    if (price_range) {
      if (price_range === 'under-15') prods = prods.filter(p => p.price_ttc < 15);
      else if (price_range === '15-30') prods = prods.filter(p => p.price_ttc >= 15 && p.price_ttc <= 30);
      else if (price_range === '30-60') prods = prods.filter(p => p.price_ttc > 30 && p.price_ttc <= 60);
      else if (price_range === 'over-60') prods = prods.filter(p => p.price_ttc > 60);
    }

    // Sorting
    if (sort === 'price-asc') {
      prods.sort((a, b) => a.price_ttc - b.price_ttc);
    } else if (sort === 'price-desc') {
      prods.sort((a, b) => b.price_ttc - a.price_ttc);
    } else if (sort === 'popular') {
      prods.sort((a, b) => (b.is_featured || 0) - (a.is_featured || 0));
    }

    return prods;
  }

  // Cart operations
  getCart(token) {
    if (!token) return null;
    return this.carts.get(token) || null;
  }

  getOrCreateCart(token) {
    if (token && this.carts.has(token)) {
      return this.carts.get(token);
    }
    const cartId = this.carts.size + 1;
    const newToken = token || `cart_${Date.now()}_${Math.random().toString(36).slice(2)}`;
    const cart = { id: cartId, token: newToken, created_at: new Date().toISOString() };
    this.carts.set(newToken, cart);
    return cart;
  }

  getCartItems(cartId) {
    const items = [];
    for (const it of this.cartItems.values()) {
      if (it.cart_id === cartId) {
        const prod = this.getProductById(it.product_id);
        const variant = prod?.variants?.find(v => v.id === it.variant_id);
        items.push({
          ...it,
          name: prod ? prod.name : 'Produit',
          slug: prod ? prod.slug : '',
          image_url: prod ? prod.image_url : '/static/images/01-hero.jpg',
          price_ttc: prod ? prod.price_ttc : it.price_ttc_at_add,
          variant_name: variant ? variant.name : null,
          custom_text: it.custom_text || null
        });
      }
    }
    return items;
  }

  addToCart(cartId, productId, variantId, quantity = 1, customText = '') {
    const prod = this.getProductById(productId);
    if (!prod) return;

    let price = prod.price_ttc;
    if (variantId && prod.variants) {
      const v = prod.variants.find(item => item.id === Number(variantId));
      if (v && v.price_ttc) price = v.price_ttc;
    }

    const key = `${cartId}_${productId}_${variantId || 'null'}_${customText || 'none'}`;
    if (this.cartItems.has(key)) {
      const existing = this.cartItems.get(key);
      existing.quantity += Number(quantity);
    } else {
      const item = {
        id: this.nextCartItemId++,
        cart_id: cartId,
        product_id: Number(productId),
        variant_id: variantId ? Number(variantId) : null,
        quantity: Number(quantity),
        price_ttc_at_add: price,
        custom_text: customText || null
      };
      this.cartItems.set(key, item);
    }
  }

  removeCartItem(cartId, itemId) {
    for (const [key, it] of this.cartItems.entries()) {
      if (it.cart_id === cartId && it.id === Number(itemId)) {
        this.cartItems.delete(key);
        break;
      }
    }
  }

  clearCart(cartId) {
    for (const [key, it] of this.cartItems.entries()) {
      if (it.cart_id === cartId) {
        this.cartItems.delete(key);
      }
    }
  }

  createOrder({ cartId, customerInfo, shippingMethodCode }) {
    const items = this.getCartItems(cartId);
    if (!items.length) return null;

    const totalTtc = items.reduce((acc, it) => acc + it.quantity * it.price_ttc_at_add, 0);
    const ship = SHIPPING_METHODS.find(s => s.code === shippingMethodCode) || SHIPPING_METHODS[0];
    let shippingCost = ship.price_ttc;
    if (ship.free_from && totalTtc >= ship.free_from) shippingCost = 0;

    const orderNumber = `WAOUH-${new Date().getFullYear()}-${Math.floor(100000 + Math.random() * 900000)}`;
    const order = {
      id: this.nextOrderId++,
      number: orderNumber,
      email: customerInfo.email,
      first_name: customerInfo.first_name,
      last_name: customerInfo.last_name,
      phone: customerInfo.phone,
      street: customerInfo.street,
      zip_code: customerInfo.zip_code,
      city: customerInfo.city,
      status: "confirmé",
      total_ht: Math.round((totalTtc / 1.2) * 100) / 100,
      total_tva: Math.round((totalTtc - (totalTtc / 1.2)) * 100) / 100,
      total_ttc: Math.round((totalTtc + shippingCost) * 100) / 100,
      shipping_cost_ttc: shippingCost,
      shipping_method: ship,
      shipping_method_code: shippingMethodCode,
      created_at: new Date().toISOString(),
      items: items.map(it => ({ ...it }))
    };

    // Decrement stock
    for (const it of items) {
      const prod = this.getProductById(it.product_id);
      if (prod) prod.stock_qty = Math.max(0, prod.stock_qty - it.quantity);
    }

    this.orders.set(orderNumber, order);
    this.clearCart(cartId);
    return order;
  }

  getOrder(number) {
    return this.orders.get(number) || null;
  }

  getAdminStats() {
    const products = this.getAllProducts();
    const eventCounts = {};
    for (const p of products) {
      if (p.event_type) {
        eventCounts[p.event_type] = (eventCounts[p.event_type] || 0) + 1;
      }
    }
    const by_event = Object.entries(eventCounts).map(([ev, count]) => {
      const matching = products.filter(p => p.event_type === ev);
      const avg = matching.reduce((a, b) => a + (b.price_ttc || 0), 0) / (matching.length || 1);
      return { event_type: ev, c: count, avg_price: Math.round(avg * 10) / 10 };
    });

    return {
      nb_products: products.length,
      nb_cats: UNIVERSES.length,
      stock_alert: products.filter(p => p.stock_qty < 10).length,
      featured: products.filter(p => p.is_featured === 1).length,
      kits: products.filter(p => (p.slug && p.slug.includes('kit')) || (p.name && p.name.includes('Kit'))).length,
      by_event
    };
  }
}

export const store = new InMemoryStore();
