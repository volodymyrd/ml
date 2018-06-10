# sudo apt-get --fix-missing install python-pandas python-numpy python-matplotlib

import pandas as pd
# from pandas.tools.plotting import autocorrelation_plot
# from pandas.tools.plotting import scatter_matrix

import numpy as np

import matplotlib.pyplot as plt

import os

from google.cloud import bigquery

import tensorflow as tf

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/vova/Downloads/cloud-training-50c4f6cb3935.json'

client = bigquery.Client()

job_config = bigquery.QueryJobConfig()
job_config.dry_run = True
job_config.use_query_cache = False
# query_job = client.query(
#     ('SELECT name, COUNT(*) as name_count '
#      'FROM `bigquery-public-data.usa_names.usa_1910_2013` '
#      "WHERE state = 'WA' "
#      'GROUP BY name'),
#     # Location must match that of the dataset(s) referenced in the query.
#     location='US',
#     job_config=job_config)  # API request

# A dry run query completes immediately.
# assert query_job.state == 'DONE'
# assert query_job.dry_run
#
# print("This query will process {} GB.".format(
#     query_job.total_bytes_processed / 1000000000))

select = 'SELECT Date, Close FROM '

# S&P 500 (US)
sql = select + '`bingo-ml-1.market_data.snp`'
snp = client.query(sql).to_dataframe().set_index('Date')

# NYSE Composite (US)
sql = select + '`bingo-ml-1.market_data.nyse`'
nyse = client.query(sql).to_dataframe().set_index('Date')

# Dow Jones Industrial Average (US)
sql = select + '`bingo-ml-1.market_data.djia`'
djia = client.query(sql).to_dataframe().set_index('Date')

# Nikkei 225 (Japan)
sql = select + '`bingo-ml-1.market_data.nikkei`'
nikkei = client.query(sql).to_dataframe().set_index('Date')

# Hang Seng (Hong Kong)
sql = select + '`bingo-ml-1.market_data.hangseng`'
hangseng = client.query(sql).to_dataframe().set_index('Date')

# FTSE 100 (UK)
sql = select + '`bingo-ml-1.market_data.ftse`'
ftse = client.query(sql).to_dataframe().set_index('Date')

# DAX (Germany)
sql = select + '`bingo-ml-1.market_data.dax`'
dax = client.query(sql).to_dataframe().set_index('Date')

# All Ords (Australia)
sql = select + '`bingo-ml-1.market_data.aord`'
aord = client.query(sql).to_dataframe().set_index('Date')

closing_data = pd.DataFrame()

closing_data['snp_close'] = snp['Close']
closing_data['nyse_close'] = nyse['Close']
closing_data['djia_close'] = djia['Close']
closing_data['nikkei_close'] = nikkei['Close']
closing_data['hangseng_close'] = hangseng['Close']
closing_data['ftse_close'] = ftse['Close']
closing_data['dax_close'] = dax['Close']
closing_data['aord_close'] = aord['Close']

# Pandas includes a very convenient function for filling gaps in the data.
closing_data = closing_data.fillna(method='ffill')

print(closing_data.describe());
