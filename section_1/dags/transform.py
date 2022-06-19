from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

DAG_FOLDER_PATH = os.path.realpath(os.path.join(os.path.abspath(__file__), ".."))
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
        'sql': f'{DAG_FOLDER_PATH}/sql/dataset1.sql',
    },
    {
        'task' : 'transform_dataset2',
        'sql': f'{DAG_FOLDER_PATH}/sql/dataset2.sql',
    },
]

#Assign tasks with customized task id and sql location
for item in tables:
    transform = PostgresOperator(
        task_id=item['task'],
        sql=item['sql'],
        dag=dag
    )

    #Instantiate tasks in dag
    transform
