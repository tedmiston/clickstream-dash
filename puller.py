"""
Fetch data from Airflow's metadata database.
"""

import datetime
import os
import time

import pandas as pd
import psycopg2

AIRFLOW_POSTGRES = os.environ['AIRFLOW_POSTGRES']

conn = psycopg2.connect(AIRFLOW_POSTGRES)

all_df = pd.DataFrame()

i = 0
while True:
# for i in range(2):
    print(f'run {i}')
    time.sleep(60)
    # time.sleep(5)

    ts = datetime.datetime.now()
    df = pd.read_sql('select state, count(*) from task_instance group by state;', conn)
    df['timestamp'] = ts

    all_df = all_df.append(df, ignore_index=True, verify_integrity=True)
    # all_df = all_df.append(df)

    # del df

    all_df.to_json('data.json')
    i += 1
