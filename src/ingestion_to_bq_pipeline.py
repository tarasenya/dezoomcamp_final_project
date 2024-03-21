import dlt
import pandas as pd
from dlt.destinations.impl.bigquery.bigquery_adapter import bigquery_adapter
from prefect import task
from src.definitions import bucket_name, dataset, table_name
from src.schemas import KoalaScheme


@dlt.resource(columns=KoalaScheme, primary_key="objectid")
def koala_data(resource_name: str, bucket_name: str):
    df = pd.read_csv(f"gs://{bucket_name}/{resource_name}")
    for row in df.to_dict("records"):
        yield row

@task(name='Ingest to BQ')
def ingest_koala_data_to_big_query(
    resource_name: str, bucket_name: str, dataset_name: str, table_name: str
):

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


if __name__ == "__main__":
    ingest_koala_data_to_big_query(
        "my_data.csv",
        bucket_name=bucket_name,
        dataset_name=dataset,
        table_name=table_name,
    )
