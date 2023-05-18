# Script ingesting data to DB

import os
from pyspark.sql import SparkSession

from service.data_read import create_dataframes
from config.constraints import files, list_of_schemas


spark = (
    SparkSession.builder
    .appName("JSON_Ingestion")
    .master("local")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.4.2")
    .getOrCreate()
)


dataframes = {}

dataframes = create_dataframes(files, list_of_schemas, spark)

dataframes['shops'].show()

print('Przed zapisaem')

for table_name, dataframe in dataframes.items():
    dataframes[table_name].select("*") \
    .write.format("jdbc") \
    .option("url", 'jdbc:postgresql://postgres:5432/example_db') \
    .option("driver", "org.postgresql.Driver") \
    .option("dbtable", table_name) \
    .option("user", "postgres") \
    .option("password", 'postgres') \
    .mode("overwrite") \
    .save()


print("Po zapisie")

spark.stop()