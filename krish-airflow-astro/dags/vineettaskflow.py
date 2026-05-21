from airflow import DAG
from datetime import datetime , timedelta
from airflow.decorators import task 
import random
# define the sequence 
'''

Taskflow API
@task decorator can be used to make takss in the ariflow 
more cleanser and intutiive wya
wihtout using PythonOperator 
previous we have seen 
PythonOperator( task_id ='' , python_callable , context=True )

'''

with DAG ( name ='vineet_api_flow' , start_date = datetime.now() , 
          schedule_interval ='@once', 
          catch=False) as dag:
  
   @task
   def start_number():
      no = random.randint(1,111)
      print(f' my intiail number is >>>> {no}')
      return no
   
   @task
   def add_five(initial_value):
      new_value = initial_value + 5
      print(f'after adding 5 >>>> {new_value}')
      return new_value

   @task
   def multiply_by_two(initial_value):
        new_value = initial_value * 2
        print(f'after multiplying by 2 >>>> {new_value}')
        return new_value
    
   @task
   def substract_three(initial_value):
        new_value = initial_value - 3 if initial_value >= 3 else 0
        print(f'after substracting 3 >>>> {new_value}')
        return new_value
   
   @task
   def square_number(input :int) -> int:
       new_value = input**2
       print(f'the output for the square number is >>>>> {new_value}')
       return new_value
   
   ## Set the taks depenendcies
   start_value = start_number()
   added_value = add_five(start_value)
   multiply_value = multiply_by_two(added_value)
   substract_result = substract_three(multiply_value)
   final = square_number(substract_result)



