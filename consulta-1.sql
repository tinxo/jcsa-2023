EXPLAIN ANALYZE SELECT 	c.importe_solicitado,
						c.falta_pago,
						c.estado_credito
	FROM creditos c
	WHERE c.duracion_credito = 2 AND
		c.objetivo_credito like '%PERSONAL%';