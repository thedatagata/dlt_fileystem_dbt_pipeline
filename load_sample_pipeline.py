import dlt 
import pandas as pd 
from dlt.destinations import filesystem

load_sample_data_pipeline = dlt.pipeline(
    pipeline_name='load_sample_data_pipeline',
    destination=filesystem(
        layout="{table_name}.{ext}"
    ),
    dataset_name='src_google_analytics'
)

load_sample_data_pipeline.run(pd.read_csv('src_ga_sessions_fct.csv'), table_name='src_ga_sessions_fct', loader_file_format='csv')