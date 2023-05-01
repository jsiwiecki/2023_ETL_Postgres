import os
from pyspark.sql.types import StructType, StructField, LongType, StringType, DateType, DoubleType, IntegerType
from pyspark.sql import SparkSession


adress_schema = StructType([
    StructField("address_id", IntegerType(), True),
    StructField("cust_id", IntegerType(), True),
    StructField("street", StringType(), True),
    StructField("post_code", StringType(), True)
])


# Customers schema
customers_schema = StructType([
    StructField("cust_id", LongType(), True),
    StructField("Name", StringType(), True),
    StructField("since", DateType(), True),
    StructField("group", StringType(), True)
])

# Employees schema
employees_schema = StructType([
    StructField("employee_id", LongType(), True),
    StructField("name", StringType(), True),
    StructField("surname", StringType(), True),
    StructField("shop_id", LongType(), True),
    StructField("since", DateType(), True)
])

# Products schema
products_schema = StructType([
    StructField("product_id", LongType(), True),
    StructField("name", StringType(), True),
    StructField("category", StringType(), True),
    StructField("unit_price", DoubleType(), True)
])

# Purchase schema
purchase_schema = StructType([
    StructField("purch_id", LongType(), True),
    StructField("cust_id", LongType(), True),
    StructField("date", DateType(), True),
    StructField("product_id", LongType(), True),
    StructField("amount", IntegerType(), True),
    StructField("total_price", DoubleType(), True),
    StructField("shop_id", LongType(), True),
    StructField("employee_id", LongType(), True)
])

# Representatives schema
representatives_schema = StructType([
    StructField("representative_id", LongType(), True),
    StructField("Name", StringType(), True),
    StructField("Surname", StringType(), True),
    StructField("position", StringType(), True)
])

# Shops schema
shops_schema = StructType([
    StructField("shop_id", LongType(), True),
    StructField("street", StringType(), True),
    StructField("city", StringType(), True),
    StructField("size", StringType(), True)
])



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


#dataframes['shops'].show()


#    data.write \
#        .jdbc("jdbc:postgresql://localhost:5432/mydatabase", table_name, mode="overwrite", properties=properties)

spark.stop()
