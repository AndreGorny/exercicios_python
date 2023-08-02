SELECT * FROM teste.cliente;

DROP TABLE teste.produtos;

CREATE TABLE teste.produtos(
    cd_produto INT PRIMARY KEY AUTO_INCREMENT,
    nm_produto VARCHAR(100) NOT NULL,
    ds_tipo VARCHAR(50),
    vl_produto DECIMAL(6,2) NOT NULL
);

INSERT INTO teste.produtos(
    nm_produto, ds_tipo, vl_produto
)
VALUES
    ('Brahma', 'Cerveja', 14.00),
    ('Heineken', 'Cerveja', 19),
    ('Refrigerante Lata', 'Refrigerante', 6),
    ('Boazinha', 'Cachaça', 8),
    ('Seleta', 'Cachaça', 10);

SELECT * FROM teste.produtos WHERE vl_produto < 10;

ALTER TABLE teste.produto
MODIFY COLUMN ds_marca VARCHAR(50)