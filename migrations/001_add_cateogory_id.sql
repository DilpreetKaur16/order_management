ALTER TABLE products
ADD COLUMN category_id INTEGER;

ALTER TABLE products
ADD CONSTRAINT fk_products_cateogory
FOREIGN KEY (category_id)
REFERENCES categories(id)

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'products'

UPDATE products 
SET category_id = 1
WHERE id IN (1,2,3)

SELECT p.id,
  p.name,
  p.sku,
  c.name as category_name
FROM products p JOIN categories c ON p.category_id = c.id

SELECT * FROM categories