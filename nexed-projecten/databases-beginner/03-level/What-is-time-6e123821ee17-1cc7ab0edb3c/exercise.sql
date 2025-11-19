USE sterrenstelsel;

TRUNCATE TABLE planeten;

ALTER TABLE planeten
ADD COLUMN diameter INT NOT NULL,
ADD COLUMN afstand BIGINT NOT NULL,
ADD COLUMN massa FLOAT NOT NULL,
ADD COLUMN datum_bezoek DATE;

INSERT INTO planeten (naam, diameter, afstand, massa, datum_bezoek) VALUES
('Zon', 1392700, 0, 333000, NULL),
('Mercurius', 4879, 57910000, 0.055, NULL),
('Venus', 12104, 108200000, 0.815, NULL),
('Aarde', 12742, 149600000, 1, NULL),
('Mars', 6779, 227900000, 0.107, NULL),
('Maan', 3474, 384400, 0.0123, '1969-07-20');