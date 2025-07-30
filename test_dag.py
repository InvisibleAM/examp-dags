from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator

def print_hello():
    print("Hello world from first Airflow DAG!")

with DAG(
    id='hello_world',
    description='Hello World DAG',
    schedule="0 12 * * *",  # Replaces schedule_interval
    start_date=datetime(2017, 3, 20),
    catchup=False,
    tags=["example"]
) as dag:

    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello
    )
