# **Clean, Test, and Model Data in Cloud Blob Storage to Create a Staging Area for Data to be Consumed by Downstream Business Applications**

*This repo is an example of how one could create a single source of truth within the data lake to be consumed by downstream business applications like CDPs, Data Warehouses, Customer Engagement Platforms, etc.* 

*I plan to continue to build on this to explore the idea that most data processing jobs don't actually deal with "Big Data", and that we can move some of these processing jobs out of the warehouse and into the data lake with the advent of technologies like DuckDB, file formats like parquet, and file metadata management systems like Iceberg. This architecture is coined as the Dual Engine Data Stack with the aim of combatting cloud compute costs.*

[Small Data Manifesto](https://motherduck.com/blog/small-data-manifesto/)

### Technologies 

- [DLT](https://dlthub.com/docs/intro): *DLT makes the L in ETL trivial with some pretty slick functionality baked in that you likely wouldn't think of when building one off ETL jobs*
- [DBT](https://docs.getdbt.com/docs/introduction): *DBT focuses on the T in ETL and makes it possible to bring analysts with domain knowledge into the data producing engineering workflow.*
- [DuckDB](https://duckdb.org/docs/api/python/overview): *Light-weight analytics database engine that is very efficient and super fast and makes local development and single machine deployments possible*


### **Installation and Set Up** 

1. Clone this repo, create a pyenv environment, and 



