-- UAT-09: multi-call test
-- data bundle: triggers migration classification
ALTER TABLE orders ADD COLUMN payment_method VARCHAR(50);
ALTER TABLE payments ADD COLUMN processor_fee DECIMAL(10,2);
