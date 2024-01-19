from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from airflow.sensors.external_task import ExternalTaskSensor

from scripts.data_migration import run_data_migration


dag_args = {
    "owner":"airflow",
    "email_on_falure": False,
    "email_on_retry": False,
    "email": os.environ.get("TARGET_MAIL", "teste@teste.com.br"),
    'depends_on_past': False,
}


with DAG(
    "0002_data_migration",
    start_date=datetime(2024, 1, 18),
    schedule_interval=None,
    default_args=dag_args,
    catchup=False
) as dag:

    excute_python = PythonVirtualenvOperator(
        task_id="execute_migration",
        python_callable=run_data_migration,
        requirements=["pg8000","sqlalchemy"]
    )
