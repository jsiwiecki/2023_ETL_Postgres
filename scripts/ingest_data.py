# Script ingesting data to DB

import os
from pyspark.sql import SparkSession
from constraints import files
from schemas import (
    ADDRESS_SCHEMA,
    CUSTOMERS_SCHEMA,
    EMPLOYEES_SCHEMA,
    PRODUCTS_SCHEMA,
    PURCHASE_SCHEMA,
    REPRESENTATIVES_SCHEMA,
    SHOPS_SCHEMA
)


spark = (
    SparkSession.builder
    .appName("JSON Ingestion")
    .master("local")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.4.2")
    .getOrCreate()
)

#properties = {
#    "user": os.environ["POSTGRES_USER"],
#    "password": os.environ["POSTGRES_PASSWORD"],
#    "driver": "org.postgresql.Driver"
#}

schemas = {
    "address": ADDRESS_SCHEMA,
    "customers": CUSTOMERS_SCHEMA,
    "employees": EMPLOYEES_SCHEMA,
    "products": PRODUCTS_SCHEMA,
    "purchase": PURCHASE_SCHEMA,
    "representatives": REPRESENTATIVES_SCHEMA,
    "shops": SHOPS_SCHEMA
}

dataframes = {}

for file in files:
    table_name = os.path.splitext(file)[0]
    data = spark.read.option('multiline', True).schema(schemas[table_name]).json(f'data/{file}')
    schema = data.schema
    dataframes[table_name] = data

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