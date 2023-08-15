CREATE VIEW vwPedidosNacionais AS 
SELECT * FROM pedidos
WHERE nm_pais = 'Brasil';

CREATE or REPLACE VIEW vwPedidosInternacionaisVia AS
SELECT a.*, b.nm_via FROM pedidos a
INNER JOIN via b ON b.cd_via = a.ds_via
WHERE nm_pais != 'Brasil'
ORDER BY nr_pedido;

SELECT * FROM `vwPedidosInternacionaisVia`