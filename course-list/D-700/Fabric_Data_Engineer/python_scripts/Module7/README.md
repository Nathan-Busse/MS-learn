# Introduction

[Microsoft Fabric Data Warehouse](https://learn.microsoft.com/en-us/fabric/data-warehouse/) is a complete platform for data, analytics, and AI (Artificial Intelligence). It refers to the process of storing, organizing, and managing large volumes of structured and semi-structured data.

Data warehouse in Microsoft Fabric is powered up with Synapse Analytics by offering a rich set of features that make it easier to manage and analyze data. It includes advanced query processing capabilities, and supports the full transactional T-SQL capabilities like an enterprise data warehouse.

Unlike a dedicated SQL pool in Synapse Analytics, a warehouse in Microsoft Fabric is centered around a single data lake. The data in the Microsoft Fabric warehouse is stored in the Parquet file format. This setup allows users to focus on tasks such as data preparation, analysis, and reporting. It takes advantage of the SQL engine’s extensive capabilities, where a unique copy of their data is stored in [Microsoft OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview).

![https://learn.microsoft.com/en-gb/training/wwl-data-ai/load-data-into-microsoft-fabric-data-warehouse/media/1-access-onelake-data-other-tools.png](https://learn.microsoft.com/en-gb/training/wwl-data-ai/load-data-into-microsoft-fabric-data-warehouse/media/1-access-onelake-data-other-tools.png#lightbox)

## Understand the ETL (Extract, Transform, and Load) process

ETL provides the foundation for data analytics and data warehouse workstreams. Let's review some aspects of data manipulation in an ETL process.

![table1.jpeg](course-list/D-700/Fabric_Data_Engineer/python_scripts/Module7/table1.jpeg)

All these steps in the ETL process can run in parallel depending on the scenario. As soon as some data is ready, it's loaded without waiting for the previous steps to be completed.

In the next units, we'll explore various ways of loading data in a warehouse, and how they can facilitate the tasks of building a data warehouse workload.

Explore data load strategies
Completed
100 XP
6 minutes
In Microsoft Fabric, there are many ways you can choose to load data in a warehouse. This step is fundamental as it ensures that high-quality, transformed, or processed data is integrated into a single repository.

Also, the efficiency of data loading directly impacts the timeliness and accuracy of analytics, making it vital for real-time decision-making processes. Investing time and resources in designing and implementing a robust data loading strategy is essential for the success of the data warehouse project.

Understand data ingestion and data load operations
While both processes are part of the ETL (Extract, Transform, Load) pipeline in a data warehouse scenario, they usually serve different purposes. Data ingestion/extract is about moving raw data from various sources into a central repository. On the other hand, data loading involves taking the transformed or processed data and loading it into the final storage destination for analysis and reporting.

Fabric data warehouses and lakehouses automatically store their data in OneLake using the Delta Parquet format.

Stage your data
You might have to build and work with auxiliary objects involved in a load operation, such as tables, stored procedures, and functions. These auxiliary objects are commonly known as staging. Staging objects act as temporary storage and transformation areas. They can either share resources with a data warehouse or reside in their own storage area.

Staging serves as an abstraction layer, simplifying and facilitating the load operation to the final tables in the data warehouse.