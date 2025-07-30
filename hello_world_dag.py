from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello, World!")

dag = DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["test"]
)

# Set the schedule after initialization
dag.schedule_interval = None  # Manual trigger only

hello_task = PythonOperator(
    task_id="say_hello_task",
    python_callable=say_hello,
    dag=dag
)