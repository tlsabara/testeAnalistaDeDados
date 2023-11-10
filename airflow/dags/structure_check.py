from airflow import DAG
from datetime import datetime, timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator

dag_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "thi.sil.sab@gmail.com",
    "retries": 2,
    "retry_delay": timedelta(minutes=10)
}

description = "DAG para avaliar o status dos servidores e tabelas antes de executar o processo de etl"

with DAG(
    dag_id="0001_structure_check",
    start_date=datetime(2023, 11, 2),
    schedule_interval="@daily",
    default_args=dag_args,
    description=description,
    catchup=False
) as dag:

    source_connection = PostgresOperator(
        task_id="check_src_server",
        sql="SELECT * FROM t_ponto",
        postgres_conn_id="source_db_server__postgres"
    )

    destination_connection = PostgresOperator(
        task_id="check_target_server",
        sql="select * from pg_catalog.pg_database",
        postgres_conn_id="target_db_server__postgres"
    )

    source_connection >> destination_connection
