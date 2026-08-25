-- SEED PRODUITS NAISSANCE + MARIAGE VENTE (consommables)
-- Marge cible x3 à x4

-- ===== NAISSANCE =====
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('NAIS-GUIR-011', 'guirlande-bienvenue-bebe-dore', 'Guirlande Bienvenue Bébé Dorée', 'Guirlande paillettes or 2m', 6.58, 7.90, 1.8, 60, 'naissance', 1),
('NAIS-BALL-LET-012', 'ballons-lettres-baby-dore-40cm', 'Ballons Lettres BABY Doré 40cm', 'Ballons foil BABY + hélium', 10.75, 12.90, 3.2, 50, 'naissance', 1),
('NAIS-LIVRE-OR-013', 'livre-or-naissance-bebe', 'Livre d''Or Naissance Bébé', 'Livre 80 pages kraft', 12.42, 14.90, 4.5, 30, 'naissance', 0),
('NAIS-KIT-EMPR-014', 'kit-empreintes-bebe-argile', 'Kit Empreintes Bébé Argile', 'Kit empreinte main/pied + cadre', 14.08, 16.90, 5, 35, 'naissance', 1),
('NAIS-BOITE-SOUV-015', 'boite-souvenirs-bebe-personnalisable', 'Boîte à Souvenirs Bébé', 'Boîte bois avec compartiments', 19.08, 22.90, 7, 20, 'naissance', 0),
('NAIS-BALLON-BULLE-016', 'ballon-bulle-personnalisable-naissance', 'Ballon Bulle Personnalisable Naissance', 'Ballon transparent 60cm + confettis + prénom', 15.75, 18.90, 5, 25, 'naissance', 0);

INSERT OR IGNORE INTO product_categories(product_id, category_id) VALUES
((SELECT id FROM products WHERE sku='NAIS-GUIR-011'), (SELECT id FROM categories WHERE slug='naissance-annonce')),
((SELECT id FROM products WHERE sku='NAIS-BALL-LET-012'), (SELECT id FROM categories WHERE slug='naissance-annonce')),
((SELECT id FROM products WHERE sku='NAIS-LIVRE-OR-013'), (SELECT id FROM categories WHERE slug='naissance-livre-or')),
((SELECT id FROM products WHERE sku='NAIS-KIT-EMPR-014'), (SELECT id FROM categories WHERE slug='naissance-souvenir')),
((SELECT id FROM products WHERE sku='NAIS-BOITE-SOUV-015'), (SELECT id FROM categories WHERE slug='naissance-souvenir'));

-- ===== MARIAGE VENTE (consommables à forte marge) =====
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_consumable, is_featured) VALUES
('MAR-CIERGE-020', 'cierges-magiques-lot-50-40cm', 'Cierges Magiques 40cm - Lot de 50', 'Cierges magiques extra longs 40cm, 4min', 'Lot de 50 cierges magiques 40cm, durée 4 minutes, sans fumée. Pour sortie église ou fin de soirée extérieur. Le produit le plus rentable mariage : achat 0.18€, vente 0.60€. Avec consigne sécurité.', 24.08, 28.90, 9, 100, 'mariage', 1, 1),
('MAR-CIERGE-021', 'cierges-magiques-lot-100-40cm', 'Cierges Magiques 40cm - Lot de 100', 'Lot 100 cierges magiques 40cm', 'Lot de 100 cierges magiques 40cm. Economique pour 80-100 invités. Emballage individuel.', 40.75, 48.90, 18, 80, 'mariage', 1, 1),
('MAR-CONFET-BIO-022', 'confettis-biodegradables-blanc-lot-1kg', 'Confettis Biodégradables Blancs 1kg', 'Confettis ronds blancs biodégradables', '1kg de confettis ronds blancs 2cm papier de soie biodégradable. Pour 50 personnes sortie mairie. Se dissout à la pluie. Norme ERP OK.', 16.58, 19.90, 5, 60, 'mariage', 1, 0),
('MAR-BULLES-023', 'bulles-mariage-tubes-lot-24', 'Tubes à Bulles Mariage - Lot de 24', 'Tubes bulles avec coeur, lot 24', 'Lot 24 tubes à bulles 10cm avec bouchon coeur. Pour sortie mairie enfants. Liquide inclus.', 12.42, 14.90, 4, 70, 'mariage', 1, 0),
('MAR-PETALES-024', 'petales-roses-sechees-blanc-1L', 'Pétales de Roses Séchées Blanc 1L', 'Pétales naturels séchés 1L', 'Pétales de roses blanches séchées naturelles, 1 litre = ~ 150g. Parfum léger. Pour sortie mairie ou déco table.', 14.08, 16.90, 5, 40, 'mariage', 1, 0),
('MAR-LIVRE-OR-025', 'livre-or-mariage-bois-personnalisable', 'Livre d''Or Mariage Bois Personnalisable', 'Livre d''or bois gravé Mr & Mrs', 'Livre d''or en bois clair 30x30cm avec gravure Mr & Mrs + date (personnalisable). 50 pages kraft. Couvercle magnétique.', 29.08, 34.90, 11, 20, 'mariage', 0, 1),
('MAR-URNE-026', 'urne-mariage-bois-acrylique', 'Urne Mariage Bois & Acrylique', 'Urne cagnotte mariage transparente', 'Urne mariage 25x25x25cm bois et plexi transparent avec fente et serrure. Gravure personnalisable en option.', 32.42, 38.90, 12, 15, 'mariage', 0, 0),
('MAR-NEON-027', 'neon-mr-mrs-led-60cm', 'Néon LED Mr & Mrs 60cm - VENTE', 'Néon LED blanc chaud 60cm', 'Néon LED Mr & Mrs 60cm blanc chaud, dimmable, alimentation incluse. Achat revente : vous le gardez après mariage. Marge 60%. Support inclus.', 74.08, 88.90, 32, 10, 'mariage', 0, 1);

-- CATEGORIES LIENS
INSERT OR IGNORE INTO product_categories(product_id, category_id) VALUES
((SELECT id FROM products WHERE sku='MAR-CIERGE-020'), (SELECT id FROM categories WHERE slug='mariage-cierges')),
((SELECT id FROM products WHERE sku='MAR-CIERGE-021'), (SELECT id FROM categories WHERE slug='mariage-cierges')),
((SELECT id FROM products WHERE sku='MAR-CONFET-BIO-022'), (SELECT id FROM categories WHERE slug='mariage-confettis')),
((SELECT id FROM products WHERE sku='MAR-BULLES-023'), (SELECT id FROM categories WHERE slug='mariage-sortie-mairie')),
((SELECT id FROM products WHERE sku='MAR-LIVRE-OR-025'), (SELECT id FROM categories WHERE slug='mariage-livre-or')),
((SELECT id FROM products WHERE sku='MAR-NEON-027'), (SELECT id FROM categories WHERE slug='mariage-deco-lumineuse'));

-- ===== BABY SHOWER =====
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('BS-KIT-FILLE-030', 'kit-deco-baby-shower-fille-70-pieces', 'Kit Déco Baby Shower Fille 70 pièces', 'Kit rose gold complet', 20.75, 24.90, 8, 30, 'baby_shower', 1),
('BS-KIT-GARCON-031', 'kit-deco-baby-shower-garcon-70-pieces', 'Kit Déco Baby Shower Garçon 70 pièces', 'Kit bleu gold complet', 20.75, 24.90, 8, 30, 'baby_shower', 1),
('BS-JEU-PRONO-032', 'cartes-pronostics-baby-shower-lot-20', 'Cartes Pronostics Baby Shower - Lot 20', 'Cartes à remplir date/poids/prénom', 6.58, 7.90, 1.8, 50, 'baby_shower', 0);

-- ===== PACKS COMBINÉS =====
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_consumable, is_featured) VALUES
('PACK-GR-ESSENT-040', 'pack-gender-reveal-essentiel', 'Pack Gender Reveal Essentiel', 'Ballon 90cm + 2 fumigènes + 3 canons + cartes', 'Pack essentiel gender reveal : 1 ballon éclatable 90cm + 2 fumigènes (couleur choisie) + 3 canons confettis 30cm + 10 cartes à gratter + 100g poudre Holi. Economie 15% vs achat séparé. Le pack le plus vendu.', 37.42, 44.90, 15, 40, 'gender_reveal', 1, 1),
('PACK-GR-FETE-041', 'pack-gender-reveal-fete-20-personnes', 'Pack Gender Reveal Fête 20 personnes', 'Kit complet déco + animations pour 20 invités', 'Pack fête 20 pers : arche ballons 85pcs + ballon éclatable + 2 fumigènes + 6 canons + 20 cartes pronostics + guirlande + confettis 200g. Tout pour une fête.', 70.75, 84.90, 32, 20, 'gender_reveal', 1, 1),
('PACK-MARIAGE-SORTIE-042', 'pack-sortie-mairie-50-personnes', 'Pack Sortie de Mairie 50 personnes - VENTE', '50 cierges + 1kg confettis + 24 bulles', 'Pack vente sortie mairie 50 pers : 50 cierges magiques 40cm + 1kg confettis biodégradables blancs + 24 tubes bulles. Prix coûtant ~ 18€, vente 49.90€ = marge 64%.', 41.58, 49.90, 18, 50, 'mariage', 1, 1);
