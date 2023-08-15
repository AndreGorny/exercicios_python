USE teste_aula;
CREATE TABLE teste_aula.pedidos(
    nr_pedido INT PRIMARY KEY AUTO_INCREMENT,
    cd_cliente VARCHAR(10),
    cd_funcionario INT,
    dt_pedido DATETIME,
    dt_entrega DATETIME,
    dt_envio DATETIME,
    ds_via INT,
    vl_frete DECIMAL(6,2),
    nm_destinatario VARCHAR(100),
    ds_endereco VARCHAR(200),
    nm_cidade VARCHAR(50),
    ds_regiao VARCHAR(20),
    nr_cep VARCHAR(10),
    nm_pais VARCHAR(50)
);

DROP TABLE teste_aula.pedidos;

TRUNCATE teste_aula.pedidos;
LOAD DATA INFILE '/var/lib/mysql-files/pedidos.txt'
INTO TABLE teste_aula.pedidos
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY "\r\n"
IGNORE 1 LINES
(nr_pedido,cd_cliente,cd_funcionario,@dt_pedido,
@dt_entrega,@dt_envio,ds_via,@vl_frete,nm_destinatario,
ds_endereco,nm_cidade,ds_regiao,nr_cep,nm_pais)
SET 
dt_pedido = STR_TO_DATE(@dt_pedido, '%d/%m/%Y %H:%i:%s'),
dt_entrega = STR_TO_DATE(@dt_entrega, '%d/%m/%Y %H:%i:%s'),
dt_envio = STR_TO_DATE(if (@dt_envio = "", null, @dt_envio),'%d/%m/%Y %H:%i:%s'),
vl_frete = REPLACE(TRIM(REPLACE(@vl_frete, 'R$','')),',','.')
;

-- Exercicios:

-- Escreva um comando de consulta (select) para:
-- 1. Trazer todos os registros do Brasil que tenham frete maior que 100 reais.
SELECT * FROM teste_aula.pedidos
WHERE nm_pais = 'Brasil' and vl_frete > 100;

-- 2. Trazer todos os registros entregues pela via 1 e pela via 2, que não sejam 
-- dos EUA, mas podem ser de qualquer outro país.
SELECT * FROM teste_aula.pedidos
WHERE ds_via = 1 or ds_via = 2
AND nm_pais != 'EUA';

-- 3. Trazer todos os registros feitos pelos funcionários 2, 3, 4, 5, 6 ou 7, que 
-- sejam dos EUA, Brasil ou Alemanha, mas não podem ser entregues pela via 2.
SELECT * FROM teste_aula.pedidos
WHERE cd_funcionario IN (2, 3, 4, 5, 6, 7)
AND nm_pais IN ('EUA', 'Brasil', 'Alemanha')
AND ds_via != 2;

-- 4. Trazer apenas o número do pedido, o valor do frete e o país dos registros
-- feitos pelos funcionários 2 a 8, mas apenas pedidos realizados no ano de 1998.

SELECT dt_pedido, cd_funcionario, nr_pedido, vl_frete, nm_pais
FROM pedidos
WHERE cd_funcionario BETWEEN 2 and 8
-- AND YEAR(dt_pedido) = 1998
AND dt_pedido BETWEEN '1998-01-01 00:00:00' and '1998-12-31 23:59:59';