from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, FloatType
from pyspark.sql import SparkSession

def spark():
    return SparkSession.builder.appName("DeltaTableExample").getOrCreate()

# Create the schema for the table
orderSchema = StructType([
    StructField("SalesOrderNumber", StringType()),
    StructField("SalesOrderLineNumber", IntegerType()),
    StructField("OrderDate", DateType()),
    StructField("CustomerName", StringType()),
    StructField("Email", StringType()),
    StructField("Item", StringType()),
    StructField("Quantity", IntegerType()),
    StructField("UnitPrice", FloatType()),
    StructField("Tax", FloatType())
])
    
# Import all files from bronze folder of lakehouse
df = spark.read.format("csv").option("header", "true").schema(orderSchema).load("Files/bronze/*.csv")

# Display the first 10 rows of the dataframe to preview your data
df.show(10)