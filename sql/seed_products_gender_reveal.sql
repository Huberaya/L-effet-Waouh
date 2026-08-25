-- SEED PRODUITS GENDER REVEAL - 20 PRODUITS BEST-SELLERS 2026
-- Prix basés sur achat Aliexpress/Amazon + marge x3/x4

-- 1. Ballon éclatable 90cm
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, tva_rate, cost_price, stock_qty, weight_grams, event_type, is_consumable, is_featured) VALUES
('GR-BAL-90-001', 'ballon-eclatable-gender-reveal-90cm', 'Ballon Éclatable Gender Reveal 90cm + Confettis', 'Ballon noir 90cm avec confettis rose ou bleu inclus', 'Le best-seller absolu gender reveal. Ballon latex géant noir opaque 90cm (36 pouces) + 2 sachets de confettis (rose OU bleu au choix) + paille. A éclater avec une épingle pour révéler la couleur. Vendu avec notice. Biodégradable.', 8.33, 10.00, 20, 2.5, 150, 200, 'gender_reveal', 1, 1);

INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty) VALUES
((SELECT id FROM products WHERE sku='GR-BAL-90-001'), 'GR-BAL-90-001-ROSE', 'Rose - Fille', 'color', 'rose', 10.00, 80),
((SELECT id FROM products WHERE sku='GR-BAL-90-001'), 'GR-BAL-90-001-BLEU', 'Bleu - Garçon', 'color', 'bleu', 10.00, 70);

INSERT OR IGNORE INTO product_categories(product_id, category_id) VALUES
((SELECT id FROM products WHERE sku='GR-BAL-90-001'), (SELECT id FROM categories WHERE slug='gender-ballon')),
((SELECT id FROM products WHERE sku='GR-BAL-90-001'), (SELECT id FROM categories WHERE slug='gender-reveal'));

-- 2. Fumigènes couleur (lot 2)
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, weight_grams, event_type, is_consumable, is_featured) VALUES
('GR-FUM-002', 'fumigenes-couleur-rose-bleu-lot-2', 'Fumigènes Couleur Gender Reveal - Lot de 2', 'Fumigènes 60s rose ou bleu, allumage goupille', 'Fumigènes à main 60 secondes, couleur intense rose ou bleu. Idéal photo extérieur. Vendus par lot de 2. Catégorie T1 (vente libre +18 ans). Durée 60s, portée 3m. Attention usage extérieur uniquement.', 12.42, 14.90, 4.0, 80, 400, 'gender_reveal', 1, 1);

INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty) VALUES
((SELECT id FROM products WHERE sku='GR-FUM-002'), 'GR-FUM-002-ROSE', 'Rose x2', 'color', 'rose', 14.90, 40),
((SELECT id FROM products WHERE sku='GR-FUM-002'), 'GR-FUM-002-BLEU', 'Bleu x2', 'color', 'bleu', 14.90, 40),
((SELECT id FROM products WHERE sku='GR-FUM-002'), 'GR-FUM-002-MIX', 'Pack Mixte 1 Rose + 1 Bleu (photos)', 'color', 'mixte', 14.90, 20);

INSERT OR IGNORE INTO product_categories(product_id, category_id) VALUES
((SELECT id FROM products WHERE sku='GR-FUM-002'), (SELECT id FROM categories WHERE slug='gender-fumigene'));

-- 3. Canon à confettis 30cm
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_consumable, is_featured) VALUES
('GR-CAN-30-003', 'canon-confettis-gender-reveal-30cm', 'Canon à Confettis Gender Reveal 30cm', 'Canon confettis rose ou bleu, tube 30cm', 'Canon à main 30cm, confettis rectangulaires rose ou bleu. Portée 6-8m. Sans résidu plastique. Lot de 1, 3 ou 6 pour effet waouh. Le plus vendu après le ballon.', 3.25, 3.90, 0.9, 300, 'gender_reveal', 1, 1);

INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty) VALUES
((SELECT id FROM products WHERE sku='GR-CAN-30-003'), 'GR-CAN-30-003-ROSE-X1', 'Rose x1', 'pack_qty', 'x1-rose', 3.90, 100),
((SELECT id FROM products WHERE sku='GR-CAN-30-003'), 'GR-CAN-30-003-BLEU-X1', 'Bleu x1', 'pack_qty', 'x1-bleu', 3.90, 100),
((SELECT id FROM products WHERE sku='GR-CAN-30-003'), 'GR-CAN-30-003-ROSE-X3', 'Rose x3 (-10%)', 'pack_qty', 'x3-rose', 10.50, 50),
((SELECT id FROM products WHERE sku='GR-CAN-30-003'), 'GR-CAN-30-003-BLEU-X3', 'Bleu x3 (-10%)', 'pack_qty', 'x3-bleu', 10.50, 50),
((SELECT id FROM products WHERE sku='GR-CAN-30-003'), 'GR-CAN-30-003-MIX-X6', 'Pack fête x6 (3 rose + 3 bleu)', 'pack_qty', 'x6-mix', 19.90, 30);

-- 4. Boîte surprise
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('GR-BOX-004', 'boite-surprise-gender-reveal-ballons', 'Boîte Surprise Gender Reveal à Ballons', 'Boîte blanche 60cm avec ballons hélium rose/bleu à l''intérieur', 'Boîte cartonnée blanche 60x60x60cm + 5 ballons latex rose ou bleu gonflés à l''hélium (non inclus, à gonfler) + papier de soie. Effet ouverture waouh garanti pour vidéo. Réutilisable.', 20.75, 24.90, 8, 25, 'gender_reveal', 1);

-- 5. Cartes à gratter
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_consumable) VALUES
('GR-GRAT-005', 'cartes-a-gratter-boy-or-girl-lot-10', 'Cartes à Gratter Boy or Girl - Lot de 10', 'Cartes à gratter pour annoncer le sexe à la famille', 'Lot de 10 cartes kraft 10x15cm avec zone à gratter. Sous la zone : IT''S A BOY ou IT''S A GIRL (au choix à la commande). Enveloppes incluses. Idéal pour annoncer aux grands-parents.', 8.25, 9.90, 2.2, 100, 'gender_reveal', 1);

INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty) VALUES
((SELECT id FROM products WHERE sku='GR-GRAT-005'), 'GR-GRAT-005-ROSE', 'Fille - It''s a Girl x10', 'color', 'rose', 9.90, 50),
((SELECT id FROM products WHERE sku='GR-GRAT-005'), 'GR-GRAT-005-BLEU', 'Garçon - It''s a Boy x10', 'color', 'bleu', 9.90, 50);

-- 6. Poudre Holi
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_consumable) VALUES
('GR-HOLI-006', 'poudre-holi-rose-bleu-100g', 'Poudre Holi Rose / Bleu 100g', 'Poudre colorée pour lancer gender reveal', 'Poudre Holi naturelle à base de fécule de maïs, couleur rose ou bleu. Sachet 100g = 1 à 2 lancers. Pour photos. Lavable. Non toxique.', 2.42, 2.90, 0.6, 200, 'gender_reveal', 1);

-- 7. Kit arche ballons gender reveal
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('GR-KIT-ARCHE-007', 'kit-arche-ballons-gender-reveal-85-pieces', 'Kit Arche Ballons Gender Reveal 85 pièces', 'Arche complète rose/bleu/blanc/doré + guirlande Boy or Girl', 'Kit 85 pièces : 40 ballons pastel rose/bleu, 20 blancs, 10 dorés confettis, 5 ballons foil Boy or Girl, guirlande, ruban, arche. Sans hélium. Notice montage incluse. Best-seller déco.', 24.08, 28.90, 9, 40, 'gender_reveal', 1);

-- 8. Bougie magique
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_consumable) VALUES
('GR-BOUGIE-008', 'bougie-magique-gender-reveal-flamme-couleur', 'Bougie Magique Flamme Couleur Gender Reveal', 'Bougie qui s''allume en rose ou bleu', 'Bougie gâteau 12cm avec flamme colorée rose ou bleu pendant 20s. Effet surprise pour couper le gâteau. Lot de 1.', 4.08, 4.90, 1.1, 80, 'gender_reveal', 1);

-- 9. Pinata gender reveal
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('GR-PINATA-009', 'pinata-gender-reveal-point-interrogation', 'Pinata Gender Reveal Point d''Interrogation', 'Pinata à casser avec confettis rose/bleu', 'Pinata carton 45cm forme point d''interrogation + bâton + confettis rose/bleu (au choix) + bonbons. A remplir. Vidéo TikTok garantie.', 20.75, 24.90, 7, 15, 'gender_reveal');

-- 10. Confettis biodégradables rose/bleu 100g
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_consumable) VALUES
('GR-CONFET-010', 'confettis-biodegradables-rose-bleu-100g', 'Confettis Biodégradables Rose/Bleu 100g', 'Confettis ronds papier de soie 2cm', 'Confettis ronds 2cm papier de soie biodégradable, rose ou bleu. Sachet 100g = ~ 800 confettis. Pour canon, ballon, table.', 3.25, 3.90, 0.8, 150, 'gender_reveal', 1);
