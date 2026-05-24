from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.decorators import task
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json
import requests
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    "use hook" :"True , to push the data into postgres",
}

with DAG( dag_id="nasa_apod_postgres",
         start_date=days_ago(1),
         schedule_interval='@daily',
         catchup=False,        
         ) as dag:
    
    
    def create_table():
        webhook = PostgresHook(postgres_conn_id='postgres_default')

        create_table_query = """
        CREATE TABLE IF NOT EXISTS nasa_apod (
            id SERIAL PRIMARY KEY,
            date DATE,
            title TEXT,
            explanation TEXT,
            url TEXT
        );
        """
        
        webhook.run(create_table_query)
        

''' 
Steps 
1 task to create table if not exist  
2 Extract the NASA APOD Astronomy picture of the day ... data using the API and load it into Postgres database.
3 transform pick the infromation that I need to save 
4 send to postgres database

5 verify the data DBViewer to connect any database and check the data


6 We are going to define the taks dependency in the end of the code, 
so that we can easily read the code and understand the flow of the data.
'''