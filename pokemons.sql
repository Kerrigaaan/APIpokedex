-- Créer la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS pokedex;

-- Utiliser la base de données
USE pokedex;

-- Créer la table pour les Pokémon
CREATE TABLE IF NOT EXISTS pokemon (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    hp INT,
    attack INT,
    defense INT,
    sp_attack INT,
    sp_defense INT,
    speed INT,
    image_url VARCHAR(255)
);

-- Créer la table pour les types de Pokémon
CREATE TABLE IF NOT EXISTS type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(50) UNIQUE
);

-- Créer la table de relation entre Pokémon et types
CREATE TABLE IF NOT EXISTS pokemon_type (
    pokemon_id INT,
    type_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (type_id) REFERENCES type(id),
    PRIMARY KEY (pokemon_id, type_id)
);

-- Créer la table pour les capacités de Pokémon
CREATE TABLE IF NOT EXISTS ability (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ability VARCHAR(50) UNIQUE
);

-- Créer la table de relation entre Pokémon et capacités
CREATE TABLE IF NOT EXISTS pokemon_ability (
    pokemon_id INT,
    ability_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (ability_id) REFERENCES ability(id),
    PRIMARY KEY (pokemon_id, ability_id)
);

-- Insérer des données de base pour les Pokémon
INSERT INTO pokemon (id, name, hp, attack, defense, sp_attack, sp_defense, speed, image_url) VALUES
(1, 'Bulbasaur', 45, 49, 49, 65, 65, 45, '/images/1.png'),
(2, 'Ivysaur', 60, 62, 63, 80, 80, 60, '/images/2.png'),
(3, 'Venusaur', 80, 82, 83, 100, 100, 80, '/images/3.png'),
(4, 'Charmander', 39, 52, 43, 60, 50, 65, '/images/4.png'),
(5, 'Charmeleon', 58, 64, 58, 80, 65, 80, '/images/5.png'),
(6, 'Charizard', 78, 84, 78, 109, 85, 100, '/images/6.png'),
(7, 'Squirtle', 44, 48, 65, 50, 64, 43, '/images/7.png'),
(8, 'Wartortle', 59, 63, 80, 65, 80, 58, '/images/8.png'),
(9, 'Blastoise', 79, 83, 100, 85, 105, 78, '/images/9.png'),
(10, 'Caterpie', 45, 30, 35, 20, 20, 45, '/images/10.png'),
(11, 'Metapod', 50, 20, 55, 25, 25, 30, '/images/11.png'),
(12, 'Butterfree', 60, 45, 50, 90, 80, 70, '/images/12.png'),
(13, 'Weedle', 40, 35, 30, 20, 20, 50, '/images/13.png'),
(14, 'Kakuna', 45, 25, 50, 25, 25, 35, '/images/14.png'),
(15, 'Beedrill', 65, 90, 40, 45, 80, 75, '/images/15.png'),
(16, 'Pidgey', 40, 45, 40, 35, 35, 56, '/images/16.png'),
(17, 'Pidgeotto', 63, 60, 55, 50, 50, 71, '/images/17.png'),
(18, 'Pidgeot', 83, 80, 75, 70, 70, 101, '/images/18.png'),
(19, 'Rattata', 30, 56, 35, 25, 35, 72, '/images/19.png'),
(20, 'Raticate', 55, 81, 60, 50, 70, 97, '/images/20.png'),
(21, 'Spearow', 40, 60, 30, 31, 31, 70, '/images/21.png'),
(22, 'Fearow', 65, 90, 65, 61, 61, 100, '/images/22.png'),
(23, 'Ekans', 35, 60, 44, 40, 54, 55, '/images/23.png'),
(24, 'Arbok', 60, 95, 69, 65, 79, 80, '/images/24.png'),
(25, 'Pikachu', 35, 55, 40, 50, 50, 90, '/images/25.png'),
(26, 'Raichu', 60, 90, 55, 90, 80, 110, '/images/26.png'),
(27, 'Sandshrew', 50, 75, 85, 20, 30, 40, '/images/27.png'),
(28, 'Sandslash', 75, 100, 110, 45, 55, 65, '/images/28.png'),
(29, 'Nidoran♀', 55, 47, 52, 40, 40, 41, '/images/29.png'),
(30, 'Nidorina', 70, 62, 67, 55, 55, 56, '/images/30.png'),
(31, 'Nidoqueen', 90, 92, 87, 75, 85, 76, '/images/31.png'),
(32, 'Nidoran♂', 46, 57, 40, 40, 40, 50, '/images/32.png'),
(33, 'Nidorino', 61, 72, 57, 55, 55, 65, '/images/33.png'),
(34, 'Nidoking', 81, 102, 77, 85, 75, 85, '/images/34.png'),
(35, 'Clefairy', 70, 45, 48, 60, 65, 35, '/images/35.png'),
(36, 'Clefable', 95, 70, 73, 95, 90, 60, '/images/36.png'),
(37, 'Vulpix', 38, 41, 40, 50, 65, 65, '/images/37.png'),
(38, 'Ninetales', 73, 76, 75, 81, 100, 100, '/images/38.png'),
(39, 'Jigglypuff', 115, 45, 20, 45, 25, 20, '/images/39.png'),
(40, 'Wigglytuff', 140, 70, 45, 85, 50, 45, '/images/40.png');

-- Insérer des types de Pokémon
INSERT INTO type (type) VALUES ('Grass'), ('Poison'), ('Fire'), ('Flying'), ('Water'), ('Bug'), ('Normal'), ('Electric'), ('Ground'), ('Fairy');

-- Insérer des capacités de Pokémon
INSERT INTO ability (ability) VALUES 
('Overgrow'), ('Chlorophyll'), ('Blaze'), ('Solar Power'), ('Torrent'), ('Rain Dish'), ('Shield Dust'), ('Run Away'), 
('Shed Skin'), ('Compound Eyes'), ('Tinted Lens'), ('Swarm'), ('Sniper'), ('Keen Eye'), ('Tangled Feet'), ('Big Pecks'), 
('Guts'), ('Hustle'), ('Intimidate'), ('Unnerve'), ('Static'), ('Lightning Rod'), ('Sand Veil'), ('Sand Rush'), 
('Poison Point'), ('Rivalry'), ('Sheer Force'), ('Cute Charm'), ('Magic Guard'), ('Friend Guard'), ('Unaware'), 
('Flash Fire'), ('Drought'), ('Competitive'), ('Frisk');

-- Insérer des relations entre Pokémon et types
INSERT INTO pokemon_type (pokemon_id, type_id)
SELECT p.id, t.id FROM pokemon p JOIN type t ON 
(p.id IN (1, 2, 3) AND t.type = 'Grass') OR 
(p.id IN (1, 2, 3, 13, 14, 15, 29, 30, 31, 32, 33, 34) AND t.type = 'Poison') OR 
(p.id IN (4, 5, 6, 37, 38) AND t.type = 'Fire') OR 
(p.id IN (6, 12, 16, 17, 18, 21, 22) AND t.type = 'Flying') OR 
(p.id IN (7, 8, 9) AND t.type = 'Water') OR 
(p.id IN (10, 11, 12, 13, 14, 15) AND t.type = 'Bug') OR 
(p.id IN (16, 17, 18, 19, 20, 21, 22, 39, 40) AND t.type = 'Normal') OR 
(p.id IN (25, 26) AND t.type = 'Electric') OR 
(p.id IN (27, 28, 31, 34) AND t.type = 'Ground') OR 
(p.id IN (35, 36, 39, 40) AND t.type = 'Fairy');

-- Insérer des relations entre Pokémon et capacités
INSERT INTO pokemon_ability (pokemon_id, ability_id)
SELECT p.id, a.id FROM pokemon p JOIN ability a ON 
(p.id = 1 AND a.ability IN ('Overgrow', 'Chlorophyll')) OR 
(p.id = 2 AND a.ability IN ('Overgrow', 'Chlorophyll')) OR 
(p.id = 3 AND a.ability IN ('Overgrow', 'Chlorophyll')) OR 
(p.id = 4 AND a.ability IN ('Blaze', 'Solar Power')) OR 
(p.id = 5 AND a.ability IN ('Blaze', 'Solar Power')) OR 
(p.id = 6 AND a.ability IN ('Blaze', 'Solar Power')) OR 
(p.id = 7 AND a.ability IN ('Torrent', 'Rain Dish')) OR 
(p.id = 8 AND a.ability IN ('Torrent', 'Rain Dish')) OR 
(p.id = 9 AND a.ability IN ('Torrent', 'Rain Dish')) OR 
(p.id = 10 AND a.ability IN ('Shield Dust', 'Run Away')) OR 
(p.id = 11 AND a.ability IN ('Shed Skin')) OR 
(p.id = 12 AND a.ability IN ('Compound Eyes', 'Tinted Lens')) OR 
(p.id = 13 AND a.ability IN ('Shield Dust', 'Run Away')) OR 
(p.id = 14 AND a.ability IN ('Shed Skin')) OR 
(p.id = 15 AND a.ability IN ('Swarm', 'Sniper')) OR 
(p.id = 16 AND a.ability IN ('Keen Eye', 'Tangled Feet', 'Big Pecks')) OR 
(p.id = 17 AND a.ability IN ('Keen Eye', 'Tangled Feet', 'Big Pecks')) OR 
(p.id = 18 AND a.ability IN ('Keen Eye', 'Tangled Feet', 'Big Pecks')) OR 
(p.id = 19 AND a.ability IN ('Run Away', 'Guts')) OR 
(p.id = 20 AND a.ability IN ('Run Away', 'Guts', 'Hustle')) OR 
(p.id = 21 AND a.ability IN ('Keen Eye', 'Sniper')) OR 
(p.id = 22 AND a.ability IN ('Keen Eye', 'Sniper')) OR 
(p.id = 23 AND a.ability IN ('Intimidate', 'Shed Skin', 'Unnerve')) OR 
(p.id = 24 AND a.ability IN ('Intimidate', 'Shed Skin', 'Unnerve')) OR 
(p.id = 25 AND a.ability IN ('Static', 'Lightning Rod')) OR 
(p.id = 26 AND a.ability IN ('Static', 'Lightning Rod')) OR 
(p.id = 27 AND a.ability IN ('Sand Veil', 'Sand Rush')) OR 
(p.id = 28 AND a.ability IN ('Sand Veil', 'Sand Rush')) OR 
(p.id = 29 AND a.ability IN ('Poison Point', 'Rivalry', 'Hustle')) OR 
(p.id = 30 AND a.ability IN ('Poison Point', 'Rivalry', 'Hustle')) OR 
(p.id = 31 AND a.ability IN ('Poison Point', 'Rivalry', 'Sheer Force')) OR 
(p.id = 32 AND a.ability IN ('Poison Point', 'Rivalry', 'Hustle')) OR 
(p.id = 33 AND a.ability IN ('Poison Point', 'Rivalry', 'Hustle')) OR 
(p.id = 34 AND a.ability IN ('Poison Point', 'Rivalry', 'Sheer Force')) OR 
(p.id = 35 AND a.ability IN ('Cute Charm', 'Magic Guard', 'Friend Guard')) OR 
(p.id = 36 AND a.ability IN ('Cute Charm', 'Magic Guard', 'Unaware')) OR 
(p.id = 37 AND a.ability IN ('Flash Fire', 'Drought')) OR 
(p.id = 38 AND a.ability IN ('Flash Fire', 'Drought')) OR 
(p.id = 39 AND a.ability IN ('Cute Charm', 'Competitive')) OR 
(p.id = 40 AND a.ability IN ('Cute Charm', 'Competitive', 'Frisk'));
