# Step-1 Import the required modules &  libraries
from airflow import DAG
from airflow.opertors.bash import BashOpertor
from airflow.opertors.python import PythonOpertor
from datetime import datetime, timedelta


# step-2 Define the default arguments
default_args={
    'owner':'airlow',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':2,
    'retry_delay':timedelta(minutes=2),
    'Execution_timeout':timedelta(hour=1)
    }

# step-3 Define the DAG object
with DAG(
    dag_id='Hello_world',
    default_args=default_args,
    description='A simple DAG',
    start_date=datetime(2025,11,13),
    schedule_interval='@daily',
    Catchup=False,
    ) as dag : 
# step-4 Define the tasks & operators
        say_hello=BashOpertor(
        task_id='say_hello',
        bash_command='echo"Hello_world - This is my first DAG!"'
        )

        say_bye=BashOpertor(
        task_id='say_bye',
        bash_command='echo"Goodbye! See you later!"',
        )

        add_items=PythonOpertor(
        taskk_id='add_items',
        python_callable= 2+3
        )       
# step-5 Set the task dependencies
say_hello >> add_items >> say_bye


