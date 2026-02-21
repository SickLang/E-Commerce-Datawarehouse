CREATE SCHEMA IF NOT EXISTS bronze;

CREATE TABLE IF NOT EXISTS bronze.amazon_sale (
    order_id INTEGER NOT NULL,
    order_date DATE,
    product_id INTEGER,
    product_category VARCHAR(50),
    price NUMERIC(12,2),
    discount_percent NUMERIC(5,2),
    quantity_sold INTEGER,
    customer_region VARCHAR(50),
    payment_method VARCHAR(50),
    rating NUMERIC(3,2),
    review_count INTEGER,
    discounted_price NUMERIC(12,2),
    total_revenue NUMERIC(14,2),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);