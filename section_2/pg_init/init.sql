CREATE TABLE sales (
    id BIGINT NOT NULL,
    salesperson_id INT NOT NULL,
    customer_id BIGINT NOT NULL,
    serial_number VARCHAR(30) NOT NULL,
    price FLOAT NOT NULL,
    DATE DATE NOT NULL
);

CREATE TABLE cars (
    serial_number BIGINT NOT NULL,
    manufacturer TEXT NOT NULL,
    model_name TEXT NOT NULL,
    weight FLOAT NULL
);

CREATE TABLE customers (
    customer_id BIGINT NOT NULL,
    name TEXT NOT NULL,
    phone VARCHAR(8) NULL
);

CREATE TABLE salesperson (
    salesperson_id INT NOT NULL,
    name TEXT NOT NULL,
    phone VARCHAR(8) NULL
);
