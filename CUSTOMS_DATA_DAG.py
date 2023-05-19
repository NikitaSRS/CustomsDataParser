from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': datetime(2023, 5, 18),
	'email_on_failure': False,
	'email_on_retry': False,
	'retries': 1,
	'retry_delay': timedelta(minutes=5)
}

dag = DAG(
	'CUSTOMS_DATA_DAG',
	default_args=default_args,
	description='DAG to run main.py once a day',
	schedule_interval=timedelta(days=1)
)

run_script = BashOperator(
	task_id='run_main_py',
	bash_command='cd /opt/***/dags && python3 main.py',
	dag=dag
)