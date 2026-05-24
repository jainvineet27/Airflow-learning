import os 
print(os.path.abspath(__file__))
current_dir = os.path.dirname(__file__)
print(current_dir)
file_name="main.py"
file_path = os.path.join(current_dir,  file_name)
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write('print("Hello World")')
else:
    print(f'{file_path} already exist')



from datetime import datetime, timedelta

def mydecorator(func):
    def _(*args, **kwargs) ->int :
        print('This is my decorator')
        print("start time ", datetime.now())        
        #func(*args)
        print("end time ", datetime.now())
        c=  func(*args)
        print(c)
        
    return _

@mydecorator
def load_table(table_name :str, schema_name :str , catalog_name :str) -> str:
    print('Loading data into the table ...',table_name )
    return  ('>>>>>>>>>>>>>>>>>>').join([table_name, schema_name, catalog_name])

def procesS_table():
     print('What should be position of a decorato to handle this code...')
     a=1/0

load_table('orders','dbo','vineetdb')