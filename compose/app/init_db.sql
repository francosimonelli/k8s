-- Crear la tabla 'products' si no existe
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Insertar algunos productos de ejemplo
INSERT INTO products (name, price) VALUES ('Producto 1', 10.99);
INSERT INTO products (name, price) VALUES ('Producto 2', 15.49);
INSERT INTO products (name, price) VALUES ('Producto 3', 7.99);

