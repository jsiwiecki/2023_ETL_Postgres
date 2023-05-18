'''
Module containing constraints
'''
from schemas import (
    ADDRESS_SCHEMA,
    CUSTOMERS_SCHEMA,
    EMPLOYEES_SCHEMA,
    PRODUCTS_SCHEMA,
    PURCHASE_SCHEMA,
    REPRESENTATIVES_SCHEMA,
    SHOPS_SCHEMA
)

files = [
        "customers.json",
        "address.json",
        "shops.json",
        "employees.json",
        "products.json",
        "purchase.json",
        "representatives.json"
    ]

list_of_schemas = {
    "address": ADDRESS_SCHEMA,
    "customers": CUSTOMERS_SCHEMA,
    "employees": EMPLOYEES_SCHEMA,
    "products": PRODUCTS_SCHEMA,
    "purchase": PURCHASE_SCHEMA,
    "representatives": REPRESENTATIVES_SCHEMA,
    "shops": SHOPS_SCHEMA
}