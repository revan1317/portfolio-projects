USE sterrenstelsel;

ALTER TABLE planeten
ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;

INSERT INTO planeten (naam, diameter, afstand, massa, datum_bezoek) VALUES
('Mars', 6794, 227900000, 0.107, NULL);