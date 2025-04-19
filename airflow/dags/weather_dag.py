from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG("weather_pipeline",
         default_args=default_args,
         schedule_interval="@daily",
         catchup=False) as dag:

    extract = BashOperator(
        task_id="extract_weather",
        bash_command="python /opt/airflow/scripts/extract_weather.py"
    )

    transform = BashOperator(
        task_id="transform_weather",
        bash_command="python /opt/airflow/scripts/transform_weather.py"
    )

    load = BashOperator(
        task_id="load_weather",
        bash_command="python /opt/airflow/scripts/load_to_postgres.py"
    )

    extract >> transform >> load