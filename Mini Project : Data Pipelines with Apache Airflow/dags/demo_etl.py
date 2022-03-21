from datetime import datetime, timedelta
from functions import extract, transform, savetodb, savetojson

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.operators.bash import BashOperator
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
    dag_id="demo_etl",
    default_args=default_args,
    description='DEMO ETL',
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['Demo'],
) as dag:
# [END instantiate_dag]    

    # [START main_flow]
    extract_task = PythonOperator(
        task_id='Extract_Data',
        python_callable=extract,
    )
    
    transform_task = PythonOperator(
        task_id='Transform_Data',
        python_callable=transform,
    )
    
    with TaskGroup("Load_Data", tooltip="Tasks for Load Data") as load_data_task:
        load_task = PythonOperator(
            task_id='Save_to_JSON',
            python_callable=savetojson,
        )
        
        savetodb_task = PythonOperator(
            task_id='Save_to_DB',
            python_callable=savetodb,
        )
    
    [load_task, savetodb_task]

    send_email_task = EmailOperator(
        task_id='Send_Email',
        to=['test@mailhog.local'],
        subject='Data Pipeline Report is Ready : Succeeded !! ',
        html_content=f'[Notification] Data Pipeline Status : Succeeded !! on {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}'
    )

    clean_data = BashOperator(
        task_id='Clean_Data',
        bash_command='find /opt/airflow/data -name "*.csv" -type f',
    )
    # [END main_flow]

    extract_task >> transform_task >> load_data_task >> clean_data >> send_email_task
