# **Clean, Test, and Model Data in Cloud Blob Storage to Create a Staging Area for Data to be Consumed by Downstream Business Applications**

*This repo is an example of how one could create a single source of truth within the data lake to be consumed by downstream business applications like CDPs, Data Warehouses, Customer Engagement Platforms, etc.* 

*I plan to continue to build on this to explore the idea that most data processing jobs don't actually deal with "Big Data", and that we can move some of these processing jobs out of the warehouse and into the data lake with the advent of technologies like DuckDB, file formats like parquet, and file metadata management systems like Iceberg. This architecture is coined as the Dual Engine Data Stack with the aim of combatting cloud compute costs.*

[Small Data Manifesto](https://motherduck.com/blog/small-data-manifesto/)

### Technologies 

- [DLT](https://dlthub.com/docs/intro): *DLT makes the L in ETL trivial with some pretty slick functionality baked in that you likely wouldn't think of when building one off ETL jobs*
- [DBT](https://docs.getdbt.com/docs/introduction): *DBT focuses on the T in ETL and makes it possible to bring analysts with domain knowledge into the data producing engineering workflow.*
- [DuckDB](https://duckdb.org/docs/api/python/overview): *Light-weight analytics database engine that is very efficient and super fast and makes local development and single machine deployments possible*


### **Installation and Set Up** 

- [Set Up a PyEnv Environment](https://motherduck.com/blog/small-data-manifesto/)

*Open your terminal and run the following*

1. Run `pyenv --version` to see if pyenv is installed
2. Run `pyenv versions` to see which versions of Python are available on your machine
3. This was developed using 3.11.3 but should work with 3.8+
4. Run `pyenv virtualenv {python_version} dlt_dev
5. Run `pyenv activate dlt_dev` 
6. Run `pyenv which pip` to ensure python packages will be installed to correct location
7. Run `pip install -r requirements.txt` 
- OPTIONAL: Run `pip freeze > frozen-requirements.txt` to see what has been installed

- [Create a Google Cloud Storage Bucket](https://cloud.google.com/storage/docs/creating-buckets)

1. Create a new Google Cloud Console project named **dlt_demo-walkthrough**
2. Navigate to Google Cloud Storage
3. Create a new bucket named: **dlt-demo_source-data** 
4. Choose a single region near you
5. Standard storage is fine
6. Uniform Control Access is fine for the purposes of this walkthrough
7. No need for any data protection 
8. Google-managed encryption key 
9. Create
10. Create another bucket named **dlt-demo_staging-data** and follow the same steps

- [Create a Service Account with Bucket Access](https://cloud.google.com/iam/docs/service-accounts-create) 

1. Navigate to IAM & Admin Service >> Service Accounts >> +CREATE SERVICE ACCOUNT
2. Name: **dlt_demo-service_account** 
3. Role: **Storage Admin**
4. Create and then click the 3 dots next to the newly created service account and navigate to **Manage Keys** 
5. Add Key >> Create New Key >> JSON >> Create
6. Move the downloaded JSON file somewhere safe and open it using your IDE of choice
7. Copy the private key and project id into secrets-example.toml and rename it to secrets.toml

- [DLT Configuration and Secrets](https://dlthub.com/docs/general-usage/credentials)

1. Make sure that everything in the config-example.toml file matches the objects you created in GCS and rename to config.toml if everything looks good 

- [Remote DBT Project](https://dlthub.com/docs/dlt-ecosystem/transformations/dbt/) 

1. Fork this [DBT Project](https://github.com/thedatagata/dlt_dbt_models) 
2. If you dont have GIT setup, here is a [walkthrough](https://www.freecodecamp.org/news/setup-git-on-mac/). 


### **Running the Project** 

1. Upload the sample source data 

- You can go into your config.toml file and change the destination.filesystem config to point to the source bucket, set the schema_name to src_google_analytics, and run the load_sample_pipeline.py script

- Alternatively, you can manually create the src_google_analytics folder within your dlt-demo_source-data bucket and then upload the file

2. Reset the config file if you chose to use the load_sample_pipeline option from above

3. ??? Create a folder named data as git wont track empty folders ???

4. Profit









