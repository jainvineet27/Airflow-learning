from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from dotenv import load_dotenv
from airflow.decorators import task
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json
import requests
from airflow.utils.dates import days_ago
import os 

default_args = {
    'owner': 'airflow',
    "use hook" :"True , to push the data into postgres",
}

load_dotenv()

with DAG( dag_id="nasa_apod_postgres",
         start_date=days_ago(1),
         schedule_interval='@daily',
         catchup=False,        
    ) as dag:
    
    @task(task_id="create_table")
    def create_table():
        webhook = PostgresHook(postgres_conn_id='my_postgres_connection')

        create_table_query = """
        CREATE TABLE IF NOT EXISTS nasa_apod (
            id SERIAL PRIMARY KEY,
            date DATE,
            title TEXT,
            explanation TEXT,
            url TEXT,
            media_type VARCHAR(50)
        );
        """
        
        webhook.run(create_table_query)
    
    
    extract_nasa_apod = SimpleHttpOperator(
        task_id='extract_nasa_apod',
        method='GET',
        http_conn_id='nasa_api',
        endpoint='planetary/apod',
        data = {"api_key" :"{conn.nasa_api_extra_dejson.api_key}"}
        response_filter=lambda response: response.json()
    )


    @task(task_id="api_call")
    def api_call():
        API_KEY = os.getenv("NASA_API_KEY")
        url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API call failed with status code {response.status_code}")
        
    
    @task(task_id="transform_data")
    def transform_data(response):
        transformed_data = {
            'date': response.get('date', ''),
            'title': response.get('title', ''),
            'explanation': response.get('explanation', ''),
            'url': response.get('url', ''),
            "media_type": response.get('media_type', '')
        }
        return transformed_data

    @task(task_id="load_to_postgres")
    def load_to_postgres(transformed_data):
        #INitalize the PostgresHook to connect to the database using the connection ID defined in Airflow
        webhook = PostgresHook(postgres_conn_id='my_postgres_connection')

        insert_query = """
        INSERT INTO nasa_apod (date, title, explanation, url, media_type)
        VALUES (%s, %s, %s, %s, %s);
        """
        
        #execute the insert query with the transformed data using the run method of the PostgresHook
        #what are these parameters? 
        #these are the values that we want to insert into the database, 
        # and they are passed as a tuple in the same order as the placeholders in the query
        webhook.run(insert_query, parameters=(
            transformed_data['date'],
            transformed_data['title'],
            transformed_data['explanation'],
            transformed_data['url'],
            transformed_data['media_type']
        ))

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