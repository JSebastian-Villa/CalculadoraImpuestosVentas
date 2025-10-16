-- 02_crud_ventas.sql  
BEGIN;

-- INSERT
INSERT INTO ventas (valor_unitario, cantidad, impuesto, subtotal, iva, total)
VALUES (10000.00, 5, 0.19, ROUND(10000.00*5,2), ROUND(ROUND(10000.00*5,2)*0.19,2), ROUND(ROUND(10000.00*5,2) + ROUND(ROUND(10000.00*5,2)*0.19,2),2))
RETURNING venta_id;

-- SELECT por el último
SELECT * FROM ventas WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- UPDATE (nueva cantidad = 6)
UPDATE ventas
SET cantidad  = 6,
    subtotal  = ROUND(valor_unitario * 6, 2),
    iva       = ROUND(ROUND(valor_unitario * 6, 2) * impuesto, 2),
    total     = ROUND(ROUND(valor_unitario * 6, 2) + ROUND(ROUND(valor_unitario * 6, 2) * impuesto, 2), 2)
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- Verificar
SELECT * FROM ventas WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- DELETE (si quieres dejar datos, comenta estas dos líneas)
DELETE FROM ventas WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);
SELECT * FROM ventas WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

COMMIT;
-- ROLLBACK;  -- usa esto en lugar de COMMIT si sólo estás probando
