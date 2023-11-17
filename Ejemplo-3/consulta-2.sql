-- Versión 1
SELECT 
	c.importe_solicitado,
	c.estado_credito,
	t.gastos_ult_12m
FROM creditos c, 
	tarjetas t
WHERE c.id_cliente = t.id_cliente 
	and c.estado_credito = 0;

-- Versión 2
SELECT 
	c.importe_solicitado,
	c.estado_credito,
	t.gastos_ult_12m
FROM creditos c INNER JOIN tarjetas t
	ON c.id_cliente = t.id_cliente
WHERE c.estado_credito = 0;