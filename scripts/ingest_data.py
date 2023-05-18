# Script ingesting data to DB

import os
from pyspark.sql import SparkSession
from schemas import address_schema, customers_schema, employees_schema, products_schema, purchase_schema, representatives_schema, shops_schema


spark = (
    SparkSession.builder
    .appName("JSON Ingestion")
    .master("local")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.4.2")
    .getOrCreate()
)

properties = {
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
    "driver": "org.postgresql.Driver"
}

files = [
        "customers.json",
        "address.json",
        "shops.json",
        "employees.json",
        "products.json",
        "purchase.json",
        "representatives.json"
    ]

schemas = {
    "address": address_schema,
    "customers": customers_schema,
    "employees": employees_schema,
    "products": products_schema,
    "purchase": purchase_schema,
    "representatives": representatives_schema,
    "shops": shops_schema
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