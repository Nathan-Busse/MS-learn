from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, year, month

# Initialize SparkSession
spark = SparkSession.builder.getOrCreate()

# Read the new sales data
df = spark.read.format("csv").option("header","true").load("Files/new_data/*.csv")

## Add month and year columns
df = df.withColumn("Year", year(col("OrderDate"))).withColumn("Month", month(col("OrderDate")))

# Derive FirstName and LastName columns
df = df.withColumn("FirstName", split(col("CustomerName"), " ").getItem(0)).withColumn("LastName", split(col("CustomerName"), " ").getItem(1))

# Filter and reorder columns
df = df["SalesOrderNumber", "SalesOrderLineNumber", "OrderDate", "Year", "Month", "FirstName", "LastName", "EmailAddress", "Item", "Quantity", "UnitPrice", "TaxAmount"]

# Load the data into a table
table_name = "your_table_name"  # Replace with your actual table name
df.write.format("delta").mode("append").saveAsTable(table_name)