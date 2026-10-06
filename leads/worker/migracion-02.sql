-- Folio para recoger el regalo en el stand, y la cuenta del negocio que se
-- graba en el llavero NFC.
ALTER TABLE leads ADD COLUMN folio TEXT;
ALTER TABLE leads ADD COLUMN cuenta TEXT;
ALTER TABLE leads ADD COLUMN entregado INTEGER DEFAULT 0;
CREATE UNIQUE INDEX IF NOT EXISTS idx_leads_folio ON leads(folio);
