/*
Module 5 Exercise 3 Create a view part 1:
A data warehouse in Microsoft Fabric has many of the same capabilities you may be used to in relational databases. 
For example, you can create database objects like views and stored procedures to encapsulate SQL logic.

Modify the query you created previously as follows
 to create a view (note that you need to remove the ORDER BY clause to create a view).
 */
CREATE VIEW vw_SalesRevenueByMonth
AS
SELECT  d.[Year] AS CalendarYear,
         d.[Month] AS MonthOfYear,
         d.MonthName AS MonthName,
         SUM(so.SalesTotal) AS SalesRevenue
FROM FactSalesOrder AS so
JOIN DimDate AS d ON so.SalesOrderDateKey = d.DateKey
GROUP BY d.[Year], d.[Month], d.MonthName;
/*
Note that the view is created in the current database context.
You can use the view in the same way as a table,
and you can use it in a query to return the data.
For example, you can run the following query to return the data from the view:
*/