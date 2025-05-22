/*
Module 5 Exercise 2 Query data warehouse tables part 1: 
Create a mew SQL query and run the following code below:
*/

SELECT  d.[Year] AS CalendarYear,
         d.[Month] AS MonthOfYear,
         d.MonthName AS MonthName,
        SUM(so.SalesTotal) AS SalesRevenue
FROM FactSalesOrder AS so
JOIN DimDate AS d ON so.SalesOrderDateKey = d.DateKey
GROUP BY d.[Year], d.[Month], d.MonthName
ORDER BY CalendarYear, MonthOfYear;
/*
Note that the attributes in the date dimension enable you 
to aggregate the measures in the fact table at 
multiple hierarchical levels - in this case, year and month. 
This is a common pattern in data warehouses.
*/
