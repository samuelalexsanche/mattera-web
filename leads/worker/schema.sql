-- Contactos capturados en la expo Connect Zapopan y en el sitio.
-- Solo lo que la persona escribe y acepta compartir; nada de rastreo.
CREATE TABLE IF NOT EXISTS leads (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  creado      TEXT    NOT NULL,          -- ISO 8601 UTC
  nombre      TEXT    NOT NULL,
  telefono    TEXT    NOT NULL,
  giro        TEXT,                      -- a qué se dedica
  dolor       TEXT,                      -- qué le quita tiempo hoy
  horas_anio  INTEGER,                   -- resultado de la medición, si lo hizo
  personas    INTEGER,
  origen      TEXT,                      -- 'expo' | 'sitio'
  nota        TEXT                       -- para el seguimiento posterior
);
CREATE INDEX IF NOT EXISTS idx_leads_creado ON leads(creado DESC);
CREATE UNIQUE INDEX IF NOT EXISTS idx_leads_tel ON leads(telefono);
