# [START import_module]
import time
import tempfile
import requests
import pandas as pd
from datetime import datetime
from airflow import DAG
from airflow.decorators import task, dag
from os import getenv
from os import path
from minio import Minio
from airflow.operators.dummy import DummyOperator
# [END import_module]

from faker.extract.requestAPI import request_data_as_df
MINIO_PORT = 9000
HOST_URI = getenv('HOST_URI')
BUCKET_NAME = getenv('STAGING')
ACCESS_KEY = getenv('ACCESS_KEY')
SECRET_KEY = getenv('SECRET_KEY')

@dag(schedule_interval = '@daily', start_date=datetime(2022,5,26), catchup = False)
def taskflow():

    @task(task_id='extract')
    def extract_data_as_df() -> None:
        df = request_data_as_df(1000)
        file_name = f'''faker_csv_{datetime.now().strftime('%Y-%m-%d')}'''
        df.to_csv(file_name,)

        return 'extract'

    extract_data_as_df()

dag = taskflow()

