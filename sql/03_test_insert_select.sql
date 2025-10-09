
-- Script: 03_test_insert_select.sql
-- Propósito: Insertar una fila en 'ventas' y luego consultarla.


BEGIN;

-- INSERT de prueba
INSERT INTO ventas (valor_unitario, cantidad, impuesto, subtotal, iva, total)
VALUES (12000.00, 3, 0.19, 36000.00, 6840.00, 42840.00)
RETURNING venta_id;

-- Consulta de la fila recién insertada
SELECT *
FROM ventas
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- Si solo quieres probar y NO dejar datos, deja ROLLBACK:
ROLLBACK;


