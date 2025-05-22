/*
Module 5 exercise 2 Query data warehouse tables part 2:

Modify the uery as follows: to add a second dimension to the aggregation.
*/

SELECT  d.[Year] AS CalendarYear,
         d.[Month] AS MonthOfYear,
         d.MonthName AS MonthName,
         p.ProductCategory AS ProductCategory,
         SUM(so.SalesTotal) AS SalesRevenue
FROM FactSalesOrder AS so
JOIN DimDate AS d ON so.SalesOrderDateKey = d.DateKey
JOIN DimProduct AS p ON so.ProductKey = p.ProductKey
GROUP BY d.[Year], d.[Month], d.MonthName, p.ProductCategory
ORDER BY CalendarYear, MonthOfYear, ProductCategory;
