from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def ingest(): ...
def transform(): ...
def materialize_features(): ...
def train_and_register(): ...
def deploy_api(): ...

with DAG(
    dag_id="credit_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False,
    default_args={"owner":"risk-platform"}
):
    t1 = PythonOperator(task_id="ingest", python_callable=ingest)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="materialize_features", python_callable=materialize_features)
    t4 = PythonOperator(task_id="train_register", python_callable=train_and_register)
    t5 = PythonOperator(task_id="deploy_api", python_callable=deploy_api)

    t1 >> t2 >> t3 >> t4 >> t5
