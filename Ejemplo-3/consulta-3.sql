-- Opción 1
SELECT 
    t.id_cliente,
    t.gastos_ult_12m,
    t.limite_credito_tc
FROM tarjetas t
WHERE t.id_cliente IN
                    (SELECT c.id_cliente
                        FROM creditos c
                        WHERE c.duracion_credito = 2 AND
                            c.objetivo_credito like '%PERSONAL%');

-- Opción 2
SELECT 
	t.id_cliente,
    t.gastos_ult_12m,
    t.limite_credito_tc
FROM creditos c INNER JOIN tarjetas t
	ON c.id_cliente = t.id_cliente
WHERE c.duracion_credito = 2 
    AND c.objetivo_credito like '%PERSONAL%';

-- Opción 3
SELECT 
	t.id_cliente,
    t.gastos_ult_12m,
    t.limite_credito_tc
 FROM creditos c, 
	tarjetas t
WHERE c.id_cliente = t.id_cliente 
    AND c.duracion_credito = 2 
    AND c.objetivo_credito like '%PERSONAL%';