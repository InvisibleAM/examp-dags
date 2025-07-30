from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator  # replaces DummyOperator
from airflow.operators.python import PythonOperator  # updated import

def print_hello():
    return 'Hello world from first Airflow DAG!'

with DAG(
    dag_id='hello_world',
    description='Hello World DAG',
    schedule_interval='0 12 * * *',  # valid cron: 12:00 PM every day
    start_date=datetime(2017, 3, 20),
    catchup=False,
    tags=["example"]
) as dag:

    start = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello
    )
