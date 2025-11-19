USE sterrenstelsel;

TRUNCATE TABLE planeten;

ALTER TABLE planeten
ADD COLUMN diameter INT,
ADD COLUMN afstand BIGINT,
ADD COLUMN massa FLOAT;

INSERT INTO planeten (naam, diameter, afstand, massa) VALUES
('Zon', 1392700, 0, 333000),
('Mercurius', 4879, 57910000, 0.055),
('Venus', 12104, 108200000, 0.815),
('Aarde', 12742, 149600000, 1),
('Mars', 6779, 227900000, 0.107);