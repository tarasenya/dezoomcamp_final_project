from typing import List
from prefect import flow, task
import pandas as pd
from google.cloud import storage, bigquery
from src.koala_data_processing import (
    query_koala_endpoint,
    flatten_koala_response,
    KoalaData,
)
from src.ingestion_to_bq_pipeline import ingest_koala_data_to_big_query
from src.definitions import table_name, dataset, bucket_name, project_name


path_to_private_key = r"/home/taras/Documents/secrets/personal_gcp.json"
client = storage.Client.from_service_account_json(
    json_credentials_path=path_to_private_key
)

bucket = client.bucket("ny-green-taxi")


@task(name="Get_koala_data_and_transform_to_tabular_view")
def koala_data_to_tabular_view() -> pd.DataFrame:
    current_data = query_koala_endpoint()
    array_of_koala_data: List[KoalaData] = flatten_koala_response(current_data)
    df = pd.DataFrame(array_of_koala_data)
    df["sighttime"] = pd.to_datetime(df["sighttime"], unit="ms")
    return df


@flow(name="Koalas_to_GCS")
def koalas_to_gcs():
    df = koala_data_to_tabular_view()
    print(df)
    blob = bucket.blob("my_data.csv")
    blob.upload_from_string(df.to_csv(index=False), "text/csv")


@flow(name="Koalas_to_BQ")
def koalas_to_bq():
    client = bigquery.Client()

    table_id = f"{project_name}.{dataset}.{table_name}"
    print(f"Writing into {table_id}")
    ingest_koala_data_to_big_query(
        resource_name="my_data.csv",
        bucket_name=bucket_name,
        dataset_name=dataset,
        table_name=table_name,
    )

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))


if __name__ == "__main__":
    koalas_to_bq()
