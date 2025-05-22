# Exercise 3: Creating a delta table from a dataframe

#Creating a delta table from a dataframe
# One of the easiest ways to create a delta table in Spark is to save a dataframe in the delta format.
# For example,

#Below is the following PySpark code loads a dataframe with data from an existing file, and then saves that dataframe as a delta table:

##Script
# Load a dataframe from a CSV file
df = spark.read.load('Files/data/product-data.csv',
    format='csv',
    schema=productSchema,
    header=False)
# Save the dataframe as a delta table
df.write.format("delta").mode("overwrite").saveAsTable("products")
# The code above loads a dataframe from a CSV file and saves it as a delta table named "products".
# The dataframe is saved in the delta format, which allows for ACID transactions and time travel.
# The mode("overwrite") option specifies that if the table already exists, it should be overwritten.
# The saveAsTable("products") method saves the dataframe as a table named "products" in the default database.
# The delta table can then be queried using SQL or DataFrame API.
# The delta table can be queried using SQL or DataFrame API.
# For example, you can run the following SQL query to get the first 10 rows of the delta table:
# %sql
# SELECT * FROM products LIMIT 10
# The above SQL query selects all columns from the "products" table and limits the result to 10 rows.
# The result will be displayed in a tabular format.
# The delta table can also be queried using the DataFrame API:
# df = spark.sql("SELECT * FROM products LIMIT 10")
# display(df)
# The above code uses the Spark SQL API to query the "products" table and limit the result to 10 rows.
# The result is then displayed in a tabular format using the display() function.
# The delta table can be queried using SQL or DataFrame API.

spark = ... # Define your SparkSession here
productSchema = ... # Define your schema here