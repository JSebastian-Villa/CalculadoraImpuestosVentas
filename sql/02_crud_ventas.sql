-- ===============================================================
-- Script: 02_crud_ventas.sql
-- Descripción: Pruebas de inserción, consulta, actualización y borrado
-- Tabla: ventas
-- ===============================================================

-- RECOMENDACIÓN: ejecutar este archivo dentro de una transacción manual
-- para poder hacer ROLLBACK si algo sale mal.
BEGIN;

-- 1) INSERT: crear una venta de prueba
--   valor_unitario = 10,000 ; cantidad = 5 ; impuesto = 0.19
--   subtotal = 50,000 ; iva = 9,500 ; total = 59,500
INSERT INTO ventas (valor_unitario, cantidad, impuesto, subtotal, iva, total)
VALUES (10000.00, 5, 0.19, 50000.00, 9500.00, 59500.00)
RETURNING venta_id;

-- Copia el 'venta_id' devuelto por la línea anterior (ej: 1)
-- Para que el script sea repetible, usamos el último id insertado:
WITH ultimo AS (
  SELECT MAX(venta_id) AS vid FROM ventas
)
SELECT * FROM ventas WHERE venta_id = (SELECT vid FROM ultimo);

-- 2) SELECT: consulta por clave primaria
-- (si quieres usar el id explícito, reemplaza el subselect por el número)
SELECT * 
FROM ventas 
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- 3) UPDATE: modificar cantidad y recalcular totales
--   nueva cantidad = 6  => subtotal = 60,000 ; iva = 11,400 ; total = 71,400
UPDATE ventas
SET cantidad  = 6,
    subtotal  = 10000.00 * 6,
    iva       = (10000.00 * 6) * 0.19,
    total     = (10000.00 * 6) + ((10000.00 * 6) * 0.19),
    updated_at = NOW()
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- Verificar el cambio
SELECT * 
FROM ventas 
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- 4) DELETE: borrar el registro de prueba (si no quieres borrar, comenta esto)
DELETE FROM ventas
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- Confirmar que ya no existe
SELECT * 
FROM ventas 
WHERE venta_id = (SELECT MAX(venta_id) FROM ventas);

-- Si todo salió bien, confirma; si quieres dejar datos de prueba, usa ROLLBACK.
COMMIT;
-- ROLLBACK;  -- <- úsalo en vez de COMMIT para deshacer todo
