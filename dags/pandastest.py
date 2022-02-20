from datetime import datetime, timedelta
from functions import extract, transform, savetodb, savetojson

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.utils.task_group import TaskGroup
# [END import_module]


# [START default_args]
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}
# [END default_args]

# [START instantiate_dag]
with DAG(
    dag_id="demo_email",
    default_args=default_args,
    description='email',
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['Demo'],
) as dag:
    # [END instantiate_dag] 

    send_email_task = EmailOperator(
        task_id='Send_Email',
        to=['test@mailhog.local'],
        subject='Your report today is ready',
        html_content='Please check your dashboard.'
    )
send_email_task