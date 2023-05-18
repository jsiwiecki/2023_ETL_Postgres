'''
Module containing read functions
'''
import os


def create_dataframes(files, list_of_schemas, spark):
    dataframes = {}
    for file in files:
        table_name = os.path.splitext(file)[0]
        data = spark.read.option('multiline', True).schema(list_of_schemas[table_name]).json(f'data/{file}')
        schema = data.schema
        dataframes[table_name] = data
    return dataframes