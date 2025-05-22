/*
Code example 1: Create tabbles
To create a table in the data warehouse, you can use SQL Server Management Studio (SSMS) or another SQL client to connect to the data warehouse and run a CREATE TABLE statement. You can also create tables directly in the Fabric UI.

You can copy data from an external location into a table in the data warehouse using the COPY INTO syntax. For example
*/

-- Use BULK INSERT for SQL Server or Azure SQL Database
BULK INSERT dbo.Region
FROM 'https://mystorageaccountxxx.blob.core.windows.net/private/Region.csv'
WITH (
    DATA_SOURCE = 'MyAzureBlobStorage',
    FORMAT = 'CSV',
    FIRSTROW = 2
);
GO
/*
This example copies data from a CSV file stored in Azure Blob Storage into a table named dbo.Region in the data warehouse. The COPY INTO statement specifies the file type, the credentials to access the file, and the first row to start copying from (in this case, skipping the header row).
*/