import pandas as pd
# from pandas.tools.plotting import autocorrelation_plot
# from pandas.tools.plotting import scatter_matrix

import numpy as np

import matplotlib.pyplot as plt

# import google.datalab.bigquery as bq

import os

from google.cloud import bigquery

import tensorflow as tf

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/vova/Downloads/cloud-training-50c4f6cb3935.json'

client = bigquery.Client()

job_config = bigquery.QueryJobConfig()
job_config.dry_run = True
job_config.use_query_cache = False
query_job = client.query(
    ('SELECT name, COUNT(*) as name_count '
     'FROM `bigquery-public-data.usa_names.usa_1910_2013` '
     "WHERE state = 'WA' "
     'GROUP BY name'),
    # Location must match that of the dataset(s) referenced in the query.
    location='US',
    job_config=job_config)  # API request

# A dry run query completes immediately.
assert query_job.state == 'DONE'
assert query_job.dry_run

print("This query will process {} GB.".format(
    query_job.total_bytes_processed / 1000000000))

# snp = bq.Query.from_table(bq.Table('bingo-ml-1.market_data.snp'),
#                           fields=['Date', 'Close']).execute().result().to_dataframe().set_index('Date')
