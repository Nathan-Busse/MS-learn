/*
Module 5 Exercise part 1:
Create the tables and insert data
*/
-- Create the tables
-- Create the dbo.DimCustomer table

CREATE TABLE dbo.DimProduct
(
    ProductKey INTEGER NOT NULL,
    ProductAltKey VARCHAR(25) NULL,
    ProductName VARCHAR(50) NOT NULL,
    Category VARCHAR(50) NULL,
    ListPrice DECIMAL(5,2) NULL
);
GO
