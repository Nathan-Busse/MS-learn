spark = ... # Define your SparkSession here

def display(df):
    print(df.show())

# Read and display the input table
df = spark.read.format("delta").table("orders_in")

display(df)

# Load a streaming DataFrame from the Delta table
stream_df = spark.readStream.format("delta") \
    .option("ignoreChanges", "true") \
    .table("orders_in")

# Verify that the stream is streaming
stream_df.isStreaming