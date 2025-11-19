USE sterrenstelsel;

CREATE TABLE IF NOT EXISTS planeten (
    naam VARCHAR(50) NOT NULL
);

INSERT INTO planeten (naam) VALUES ('Zon');
INSERT INTO planeten (naam) VALUES ('Mercurius');
INSERT INTO planeten (naam) VALUES ('Venus');
INSERT INTO planeten (naam) VALUES ('Aarde');
INSERT INTO planeten (naam) VALUES ('Mars');