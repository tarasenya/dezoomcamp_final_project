from typing import List
from prefect import flow, task
import os
import pandas as pd
from google.cloud import storage, bigquery
from configparser import ConfigParser
from src.schemas import koala_schema
from src.koala_data_processing import query_koala_endpoint, flatten_koala_response, KoalaData

config_parser = ConfigParser()
config_parser.read(filenames='config.ini')

project_name = config_parser.get('GCP', 'project')
dataset = config_parser.get('GCP', 'dataset')
table_name = config_parser.get('GCP', 'table_name')
bucket_name = config_parser.get('GCP', 'bucket_name')

path_to_private_key = r'/home/taras/Documents/secrets/personal_gcp.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)

bucket = client.bucket('ny-green-taxi')



@task(name='Get_koala_data_and_transform_to_tabular_view')
def koala_data_to_tabular_view()->pd.DataFrame:
    current_data = query_koala_endpoint()
    array_of_koala_data: List[KoalaData] = flatten_koala_response(current_data)
    df = pd.DataFrame(array_of_koala_data)
    df['sighttime'] = pd.to_datetime(df['sighttime'], unit='ms')
    return df
  

@flow(name='Koalas_to_GCS')
def koalas_to_gcs():
    df = koala_data_to_tabular_view()
    print(df)
    blob = bucket.blob('my_data.csv')
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')

@flow(name='Koalas_to_BQ')
def koalas_to_bq():
    client = bigquery.Client()
    
    #Set table_id to the ID of the table to create.
    table_id = f'{project_name}.{dataset}.{table_name}'


    #table = bigquery.Table(table_id, schema=koala_schema)
        # Set the external data configuration of the table
    #table = client.create_table(table)  # Make an API request. 

    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    job_config.skip_leading_rows = 1
    job_config.source_format = bigquery.SourceFormat.CSV

    uri = f"gs://{bucket_name}/my_data.csv"
    load_job = client.load_table_from_uri(
            uri, table_id, job_config=job_config
        )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))      


if __name__ == '__main__':
    koalas_to_gcs()
    koalas_to_bq()