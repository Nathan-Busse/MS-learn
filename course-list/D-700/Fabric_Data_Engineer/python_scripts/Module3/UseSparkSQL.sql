-- Exercise 5: Create a table using SQL

CREATE TABLE salesorders
USING DELTA
LOCATION '/mnt/delta/salesorders'
AS
SELECT *
FROM sales
WHERE OrderDate >= '2023-01-01'
  AND OrderDate < '2024-01-01'
  AND CustomerName IS NOT NULL
  AND SalesTotal > 0
  AND Orderid IS NOT NULL

