CREATE DATABASE IF NOT EXISTS sterrenstelsel;
USE sterrenstelsel;

CREATE TABLE IF NOT EXISTS planeten (
    naam VARCHAR(255) NOT NULL,
    diameter INT NOT NULL,
    afstand BIGINT NOT NULL,
    massa FLOAT NOT NULL,
    datum_bezoek DATE
);

INSERT INTO planeten (naam, diameter, afstand, massa, datum_bezoek) VALUES
('Zon', 1392700, 0, 333000, NULL),
('Mercurius', 4879, 57910000, 0.055, NULL),
('Venus', 12104, 108200000, 0.815, NULL),
('Aarde', 12742, 149600000, 1, NULL),
('Mars', 6779, 227900000, 0.107, NULL),
('Maan', 3474, 384400, 0.0123, '1969-07-20');