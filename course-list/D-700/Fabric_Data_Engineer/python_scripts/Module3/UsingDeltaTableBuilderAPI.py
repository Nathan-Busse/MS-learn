# Exercise 4: Using DeltaTableBuilder API
# # In this exercise, you will use the DeltaTableBuilder API to create a delta table based from my specifications\
from delta.tables import DeltaTable

spark = ... # Define your SparkSession here

# Column names like "Productid" are valid and can be ignored if flagged by a linter.

DeltaTable.create(spark) \
  .tableName("products") \
  .addColumn("Productid", "INT") \
  .addColumn("ProductName", "STRING") \
  .addColumn("Category", "STRING") \
  .addColumn("Price", "FLOAT") \
  .execute()
# # The above code creates a delta table named "products" using the DeltaTableBuilder API.
# # The table has four columns: Productid, ProductName, Category, and Price.
# # The create() method is used to create a new delta table, and the tableName() method specifies the name of the table.
# # The addColumn() method is used to add columns to the table, specifying the column name and data type.