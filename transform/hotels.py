import json
import os
from functools import partial
import arrow

from google.cloud import bigquery, pubsub_v1

project_name = 'oi-hackaton-vtk2019'
subscriber = pubsub_v1.SubscriberClient()

bigquery_client = bigquery.Client(project=project_name)


def bq_get_or_create_dataset():
    dataset_ref = bigquery_client.dataset('workshop')

    try:
        dataset = bigquery_client.get_dataset(dataset_ref)
    except Exception as e:
        # print("Error:", e)
        # exit(1)
        dataset = bigquery.Dataset(dataset_ref)
        dataset = bigquery_client.create_dataset(dataset)
        print('Dataset {} created.'.format(dataset.dataset_id))
    
    return dataset_ref


def bq_get_or_create_hotels_table(dataset_ref):
    table_ref = dataset_ref.table('hotels')

    try:
        table = bigquery_client.get_table(table_ref)
    except Exception as e:
        # print("Error:", e)
        # exit(1)
        schema = [
            bigquery.SchemaField('destination', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('dt_inserted', 'DATETIME', mode='REQUIRED'),
            # Add fields here
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = bigquery_client.create_table(table)
        print('Table {} created.'.format(table.table_id))
    return table


dataset = bq_get_or_create_dataset()
table = bq_get_or_create_hotels_table(dataset)


if __name__ == "__main__":
    # Start the pubsub subscription here
    pass