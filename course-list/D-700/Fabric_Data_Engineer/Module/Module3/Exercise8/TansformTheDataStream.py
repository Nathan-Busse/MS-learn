# Exercise 8: Transform the Data Stream
# In this exercise, you will transform the data stream by filtering out null values, adding a new column to indicate if the product is a bike, and calculating the total price.
# Import necessary libraries

from pyspark.sql.functions import col, expr

spark = ... # Define your SparkSession here

stream_df = spark.readStream.format("delta").table("orders_in")

transformed_df = stream_df.filter(col("Price").isNotNull()) \
    .withColumn('IsBike', expr("INSTR(Product, 'Bike') > 0").cast('int')) \
    .withColumn('Total', expr("Quantity * Price").cast('decimal'))
    
# Write the stream to a delta table
output_table_path = 'Tables/orders_processed'
checkpointpath = 'Files/delta/checkpoint'
deltastream = transformed_df.writeStream.format("delta").option("checkpointLocation", checkpointpath).start(output_table_path)

print("Streaming to orders_processed...")
# Wait for the stream to finish
deltastream.awaitTermination()
# Stop the streaming data to avoid excessive processing costs
deltastream.stop()
# The above code transforms the data stream by filtering out null values, adding a new column to indicate if the product is a bike, and calculating the total price.
# The transformed data stream is then written to a delta table named "orders_processed" using the writeStream method.
# The checkpointLocation option specifies the location where the checkpoint files will be stored.
# The awaitTermination() method is used to wait for the stream to finish.
# The transformed data stream can be used for further analysis or processing using the PySpark API.
# The transformed data stream is then written to a delta table named "orders_processed" using the writeStream method.
# The checkpointLocation option specifies the location where the checkpoint files will be stored.