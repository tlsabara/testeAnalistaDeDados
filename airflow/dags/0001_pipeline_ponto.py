import os

from airflow import DAG
from datetime import datetime, timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.utils.trigger_rule import TriggerRule

dag_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": os.environ.get("TARGET_MAIL", "teste@teste.com.br"),
    "retries": 2,
    "retry_delay": timedelta(minutes=10)
}

description = "DAG para avaliar o status dos servidores e tabelas antes de executar o processo de etl"

with DAG(
    dag_id="0001_pipeline_ponto",
    start_date=datetime(2024, 1, 18),
    schedule_interval="0 0 * * *",
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


    trigger_migration = TriggerDagRunOperator(
        task_id="trigger_migration",
        trigger_rule=TriggerRule.ALL_SUCCESS,
        trigger_dag_id="0002_data_migration"
    )

    trigger_analysis = TriggerDagRunOperator(
        task_id="trigger_analysis",
        trigger_rule=TriggerRule.ALL_SUCCESS,
        trigger_dag_id="0003_analysis_dag"
    )

    source_connection >> destination_connection
    destination_connection >> trigger_migration
    destination_connection >> trigger_analysis
