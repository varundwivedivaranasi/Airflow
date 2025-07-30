from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

def parent_task_func():
    print("Hello from Parent DAG!")

default_args = {
    "start_date": datetime(2023, 1, 1)
}

parent_dag = DAG(
    dag_id="parent_hello_dag",
    default_args=default_args,
    catchup=False,
    tags=["demo"]
)
parent_dag.schedule_interval = None  

hello_parent = PythonOperator(
    task_id="say_hello_from_parent",
    python_callable=parent_task_func,
    dag=parent_dag
)

trigger_child = TriggerDagRunOperator(
    task_id="trigger_child_dag",
    trigger_dag_id="child_hello_dag",
    wait_for_completion=True,
    dag=parent_dag
)

hello_parent >> trigger_child