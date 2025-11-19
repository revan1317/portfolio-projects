CREATE TABLE films (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titel VARCHAR(255) NOT NULL,
    duur INT NOT NULL,
    datum_van_uitkomst DATE,
    land_van_uitkomst VARCHAR(100),
    omschrijving TEXT NOT NULL,
    youtube_trailer_id VARCHAR(20) NOT NULL
);

INSERT INTO films (titel, duur, datum_van_uitkomst, land_van_uitkomst, omschrijving, youtube_trailer_id) VALUES
    ('Inception', 148, '2010-07-16', 'VS', 'Een meesterdief krijgt de kans om zijn strafblad te wissen door een idee in het onderbewustzijn van een CEO te planten.', 'YoHD9XEInc0'),
    ('Interstellar', 169, '2014-11-07', 'VS', 'Een team astronauten reist door een wormgat op zoek naar een nieuwe bewoonbare planeet.', 'zSWdZVtXT7E'),
    ('The Matrix', 136, '1999-03-31', 'VS', 'Een computerhacker ontdekt dat de realiteit een illusie is en sluit zich aan bij een opstand tegen de controleurs.', 'vKQi3bBA1y8'),
    ('The Dark Knight', 152, '2008-07-18', 'VS', 'Batman neemt het op tegen de Joker, die chaos en vernietiging brengt in Gotham City.', 'EXeTwQWrcwY'),
    ('Pulp Fiction', 154, '1994-10-14', 'VS', 'Verweven verhalen van criminelen, huurmoordenaars en een mysterieuze koffer in Los Angeles.', 's7EdQ4FqbhY');