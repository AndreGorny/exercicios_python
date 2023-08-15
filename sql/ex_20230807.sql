-- Active: 1675433496076@@127.0.0.1@3306@teste_aula
CREATE TABLE shows (
    cd_show INT PRIMARY KEY AUTO_INCREMENT,
    nm_show VARCHAR(100),
    dt_show DATE
);

CREATE TABLE bandas(
    cd_banda INT PRIMARY KEY AUTO_INCREMENT,
    nm_banda VARCHAR(50)
);

INSERT INTO shows (nm_show, dt_show)
VALUES ("Rock in Rio", '2023-08-08'),
("Lollapalooza", '2023-08-09'),
("Festival de Curitiba", '2023-08-07');

INSERT INTO bandas (nm_banda)
VALUES ("AC/DC"),
       ("Nirvana"),
       ("U2"),
       ("Coldplay"),
       ("Iron Maiden");

CREATE TABLE lineups(
    cd_lineup INT PRIMARY KEY AUTO_INCREMENT,
    fk_shows INT,
    fk_banda INT,
    FOREIGN KEY (fk_banda) REFERENCES bandas(cd_banda),
    FOREIGN KEY (fk_shows) REFERENCES shows(cd_show)
);

INSERT INTO lineups (fk_shows, fk_banda)
VALUES (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
(2, 2), (2, 4), (2, 3),
(3, 1), (3, 4), (3, 5);

SELECT * FROM lineups;

SELECT nm_show, nm_banda FROM shows a
INNER JOIN lineups b ON b.fk_shows = a.cd_show
INNER JOIN bandas c ON b.fk_banda = c.cd_banda;
