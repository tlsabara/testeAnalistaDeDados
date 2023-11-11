from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from airflow.sensors.external_task import ExternalTaskSensor

from scripts.analise import run_analysis

dag_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_rety": False,
    'depends_on_past': False,
    "retries": 3,
    "retry_delay": timedelta(minutes=15),
    "email": os.environ.get("TARGET_MAIL", "teste@teste.com.br")
}

with DAG(
    "0003_analysis_dag",
    default_args=dag_args,
    start_date=datetime(2023, 11, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    excute_analysis = PythonVirtualenvOperator(
        task_id="excute_analysis",
        python_callable=run_analysis,
        requirements=["pg8000", "sqlalchemy"]
    )
