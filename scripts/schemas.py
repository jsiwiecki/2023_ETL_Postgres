# Module containing SCHEMAS

from pyspark.sql.types import StructType, StructField, LongType, StringType, DateType, DoubleType, IntegerType

# Adress schema
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
