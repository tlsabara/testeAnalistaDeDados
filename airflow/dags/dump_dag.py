from datetime import datetime, timedelta

import requests
from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor

dag_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": True,
    "email": "thi.sil.sab@gmail.com",
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}

dag_desc = "Esta é uma DAG de teste"

def validate_http_sensor(response: requests.Response):
    return response.status_code == 200 and "name" in response.text


with DAG(
    dag_id="just_a_test",
    start_date=datetime(2023, 11, 2),
    schedule_interval="@daily",
    default_args=dag_args,
    description=dag_desc,
    catchup=False
) as dag:

    site_avaliable = HttpSensor(
        task_id="is_site_avaliable",
        http_conn_id="url_test",
        endpoint="api",
        response_check=validate_http_sensor,
        poke_interval=5,
        timeout=20
    )

    site_avaliable_pt2 = HttpSensor(
        task_id="is_site_avaliable_2",
        http_conn_id="url_test",
        endpoint="api",
        response_check=validate_http_sensor,
        poke_interval=5,
        timeout=20
    )

    # precedencia
    site_avaliable >> site_avaliable_pt2
