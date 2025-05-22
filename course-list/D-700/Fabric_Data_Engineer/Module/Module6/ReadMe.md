# Introduction

Relational data warehouses are at the center of most enterprise business intelligence (BI) solutions. While the specific details may vary across data warehouse implementations, a common pattern based on a denormalized, multidimensional schema has emerged as the standard design for a relational data warehouse.

Microsoft Fabric's data warehouse is a modern version of the traditional data warehouse. It centralizes and organizes data from different departments, systems, and databases into a single, unified view for analysis and reporting purposes. Fabric's data warehouse provides full SQL semantics, including the ability to insert, update, and delete data in the tables. Fabric's data warehouse is unique because it's built on the Lakehouse, which is stored in Delta format and can be queried using SQL. It's designed for use by the whole data team, not just data engineers.

Fabric's data warehouse experience is designed to address these challenges. Fabric enables data engineers, analysts, and data scientists to work together to create and query a data warehouse that is optimized for their specific needs.

In this module, you'll learn about data warehouses in Fabric, create a data warehouse, load, query, and visualize data.

## Understand data warehouse fundamentals

The process of building a modern data warehouse typically consists of:

- *Data ingestion:* *Moving data from source systems into a data warehouse.*
- *Data storage:* *Storing the data in a format that is optimized for analytics.*
- *Data processing Transforming:* *The data into a format that is ready for consumption by analytical tools.*
- *Data analysis and delivery:* *Analyzing the data to gain insights and delivering those insights to the business.*

Microsoft Fabric enables data engineers and analysts to ingest, store, transform, and visualize data all in one tool with both a low-code and traditional experience.

## Clone tables

You can create zero-copy table clones with minimal storage costs in a data warehouse. These clones are essentially replicas of tables created by copying the metadata while still referencing the same data files in OneLake. This means that the underlying data stored as parquet files is not duplicated, which helps in saving storage costs.

Table clones are particularly useful in several scenarios.

Development and testing: Clones allow developers and testers to create copies of tables in lower environments, facilitating development, debugging, testing, and validation processes.
Data recovery: In the event of a failed release or data corruption, table clones can retain the previous state of data, enabling data recovery.
Historical reporting: They help create historical reports that reflect the state of data at specific points in time and preserve data at specific business milestones.
You can create a table clone using the CREATE TABLE AS CLONE OF T-SQL command.

To learn more about table clones, see Tutorial: Clone a table using T-SQL in Microsoft Fabric.

Table considerations
After creating tables in a data warehouse, it's important to consider the process of loading data into those tables. A common approach is to use staging tables. In Fabric, you can use T-SQL commands to load data from files into staging tables in the data warehouse.

Staging tables are temporary tables that can be used to perform data cleansing, data transformations, and data validation. You can also use staging tables to load data from multiple sources into a single destination table.

Usually, data loading is performed as a periodic batch process in which inserts and updates to the data warehouse are coordinated to occur at a regular interval (for example, daily, weekly, or monthly).

Generally, you should implement a data warehouse load process that performs tasks in the following order:

Ingest the new data to be loaded into a data lake, applying pre-load cleansing or transformations as required.
Load the data from files into staging tables in the relational data warehouse.
Load the dimension tables from the dimension data in the staging tables, updating existing rows or inserting new rows and generating surrogate key values as necessary.
Load the fact tables from the fact data in the staging tables, looking up the appropriate surrogate keys for related dimensions.
Perform post-load optimization by updating indexes and table distribution statistics.
If you have tables in the lakehouse, and you want to be able to query it in your warehouse - but not make changes - with a Fabric data warehouse, you don't have to copy data from the lakehouse to the data warehouse. You can query data in the lakehouse directly from the data warehouse using cross-database querying.

*IMPORTANT*
Working with tables in the Fabric data warehouse currently has some limitations. See [Tables in data warehousing in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-warehouse/tables) for more information.

## Query and transform data

Now that you know how to implement a data warehouse in Fabric, let's prepare the data for analytics.

There are two ways to query data from your data warehouse. The Visual query editor provides a no-code, drag-and-drop experience to create your queries. If you're comfortable with T-SQL, you may prefer to use the SQL query editor to write your queries. In both cases, you can create tables, views, and stored procedures to query data in the data warehouse and Lakehouse.

There's also a SQL analytics endpoint, where you can connect from any tool.

To create a new query, use the New SQL query button in the menu. You can author and run your T-SQL queries here. In the example below we're creating a new view for analysts to use for reporting in Power BI.
![create-view.png](https://learn.microsoft.com/en-gb/training/wwl/get-started-data-warehouse/media/create-view.png)

# Query data using the Visual query editor

The visual query editor provides an experience similar to the [Power Query online diagram view](https://learn.microsoft.com/en-us/power-query/diagram-view)
Use the **New visual query** button to create a new query.

Drag a table from your data warehouse onto the canvas to get started. You can then use the **Transform** menu at the top of the screen to add:

- columns
- filters
- other transformations to your  query.
You can also use the ( *+* ) button on the visual itself to perform similar transformations:
![visual-query.png](https://learn.microsoft.com/en-gb/training/wwl/get-started-data-warehouse/media/visual-query.png)

# Prepart data for analysis and reporting

A semantic model defines the relationships between the different tables in the semantic model, the rules for how data is aggregated and summarized, and the calculations or measures that are used to derive insights from the data. These relationships and measures are included in the semantic model, which is then used to create reports in Power BI.

You can easily switch between the Data, Query, and Model view Fabric using the menu in the bottom left corner of the screen. The Data view shows the tables in the semantic model, the Query view shows the SQL queries that are used to create the semantic model, and the Model view shows the semantic model.

*TIP*
*See [Analyzre daya in a relational data warehouse](https://learn.microsoft.com/en-us/training/modules/design-multidimensional-schema-to-optimize-analytical-workloads/) to learn more about data models and data warehouse schema.*

# Build relationships

Relationships allow you to connect tables in the semantic model. Create relationships between tables in your data warehouse using a click-and-drag interface in Fabric in the Model view.

[Module 5 Assessment page](https://learn.microsoft.com/en-gb/training/modules/get-started-data-warehouse/8-knowledge-check)

[Module 5 Victory](https://learn.microsoft.com/api/achievements/share/en-gb/NathanBusse-2561/XQ4K6JKY?sharingId=A06D9EE30C453065)

# Summary
In this module, you learned about data warehouses and dimensional modeling, created a data warehouse, loaded, queried, and visualized data, and described semantic models and how they're used for downstream reporting.