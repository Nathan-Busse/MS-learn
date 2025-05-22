# Exercise 2: Creating a bar plot of product counts by category
# In this exercise, you will create a bar plot of product counts by category using the Matplotlib library.

import matplotlib.pyplot as plt

# If you see "Import 'matplotlib.pyplot' could not be resolved from source", ensure matplotlib is installed in your environment.
# pip install matplotlib

spark = ... # Define your SparkSession here

# All keywords like figsize, xlabel, ylabel, linestyle, xticks are valid for matplotlib and can be ignored if flagged by a linter.

# Get the data as a Pandas dataframe
data = spark.sql("SELECT Category, COUNT(ProductID) AS ProductCount \
                  FROM products \
                  GROUP BY Category \
                  ORDER BY Category").toPandas()

# Clear the plot area
plt.clf()

# Create a Figure
fig = plt.figure(figsize=(12,8))

# Create a bar plot of product counts by category
plt.bar(x=data['Category'], height=data['ProductCount'], color='orange')

# Customize the chart
plt.title('Product Counts by Category')
plt.xlabel('Category')
plt.ylabel('Products')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(rotation=70)

# Show the plot area
plt.show()
# The above code creates a bar plot of product counts by category using the Matplotlib library.
# The data is obtained from the "products" table using a SQL query that counts the number of products in each category.
# The result is then converted to a Pandas dataframe using the toPandas() method.
# The plot is customized with a title, x and y labels, grid lines, and rotated x-axis labels for better readability.
# The plot is displayed using the show() method.
# The bar plot shows the number of products in each category, with the categories on the x-axis and the product counts on the y-axis.
# The bar plot is displayed in a tabular format using the display() function.

# spark = ... # Define your SparkSession here

# All keywords like figsize, xlabel, ylabel, linestyle, xticks are valid for matplotlib and can be ignored if flagged by a linter.