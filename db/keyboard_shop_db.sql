DROP TABLE IF EXISTS keyboards;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS categories;

CREATE TABLE brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    origin VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE keyboards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    brand_id INT REFERENCES brands(id) ON DELETE CASCADE,
    description VARCHAR(255),
    category_id INT REFERENCES categories(id),
    current_stock INT,
    cost_price INT,
    sale_price INT
);
