-- Elimina la tabla si existe
DROP TABLE IF EXISTS public.ventas CASCADE;

-- Crea la tabla principal de ventas
CREATE TABLE public.ventas (
  venta_id       BIGSERIAL PRIMARY KEY,
  valor_unitario NUMERIC(12,2) NOT NULL CHECK (valor_unitario > 0),
  cantidad       INTEGER NOT NULL CHECK (cantidad > 0),
  impuesto       NUMERIC(6,4) NOT NULL CHECK (impuesto >= 0 AND impuesto <= 1),
  subtotal       NUMERIC(14,2) NOT NULL,
  iva            NUMERIC(14,2) NOT NULL,
  total          NUMERIC(14,2) NOT NULL,
  created_at     TIMESTAMPTZ DEFAULT NOW(),
  updated_at     TIMESTAMPTZ DEFAULT NOW()
);

-- Función trigger para actualizar el campo updated_at
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at := NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crea el trigger
DROP TRIGGER IF EXISTS trg_ventas_updated_at ON public.ventas;
CREATE TRIGGER trg_ventas_updated_at
BEFORE UPDATE ON public.ventas
FOR EACH ROW EXECUTE FUNCTION set_updated_at();
