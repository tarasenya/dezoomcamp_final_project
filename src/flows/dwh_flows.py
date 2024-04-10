"""
Flows dealig with Spark processing DWH
"""
from pyspark.sql import SparkSession
from src.schemas import spark_schema
from src.definitions import (
    bucket_name,
    project_name,
    dataset,
    table_name,
    HISTORICAL_DATA,
    HEALTH_DATA,
)
from prefect import flow

SPARK_SESSION = (
    SparkSession.builder.appName("Optimize BigQuery Storage")
    .config(
        "spark.jars.packages",
        "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.15.1-beta,com.google.cloud.bigdataoss:gcs-connector:hadoop2-2.1.6",  # noqa E501
    )
    .config(
        "spark.jars",
        "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar",
    )
    .getOrCreate()
)

SPARK_SESSION._jsc.hadoopConfiguration().set(
    "fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem"
)
SPARK_SESSION.conf.set("temporaryGcsBucket", bucket_name)

TABLE_NAME = f"{project_name}.{dataset}.{table_name}"


@flow(name="Summarized historical data", log_prints=True)
def total_number_of_koalas_met():
    """
    Crates an aggregated data, koalas met pro day and writes it to the corresponding BigQuery table.
    """
    print("Preparing the summarized historical data")
    historical_data_table = f"{project_name}.{dataset}.{HISTORICAL_DATA}"

    koala_data = (
        SPARK_SESSION.read.format("bigquery")
        .option("table", TABLE_NAME)
        .schema(spark_schema)
        .load()
    )

    total_koalas_seen = (
        koala_data.groupBy("sightdate")
        .sum("numberofkoala")
        .withColumnRenamed("sum(numberofkoala)", "totalnumberofkoala")
    )

    total_koalas_seen.write.format("bigquery").option(
        "table", historical_data_table
    ).mode("overwrite").save()
    print(f"The data has been written to {historical_data_table}.")
    total_koalas_seen.limit(10).show()


@flow(name="Health data", log_prints=True)
def koala_health_conditions():
    """
    Creates an aggregated data, sighted koalas grouped by the health condition and writes
    to the corresponding BigQuery table.
    """
    print("Preparing the summarized health data.")
    health_data_table = f"{project_name}.{dataset}.{HEALTH_DATA}"
    koala_data = (
        SPARK_SESSION.read.format("bigquery")
        .option("table", TABLE_NAME)
        .schema(spark_schema)
        .load()
    )

    health_data = (
        koala_data.groupBy("koalacondifinal")
        .sum("numberofkoala")
        .withColumnRenamed("sum(numberofkoala)", "totalnumberofkoala")
    )
    health_data.write.format("bigquery").option("table", health_data_table).mode(
        "overwrite"
    ).save()

    print(f"The data has been written to  {health_data_table}.")
    health_data.limit(10).show()
