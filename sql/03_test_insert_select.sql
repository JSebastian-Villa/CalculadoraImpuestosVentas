BEGIN;

INSERT INTO ventas (valor_unitario, cantidad, impuesto, subtotal, iva, total)
VALUES (12000.00, 3, 0.19,
        ROUND(12000.00*3,2),
        ROUND(ROUND(12000.00*3,2)*0.19,2),
        ROUND(ROUND(12000.00*3,2) + ROUND(ROUND(12000.00*3,2)*0.19,2),2))
RETURNING venta_id;

SELECT * FROM ventas
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

ROLLBACK;
