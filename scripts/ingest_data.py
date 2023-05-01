import os
from pyspark.sql import SparkSession
from schemas import adress_schema, customers_schema, employees_schema, products_schema, purchase_schema, representatives_schema, shops_schema


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
        "adress.json",
        "customers.json",     
        "employees.json",
        "products.json",
        "purchase.json",
        "representatives.json",
        "shops.json"
    ]

schemas = {
    "adress": adress_schema,
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
    data = spark.read.option('multiline', True).schema(schemas[table_name]).json(file)
    schema = data.schema
    dataframes[table_name] = data


dataframes['shops'].show()
#dataframes['products'].show()


#    data.write \
#        .jdbc("jdbc:postgresql://localhost:5432/mydatabase", table_name, mode="overwrite", properties=properties)

spark.stop()
