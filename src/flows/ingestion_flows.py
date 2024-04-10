"""
Flows dealing with data ingestion and transfer
"""
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
from datetime import datetime


@task(name="Get_koala_data_and_transform_to_tabular_view")
def koala_data_to_tabular_view(where_query) -> pd.DataFrame:
    """
    Queries the SightedKoala endpoint using where_query, flattens the response
    and saves it as pandas DataFrame.
    :param where_query: defines the date range when a koala has been sighted.
    :return: pandas DataFrame representation of processed koala sighting data.
    """
    current_data = query_koala_endpoint(where_query=where_query)
    array_of_koala_data: List[KoalaData] = flatten_koala_response(current_data)
    df = pd.DataFrame(array_of_koala_data)
    df["sighttime"] = pd.to_datetime(df["sighttime"], unit="ms")
    df["sightdate"] = df["sighttime"].apply(lambda x: x.date())
    return df


@flow(name="Koalas_to_GCS", log_prints=True)
def koalas_to_gcs(source_name, where_query):
    """
    :param source_name: name of a file we save koala sighting data
    :param where_query: defines the date range when a koala has been sighted.
    """
    client = storage.Client(project=project_name)

    bucket = client.bucket(bucket_name)
    df = koala_data_to_tabular_view(where_query)
    blob = bucket.blob(source_name)
    blob.upload_from_string(df.to_csv(index=False), "text/csv")


@flow(name="Koalas to BQ", log_prints=True)
def koalas_to_bq(source_name, where_query):
    """
    Loads preprocessed koala sighting data to the BigQuery table.
    :param source_name:  name of a file we have saved koala sighting data
    :param where_query: defines the date range when a koala has been sighted.
    """

    koalas_to_gcs(source_name, where_query)
    client = bigquery.Client(project=project_name)

    table_id = f"{project_name}.{dataset}.{table_name}"
    print(f"Writing into {table_id}")
    ingest_koala_data_to_big_query(
        resource_name=source_name,
        bucket_name=bucket_name,
        dataset_name=dataset,
        table_name=table_name,
    )

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))


@flow(name="Current koalas sighting to BQ", log_prints=True)
def current_koalas_to_bq():
    """
    Loads current preprocessed koala sighting data to the BigQuery table.
    """
    source_name = f"koala_{datetime.now().date()}.csv"
    where_query = r"sighttime+%3E+CURRENT_TIMESTAMP+-+INTERVAL+%271%27+DAY"
    koalas_to_bq(source_name, where_query)


@flow(name="Initial koalas sighting to BQ", log_prints=True)
def initial_state_koalas_to_bq():
    """
    Loads historical koala sighting data to the BigQuery table. Used only once when the project is
    started.
    """
    source_name = "koala_initial.csv"
    where_query = r"sighttime+%3E+DATE+%272023-01-01%27"
    koalas_to_bq(source_name, where_query)
