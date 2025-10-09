
-- Script: 01_create_ventas.sql
-- Descripción: Crea la tabla 'ventas' en la base de datos PostgreSQL


CREATE TABLE IF NOT EXISTS ventas (
    venta_id BIGSERIAL PRIMARY KEY,                   -- Identificador único autoincremental
    valor_unitario NUMERIC(12, 2) NOT NULL CHECK (valor_unitario > 0), -- Precio del producto
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),                    -- Cantidad vendida
    impuesto NUMERIC(5, 4) NOT NULL CHECK (impuesto BETWEEN 0 AND 1),  -- Proporción del impuesto (0.19 = 19%)
    subtotal NUMERIC(12, 2) NOT NULL,                                  -- valor_unitario * cantidad
    iva NUMERIC(12, 2) NOT NULL,                                       -- subtotal * impuesto
    total NUMERIC(12, 2) NOT NULL,                                     -- subtotal + iva
    created_at TIMESTAMPTZ DEFAULT NOW(),                              -- Fecha de creación
    updated_at TIMESTAMPTZ DEFAULT NOW()                               -- Fecha de última actualización
);
