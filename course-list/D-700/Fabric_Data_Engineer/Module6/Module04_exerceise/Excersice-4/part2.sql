/*
Module 5 Exercise 4 Create a view part 2:
Create a new SQL query and run the following code below:

This query is known as a SELECT statement.
*/

SELECT CalendarYear, MonthName, SalesRegion, SalesRevenue
FROM vSalesByRegion
ORDER BY CalendarYear, MonthOfYear, SalesRegion;
/*
Note that the view is created in the current database context.
You can use the view in the same way as a table,
and you can use it in a query to return the data.
For example, you can run the following query to return the data from the view:
*/
--
-- Compare this snippet from course-list/D-700/Fabric_Data_Engineer/python_scripts/Module6/Module04_exercise/Exercise%20-4/part1.sql:
-- /*
-- Module 5 Exercise 3 Create a view part 1:
-- A data warehouse in Microsoft Fabric has many of the same capabilities you may be used to in relational databases.
-- For example, you can create database objects like views and stored procedures to encapsulate SQL logic.
--
-- Modify the query you created previously as follows
--  to create a view (note that you need to remove the ORDER BY clause to create a view). ALTER
-- */
