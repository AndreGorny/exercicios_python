-- 1. Consulte os cursos que o Pedro está fazendo, mostrando
-- o nome do curso e o nome do cliente no resultado da consulta.

-- 2. Consulta os pedidos dos EUA, mostrando se a via será aérea,
-- marítima ou terrestre.

SELECT a.nr_pedido, a.nm_pais, b.nm_via FROM pedidos a
INNER JOIN via b ON a.ds_via = b.cd_via
WHERE nm_pais = "EUA";

-- 3. Consulte os clientes que não estão fazendo nenhum curso.

-- 4. Mostre o nome do aluno e a quantidade de curso que ele está fazendo.ADD

-- 5. Mostre o nome da via e o valor total dos fretes de cada via.

SELECT b.nm_via, a.vl_frete
FROM pedidos a
INNER JOIN via b ON a.ds_via = b.cd_via
GROUP BY cd_via
;
