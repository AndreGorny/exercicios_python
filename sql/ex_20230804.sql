-- Active: 1675433496076@@127.0.0.1@3306@teste_aula
USE teste_aula;

-- Exercícios:

-- 1. Traga o valor total dos fretes de cada funcionário no ano de 1997.

SELECT cd_funcionario, sum(vl_frete)
FROM pedidos
WHERE YEAR(dt_pedido) = 1997
GROUP BY cd_funcionario
ORDER BY cd_funcionario;

-- 2. Quantos pedidos cada funcionário fez?
SELECT cd_funcionario, count(*) as Qtd
FROM pedidos
GROUP BY cd_funcionario
ORDER BY cd_funcionario;

-- 3. Qual a comissão de cada pedido? (Considere que a comissão é de 10%)
SELECT nr_pedido, vl_frete, vl_frete * 0.1 as Comissão 
FROM pedidos;

SELECT * FROM pedidos;
-- 4. Liste os pedidos de todas as cidades que possuem a letra A.
SELECT * FROM pedidos
WHERE nm_cidade LIKE '%a%'
ORDER BY nm_cidade, nr_pedido;

-- 5. Liste os pedidos de 1998 feitos pelos funcionários 2 a 8, que sejam do Brasil,
-- Argentina e EUA, exceto os que foram entregues pela via 2.
SELECT * FROM pedidos
WHERE YEAR(dt_pedido) = 1998
AND cd_funcionario BETWEEN 2 and 8
AND nm_pais IN ('Brasil', 'Argentina', 'EUA')
-- AND nm_pais = 'Brasil' OR nm_pais = 'Argentina' OR nm_pais = 'EUA'
AND ds_via != 2
ORDER BY nm_pais, nr_pedido;

-- 6. Qual a quantidade de linhas, o valor total dos fretes, a média dos fretes,
-- o frete mais barato e o mais caro, dos pedidos mostrados no exercício 5.
SELECT count(*), sum(vl_frete), AVG(vl_frete), min(vl_frete), max(vl_frete)
FROM pedidos
WHERE YEAR(dt_pedido) = 1998
AND cd_funcionario BETWEEN 2 and 8
-- AND nm_pais IN ('Brasil', 'Argentina', 'EUA')
AND (nm_pais = 'Brasil' OR nm_pais = 'Argentina' OR nm_pais = 'EUA')
AND ds_via != 2
ORDER BY nm_pais, nr_pedido;


-- Aterar tabelas:

ALTER TABLE pedidos 
ADD COLUMN vl_comissao DECIMAL(6,2) DEFAULT 0;

ALTER TABLE pedidos
MODIFY COLUMN vl_comissao DECIMAL(8,2);

ALTER TABLE pedidos
DROP COLUMN vl_comissao;

SELECT * FROM pedidos;

UPDATE pedidos SET vl_comissao = vl_frete * 0.03;

ALTER TABLE pedidos
ADD INDEX idxCdCliente (cd_cliente),
ADD INDEX idxNmDestinatario (nm_destinatario),
ADD INDEX idxCdFuncionario (cd_funcionario);

ALTER TABLE pedidos DROP INDEX idxCdCliente;

CREATE TABLE via(
    cd_via INT PRIMARY KEY AUTO_INCREMENT,
    nm_via VARCHAR(50)
);

INSERT INTO via (nm_via)
VALUES ("Aérea"), ("Maritimo"), ("Terrestre");

ALTER TABLE pedidos ADD CONSTRAINT fk_via FOREIGN KEY (ds_via) REFERENCES via (cd_via);