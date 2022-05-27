# [START import_module]
import pandas as pd
from airflow.models import Variable
from datetime import datetime
from airflow import DAG
from airflow.decorators import task, dag
from airflow.operators.dummy import DummyOperator
from io import BytesIO, StringIO
from faker.extract.requestAPI import request_data_as_df
import boto3
from botocore.client import Config
# [END import_module]
               
@dag(   schedule_interval = '@once'
        , start_date=datetime(2022,5,26)
        , catchup = False
        , retry_exponential_backoff = True
        , retries = 3
        , email_on_failure=True
        , email = 'marlon.saura@gmail.com')
def taskflow():

    @task(task_id='extract')
    def extract_data_as_df() -> None:
        requested_number_of_rows = int(Variable.get("requested_number_of_rows"))
        
        print(requested_number_of_rows)

        df = request_data_as_df(requested_number_of_rows)

        file_name = f'''faker_csv_{datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}'''
        
        s3 = boto3.resource('s3',
                    endpoint_url='http://165.227.255.79:9000/',
                    aws_access_key_id='myaccesskey',
                    aws_secret_access_key='mysecretkey',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

        buffer = BytesIO()

        df.to_csv(buffer, sep=",", index=False, mode="wb", encoding="UTF-8")
        s3.Object("staging", file_name).put(Body=buffer.getvalue())
                

        return f'Successfully extracted {requested_number_of_rows}'

    extract_data_as_df()

dag = taskflow()

