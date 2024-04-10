"""
Module deals with ingesting to BigQuery
"""
import dlt
import pandas as pd
from dlt.destinations.impl.bigquery.bigquery_adapter import bigquery_adapter
from prefect import task
from src.schemas import KoalaScheme


@dlt.resource(columns=KoalaScheme, primary_key="objectid")
def koala_data(resource_name: str, bucket_name: str):
    """
    Loads data from GCP Bucket and produces a generator from rows.
    :param resource_name: path to a csv file.
    :param bucket_name: name of a bucket in GCP storage.
    :yield: row of a pandas dataframe got from csv file.
    """
    df = pd.read_csv(f"gs://{bucket_name}/{resource_name}")
    for row in df.to_dict("records"):
        yield row


@task(name='Ingest to BQ')
def ingest_koala_data_to_big_query(
    resource_name: str, bucket_name: str, dataset_name: str, table_name: str
):
    """
    Ingesting data from a GCP sotrage to a BigQuery dataset.
    :param resource_name: name of a csv file.
    :param bucket_name: name of a bucket.
    :param dataset_name: name oa dataset in a BigQuery.
    :param table_name: name of a table the data will be ingested into in a dataset
    """
    prepared_data = bigquery_adapter(
        koala_data(resource_name=resource_name, bucket_name=bucket_name),
        cluster=["sighttime"],
        partition="sightdate",
        table_description="Koala sighting data",
    )

    koala_pipieline = dlt.pipeline(destination="bigquery", dataset_name=dataset_name)

    koala_pipieline.run(
        data=prepared_data,
        table_name=table_name,
        write_disposition="merge",
        primary_key="objectid",
    )
    print("Koala data has been injested")
