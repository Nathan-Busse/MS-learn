# Introduction
Relational data warehouses are at the center of most enterprise business intelligence (BI) solutions. While the specific details may vary across data warehouse implementations, a common pattern based on a denormalized, multidimensional schema has emerged as the standard design for a relational data warehouse.

Microsoft Fabric's data warehouse is a modern version of the traditional data warehouse. It centralizes and organizes data from different departments, systems, and databases into a single, unified view for analysis and reporting purposes. Fabric's data warehouse provides full SQL semantics, including the ability to insert, update, and delete data in the tables. Fabric's data warehouse is unique because it's built on the Lakehouse, which is stored in Delta format and can be queried using SQL. It's designed for use by the whole data team, not just data engineers.

Fabric's data warehouse experience is designed to address these challenges. Fabric enables data engineers, analysts, and data scientists to work together to create and query a data warehouse that is optimized for their specific needs.

In this module, you'll learn about data warehouses in Fabric, create a data warehouse, load, query, and visualize data.

# Understand datat warehouse fundementals
The process of building a modern data warehouse typically consists of:

- *Data ingestion:* _Moving data from source systems into a data warehouse._
- *Data storage:* _Storing the data in a format that is optimized for analytics._
- *Data processing Transforming:* _The data into a format that is ready for consumption by analytical tools._
- *Data analysis and delivery:* _Analyzing the data to gain insights and delivering those insights to the business._

Microsoft Fabric enables data engineers and analysts to ingest, store, transform, and visualize data all in one tool with both a low-code and traditional experience.