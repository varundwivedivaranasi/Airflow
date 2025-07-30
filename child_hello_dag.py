from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def child_task_func():
    print("Hello from Child DAG!")

default_args = {
    "start_date": datetime(2023, 1, 1)
}

child_dag = DAG(
    dag_id="child_hello_dag",
    default_args=default_args,
    catchup=False,
    tags=["demo"]
)
child_dag.schedule_interval = None  

hello_child = PythonOperator(
    task_id="say_hello_from_child",
    python_callable=child_task_func,
    dag=child_dag
)