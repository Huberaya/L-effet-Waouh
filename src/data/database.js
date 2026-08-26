import crypto from 'crypto';

// Mapping direct slug -> image file
const IMAGE_MAPPING = {
  // Gender Reveal
  "ballon-eclatable-gender-reveal-90cm": "products/gender-reveal-ballon-90cm-rose.jpg",
  "fumigenes-couleur-rose-bleu-lot-2": "products/gender-reveal-fumigenes-rose-bleu.jpg",
  "canon-confettis-gender-reveal-30cm": "products/gender-reveal-canon-confettis.jpg",
  "boite-surprise-gender-reveal-ballons": "products/gender-reveal-boite-surprise.jpg",
  "kit-arche-ballons-gender-reveal-85-pieces": "products/gender-reveal-arche-85pcs.jpg",
  "kit-gender-reveal-premium-30-pers": "products/gender-reveal-arche-85pcs.jpg",
  
  // Mariage
  "arche-ballons-mariage-blanc-or-200pcs": "products/mariage-arche-blanc-or-200pcs.jpg",
  "rideau-lumineux-led-3x3m-chaud": "products/mariage-rideau-led-3x3m.jpg",
  "lettres-lumineuses-love-40cm": "products/mariage-lettres-love-40cm.jpg",
  "cierges-magiques-lot-50-40cm": "products/mariage-cierges-magiques-40cm.jpg",
  "livre-or-mariage-bois-personnalisable": "products/affiche-personnalisee-prenom.jpg",
  "neon-mr-mrs-led-60cm": "04-neon-v1.jpg",
  "kit-mariage-essentiel-50-pers": "products/kit-mariage-50-pers.jpg",

  // Bapteme
  "bougie-personnalisee-bapteme-verre-ambre-70g": "products/bapteme-bougie-verre-ambre-real-web.jpg",
  "contenant-dragees-bapteme-plexi-lot-20": "products/bapteme-contenant-dragees-plexi-real-web.jpg",
  "fiole-verre-fleurs-sechees-bapteme-lot-15": "products/bapteme-fiole-fleurs-sechees.jpg",
  "kit-bapteme-20-invites-complet": "products/kit-bapteme-20-invites.jpg",

  // Naissance
  "affiche-naissance-personnalisee-prenom-date": "products/naissance-affiche-personnalisee.jpg",
  "guirlande-bienvenue-bebe-dore": "products/naissance-guirlande-bienvenue-real-web.jpg",

  // Baby Shower
  "kit-deco-baby-shower-fille-70-pieces": "products/baby-shower-kit-fille-70pcs-real-web.jpg",
  "kit-deco-baby-shower-garcon-70-pieces": "products/baby-shower-kit-garcon-70pcs.jpg",

  // Anniversaire
  "kit-anniversaire-licorne-70pcs": "products/anniversaire-licorne-70pcs-real-web.jpg",
  "kit-anniversaire-30-ans-rose-gold-50pcs": "products/anniversaire-30-ans-rose-gold.jpg",
  "kit-anniversaire-dinosaure-50pcs": "products/anniversaire-dinosaure-50pcs.jpg",
  "kit-anniversaire-harry-potter-60pcs": "products/anniversaire-harry-potter-60pcs.jpg"
};

const LIFESTYLE_GALLERY_BY_EVENT = {
  mariage: [
    { url: "/static/images/09-premiere-danse-v1.jpg", caption: "Ouverture de bal & haie d'honneur aux cierges 40cm" },
    { url: "/static/images/05-cierges-magiques-v1.jpg", caption: "Cliché des invités et étincelles dorées sans fumée" },
    { url: "/static/images/04-neon-v1.jpg", caption: "Coin Photobooth & lettrage LED chaleureux" }
  ],
  gender_reveal: [
    { url: "/static/images/products/gender-reveal-ballon-90cm-rose.jpg", caption: "L'instant où le ballon éclate et libère les confettis" },
    { url: "/static/images/products/gender-reveal-fumigenes-rose-bleu.jpg", caption: "Fumée rose intense 60s en extérieur" },
    { url: "/static/images/products/gender-reveal-arche-85pcs.jpg", caption: "Décor de table d'accueil Boy or Girl" }
  ],
  baby_shower: [
    { url: "/static/images/products/baby-shower-kit-fille-70pcs-real-web.jpg", caption: "Bar à douceurs et arche pastel terracotta" },
    { url: "/static/images/products/baby-shower-kit-garcon-70pcs.jpg", caption: "Ambiance cocooning bleu sauge & or" }
  ],
  naissance: [
    { url: "/static/images/products/naissance-affiche-personnalisee.jpg", caption: "Affiche encadrée dans la chambre de bébé" },
    { url: "/static/images/products/naissance-guirlande-bienvenue-real-web.jpg", caption: "Guirlande dorée au retour de la maternité" }
  ],
  bapteme: [
    { url: "/static/images/products/bapteme-bougie-verre-ambre-real-web.jpg", caption: "Bougie souvenir allumée sur table des invités" },
    { url: "/static/images/products/bapteme-fiole-fleurs-sechees.jpg", caption: "Fioles de fleurs séchées & dragées d'exception" }
  ],
  anniversaire: [
    { url: "/static/images/products/anniversaire-licorne-70pcs-real-web.jpg", caption: "Goûter d'anniversaire féerique" },
    { url: "/static/images/products/anniversaire-30-ans-rose-gold.jpg", caption: "Soirée 30 ans avec chiffres géants & rideau métallisé" }
  ]
};

const SAMPLE_REVIEWS = [
  { author: "Camille D.", rating: 5, date: "Il y a 3 jours", text: "Effet waouh garanti ! Livré en 24h chrono à Nantes, les cierges 40cm ont duré toute notre ouverture de bal. Les photos sont magiques.", verified: true },
  { author: "Maxime & Laura", rating: 5, date: "Il y a 1 semaine", text: "Le ballon 90cm était 100% opaque, aucun suspense gâché ! L'explosion de confettis roses a fait pleurer toute la famille. Merci !", verified: true },
  { author: "Sophie B.", rating: 5, date: "Il y a 2 semaines", text: "La bougie en verre ambré personnalisée pour le baptême de notre fils est sublime. Odeur fleur de coton très douce et gravure parfaite.", verified: true },
  { author: "Aurélie M.", rating: 5, date: "Il y a 3 semaines", text: "Kit arche de ballons très simple à monter avec le ruban fourni. Rendu digne d'une décoratrice professionnelle !", verified: true }
];

export function getProductImage(product) {
  const slug = product.slug || '';
  if (IMAGE_MAPPING[slug]) {
    return `/static/images/${IMAGE_MAPPING[slug]}`;
  }
  return "/static/images/01-hero.jpg";
}

export function enrichProduct(product) {
  const p = { ...product };
  p.image_url = getProductImage(p);
  
  // Gallery images
  const gallery = [{ url: p.image_url, caption: p.name }];
  if (LIFESTYLE_GALLERY_BY_EVENT[p.event_type]) {
    for (const item of LIFESTYLE_GALLERY_BY_EVENT[p.event_type]) {
      if (item.url !== p.image_url) {
        gallery.push(item);
      }
    }
  }
  p.gallery = gallery;

  // Pricing & margin
  p.compare_at_price = p.compare_at_price || (p.price_ttc ? Math.round((p.price_ttc * 1.25) * 10) / 10 : 0);
  p.savings = Math.max(0, Math.round((p.compare_at_price - p.price_ttc) * 10) / 10);
  p.marge = p.price_ttc ? Math.round(((p.price_ttc - (p.cost_price || 0)) / p.price_ttc) * 100 * 10) / 10 : 65;

  // Rating & social proof
  p.rating = 4.9;
  p.review_count = 18 + (p.id * 7) % 45;
  p.reviews = SAMPLE_REVIEWS;

  return p;
}

export function enrichProducts(products) {
  if (!products) return [];
  if (products.products && Array.isArray(products.products)) {
    return products.products.map(enrichProduct);
  }
  if (!Array.isArray(products)) return [];
  return products.map(enrichProduct);
}
