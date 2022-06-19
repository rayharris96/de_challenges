from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import psycopg2
import os

default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    "wait_for_downstream": True,
    "start_date": datetime(2022, 6, 19),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

#Create DAG with daily scheduling interval and runs at 1 am
dag = DAG(
    "transformation_v1",
    default_args=default_args,
    schedule_interval="0 1 * * *",
    max_active_runs=1,
)

tables = [
    {
        'task' : 'transform_dataset1',
        'sql': "sql/dataset1.sql",
    },
    {
        'task' : 'transform_dataset2',
        'sql': "sql/dataset2.sql",
    },
]

#Assign tasks with customized task id and sql location
for item in tables:
    transform = PostgresOperator(
        task_id=item['task'],
        sql=item['sql'],
        postgres_conn_id="database",
        dag=dag
    )

    #Instantiate tasks in dag
    transform
