# Exercise 1: Using Package Managers in Code
# In this exercise, you will use the Package Managers in Code feature to install the required packages for your PySpark code.
#

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType
import pyspark.sql.functions as F

spark = ... # Define your SparkSession here

def display(df):
    print(df.show())

productSchema = StructType([
    StructField("ProductID", IntegerType()),
    StructField("ProductName", StringType()),
    StructField("Category", StringType()),
    StructField("ListPrice", FloatType())
    ])

df = spark.read.load('Files/data/product-data.csv',
    format='csv',
    schema=productSchema,
    header=False)
display(df.limit(10))
# The code above loads a dataframe from a CSV file and displays the first 10 rows of the dataframe.
# The dataframe is loaded using the Spark DataFrame API and the display() function is used to show the result in a tabular format.
# The dataframe has four columns: ProductID, ProductName, Category, and ListPrice.
# The dataframe is loaded using the CSV format and the schema is defined using the StructType and StructField classes.
# The header option is set to False, indicating that the first row of the CSV file does not contain column names.
# The dataframe is displayed using the display() function, which shows the first 10 rows of the dataframe in a tabular format.
# The dataframe can be used for further analysis or processing using the PySpark API.