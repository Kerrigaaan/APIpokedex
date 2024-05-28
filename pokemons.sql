CREATE DATABASE IF NOT EXISTS pokedex;
USE pokedex;

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

CREATE TABLE IF NOT EXISTS pokemon_type (
    pokemon_id INT,
    type VARCHAR(50),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);

CREATE TABLE IF NOT EXISTS pokemon_ability (
    pokemon_id INT,
    ability VARCHAR(50),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);

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

INSERT INTO pokemon_type (pokemon_id, type) VALUES
(1, 'Grass'), (1, 'Poison'), (2, 'Grass'), (2, 'Poison'), (3, 'Grass'), (3, 'Poison'),
(4, 'Fire'), (5, 'Fire'), (6, 'Fire'), (6, 'Flying'), (7, 'Water'), (8, 'Water'), (9, 'Water'),
(10, 'Bug'), (11, 'Bug'), (12, 'Bug'), (12, 'Flying'), (13, 'Bug'), (13, 'Poison'), 
(14, 'Bug'), (14, 'Poison'), (15, 'Bug'), (15, 'Poison'), (16, 'Normal'), (16, 'Flying'), 
(17, 'Normal'), (17, 'Flying'), (18, 'Normal'), (18, 'Flying'), (19, 'Normal'), 
(20, 'Normal'), (21, 'Normal'), (21, 'Flying'), (22, 'Normal'), (22, 'Flying'), 
(23, 'Poison'), (24, 'Poison'), (25, 'Electric'), (26, 'Electric'), (27, 'Ground'), 
(28, 'Ground'), (29, 'Poison'), (30, 'Poison'), (31, 'Poison'), (31, 'Ground'), 
(32, 'Poison'), (33, 'Poison'), (34, 'Poison'), (34, 'Ground'), (35, 'Fairy'), 
(36, 'Fairy'), (37, 'Fire'), (38, 'Fire'), (39, 'Normal'), (39, 'Fairy'), 
(40, 'Normal'), (40, 'Fairy');

INSERT INTO pokemon_ability (pokemon_id, ability) VALUES
(1, 'Overgrow'), (1, 'Chlorophyll'), (2, 'Overgrow'), (2, 'Chlorophyll'), (3, 'Overgrow'), 
(3, 'Chlorophyll'), (4, 'Blaze'), (4, 'Solar Power'), (5, 'Blaze'), (5, 'Solar Power'), 
(6, 'Blaze'), (6, 'Solar Power'), (7, 'Torrent'), (7, 'Rain Dish'), (8, 'Torrent'), 
(8, 'Rain Dish'), (9, 'Torrent'), (9, 'Rain Dish'), (10, 'Shield Dust'), (10, 'Run Away'), 
(11, 'Shed Skin'), (12, 'Compound Eyes'), (12, 'Tinted Lens'), (13, 'Shield Dust'), 
(13, 'Run Away'), (14, 'Shed Skin'), (15, 'Swarm'), (15, 'Sniper'), (16, 'Keen Eye'), 
(16, 'Tangled Feet'), (16, 'Big Pecks'), (17, 'Keen Eye'), (17, 'Tangled Feet'), 
(17, 'Big Pecks'), (18, 'Keen Eye'), (18, 'Tangled Feet'), (18, 'Big Pecks'), 
(19, 'Run Away'), (19, 'Guts'), (20, 'Run Away'), (20, 'Guts'), (20, 'Hustle'), 
(21, 'Keen Eye'), (21, 'Sniper'), (22, 'Keen Eye'), (22, 'Sniper'), (23, 'Intimidate'), 
(23, 'Shed Skin'), (23, 'Unnerve'), (24, 'Intimidate'), (24, 'Shed Skin'), (24, 'Unnerve'), 
(25, 'Static'), (25, 'Lightning Rod'), (26, 'Static'), (26, 'Lightning Rod'), (27, 'Sand Veil'), 
(27, 'Sand Rush'), (28, 'Sand Veil'), (28, 'Sand Rush'), (29, 'Poison Point'), 
(29, 'Rivalry'), (29, 'Hustle'), (30, 'Poison Point'), (30, 'Rivalry'), (30, 'Hustle'), 
(31, 'Poison Point'), (31, 'Rivalry'), (31, 'Sheer Force'), (32, 'Poison Point'), 
(32, 'Rivalry'), (32, 'Hustle'), (33, 'Poison Point'), (33, 'Rivalry'), (33, 'Hustle'), 
(34, 'Poison Point'), (34, 'Rivalry'), (34, 'Sheer Force'), (35, 'Cute Charm'), 
(35, 'Magic Guard'), (35, 'Friend Guard'), (36, 'Cute Charm'), (36, 'Magic Guard'), 
(36, 'Unaware'), (37, 'Flash Fire'), (37, 'Drought'), (38, 'Flash Fire'), (38, 'Drought'), 
(39, 'Cute Charm'), (39, 'Competitive'), (40, 'Cute Charm'), (40, 'Competitive'), (40, 'Frisk');
