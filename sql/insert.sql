-- Active: 1675433496076@@127.0.0.1@3306@restaurante
-- cd, nm, cat, preço
INSERT INTO restaurante.cardapio
    (nm_produto, ds_categotia, vl_produto)

VALUES
    ('Macarrao', 'Pratos', 49.90),
    ('Coca-Cola', 'Refrigerante', 7.90),
    ('Cerveja Antarctica', 'Cerveja', 15.00);

SELECT * FROM restaurante.cardapio;

DROP TABLE funcionarios;

INSERT INTO restaurante.funcionarios
    (nm_funcionario, ds_cargo, dt_nascimento, dt_admissao)
VALUES
    ('José dos Santos', 'Garçom', "1977-07-01", DEFAULT),
    ('Maria da Silva', 'Cozinheira', '1992-02-14', '2021-02-22'),
    ('Paulo Souza', 'Auxiliar de Cozinha', '2001-10-24', DEFAULT);

INSERT INTO restaurante.cliente
    (nm_cliente, ds_convenio, vl_desconto)
VALUES
    ('João Machado', null, null),
    ('Juliana Santos', 'Hospital', 15),
    ('Eduardo Ribas', 'Shopping', 10);

SELECT * FROM restaurante.cliente;

create table pessoa (
    codigo integer not null auto_increment,
    nome varchar(100) not null,
    endereco varchar(200),
    nascimento date,
    primary key (codigo)
);

SHOW VARIABLES LIKE "secure_file_priv";

LOAD DATA INFILE '/var/lib/mysql-files/pessoa.txt'
INTO TABLE pessoa
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(codigo,nome,endereco,@nascimento)
SET nascimento = str_to_date(@nascimento, '%d/%m/%Y');

SELECT * FROM pessoa;

load data infile '/home/andre/Documentos/cursopython/exercicios_python/sql' 
into table pessoa
character set latin1
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
(codigo,nome,endereco,@nascimento)
set
nascimento = str_to_date(@nascimento, '%d/%m/%Y')
;