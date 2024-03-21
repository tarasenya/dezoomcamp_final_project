import pyspark
from pyspark.sql import SparkSession
from src.schemas import spark_schema
from src.definitions import bucket_name
spark = SparkSession.builder.appName("Optimize BigQuery Storage").config(
        "spark.jars.packages",
        "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.15.1-beta,com.google.cloud.bigdataoss:gcs-connector:hadoop2-2.1.6",
    ).config("spark.jars", "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar").getOrCreate()

spark._jsc.hadoopConfiguration().set('fs.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem')
spark.conf.set("temporaryGcsBucket",bucket_name)

table = "dataengineeringzoomcamp-409819.week_4_hw.koala"

df = spark.read.format("bigquery").option("table", table).schema(spark_schema).load()

total_koalas_seen = (
    df.groupBy("sightdate")
    .sum("numberofkoala")
    .withColumnRenamed("sum(numberofkoala)", "totalnumberofkoala")
)
total_conditions = (
    df.groupBy("koalacondifinal")
    .sum("numberofkoala")
    .withColumnRenamed("sum(numberofkoala)", "totalnumberofkoala")
)

if __name__ == "__main__":
    total_conditions.write.format("bigquery").option(
        "table", "dataengineeringzoomcamp-409819.week_4_hw.koala_health"
    ).mode('overwrite').save()
    total_conditions.show()
