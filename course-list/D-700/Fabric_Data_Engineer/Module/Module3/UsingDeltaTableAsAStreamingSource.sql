-- Exercise 7: Using Delta Table as a Streaming Source

CREATE TABLE orders_in
(
    OrderID INT,
    OrderDate DATE,
    Customer STRING,
    Product STRING,
    Quantity INT,
    Price DECIMAL(10,2)
);

-- Create a streaming table
-- If INSERT INTO is not supported in your SQL environment, consider using COPY INTO with a staged CSV file, or use the Spark SQL/DataFrame API for Delta tables.
-- Example for Spark SQL:
-- INSERT INTO orders_in VALUES
--     (3001, '2024-09-01', 'Yang', 'Road Bike Red', 1, 1200),
--     (3002, '2024-09-01', 'Carlson', 'Mountain Bike Silver', 1, 1500),
--     (3003, '2024-09-02', 'Wilson', 'Road Bike Yellow', 2, 1350),
--     (3004, '2024-09-02', 'Yang', 'Road Front Wheel', 1, 115),
--     (3005, '2024-09-02', 'Rai', 'Mountain Bike Black', 1, NULL);

INSERT INTO orders_in VALUES
    (3001, '2024-09-01', 'Yang', 'Road Bike Red', 1, 1200),
    (3002, '2024-09-01', 'Carlson', 'Mountain Bike Silver', 1, 1500),
    (3003, '2024-09-02', 'Wilson', 'Road Bike Yellow', 2, 1350),
    (3004, '2024-09-02', 'Yang', 'Road Front Wheel', 1, 115),
    (3005, '2024-09-02', 'Rai', 'Mountain Bike Black', 1, NULL);