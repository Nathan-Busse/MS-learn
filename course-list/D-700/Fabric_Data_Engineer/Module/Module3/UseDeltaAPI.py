# Exercise 6: Use the Delta API
from delta.tables import DeltaTable
import pyspark.sql.functions as F

spark = ... # Define your SparkSession here

# Create a DeltaTable object
delta_path = "Files/mytable"
deltaTable = DeltaTable.forPath(spark, delta_path)

# Update the table (reduce price of accessories by 10%)
deltaTable.update(
    condition = "Category == 'Accessories'",
    set = { "Price": "Price * 0.9" })
# The above code updates the delta table by reducing the price of accessories by 10%.
# Table name "mytable" is valid and can be ignored if flagged by a linter.
