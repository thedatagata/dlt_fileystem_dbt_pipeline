import dlt 
import pandas as pd 
from dlt.destinations import filesystem
from dlt.helpers.dbt import create_runner

try:
    from .fs_source import readers, read_csv
except ImportError:
    from fs_source import (
        readers,
        read_csv
    )

load_duckdb_pipeline = dlt.pipeline(
  pipeline_name='load_duckdb_pipeline',
  dataset_name=dlt.config["duckdb.source_schema"],
  destination=dlt.destinations.duckdb(dlt.config["duckdb.db_file_path"])
)

sessions_file = readers(
    bucket_url=f"{dlt.config["source_data.bucket_name"]/{dlt.config["source_data.folder_name"]}}",
    file_glob=dlt.config["source_data.file_name"]
).read_csv()

run_info = load_duckdb_pipeline.run(sessions_file.with_name(dlt.config["duckdb.source_table"]))

dbt_runner = create_runner(
    None,
    None, 
    working_dir=".", 
    package_location=dlt.config["dbt_repo.repo_url"],
    package_profiles_dir=".", 
    package_profile_name=dlt.config["dbt_repo.package_profile"]
)
dbt_runner.run_all()

load_gcs_pipeline = dlt.pipeline(
    pipeline_name="load_gcs_pipeline",
    dataset_name=dlt.config["destination.filesystem.folder_name"],
    destination=filesystem(
        layout="{table_name}.{ext}"
    )
)

def get_customer_dimensions_df():
    import duckdb
    ga_db = duckdb.connect(dlt.config["duckdb.db_file_path"])
    df = ga_db.query("SELECT * FROM staging.stg_users_dim").df()
    return df

run_info = load_gcs_pipeline.run(get_customer_dimensions_df(), table_name=dlt.config["destination.filesystem.file_name"], loader_file_format="csv")