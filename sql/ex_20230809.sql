-- Active: 1675433496076@@127.0.0.1@3306@teste_aula
-- Exercícios:

USE teste_aula;
-- 1. Inicie uma transação
begin;
-- 2. Dobre o valor do frete na tabela de pedidos de todas as linhas dos EUA.
UPDATE pedidos
SET vl_frete = vl_frete * 2
WHERE nm_pais = 'EUA';
SELECT nr_pedido, vl_frete, nm_pais FROM pedidos
WHERE nm_pais = 'EUA';
-- 3. Crie um savepoint antes de iniciar a mudança do Brasil (abaixo).
SAVEPOINT brasil;
-- 4. Triplique o valor do frete na tabela de pedidos de todas as linhas do Brasil.
UPDATE pedidos
SET vl_frete = vl_frete * 3
WHERE nm_pais = 'Brasil';

SELECT nr_pedido, vl_frete, nm_pais FROM pedidos
WHERE nm_pais = 'Brasil';
-- 5. Acesse por outra conexão e confira se o valor de uma das linhas do BR ou dos EUA foi alterada para
-- os demais usuários. (esperado que nada seja alterado).

-- 6. Desfaça as alterações posteriores ao savepoint.
ROLLBACK to SAVEPOINT brasil;

SELECT nr_pedido, vl_frete, nm_pais FROM pedidos
WHERE nm_pais = 'Brasil';
-- 7. Efetive as mudanças no banco com o comando commit;
COMMIT;

-- 8. Confira quais mudanãs afetam outros usuários. (esperado que apenas os valore dos EUA sejam alterados).