from httpx import Limits
from sqlalchemy import insert,select,and_, or_, not_,delete,update,desc
from db import Base,engine,execute
from models import User, Address
from heapq import nlargest

Base.metadata.create_all(engine)

users_data = [
    {'name':'Max', 'fullname': 'Max Padchasha','gender':'male','age':33},
    {'name':'Raman', 'fullname': 'Raman Voitka','gender':'male','age':32},
    {'name':'Alex', 'fullname': 'Alex Trunou','gender':'male','age':34},
    {'name':'Yury', 'fullname': 'Yury Kratkouski','gender':'male','age':35},
    {'name':'Tatsiana', 'fullname': 'Tatsiana Ivankova','gender':'female','age':34},
    {'name':'Vitali', 'fullname': 'Vitali Losik','gender':'male','age':34},
]
def insert_many_users():
    query = insert(User)
    execute (query,users_data) 
# insert_many_users()    

def select_users():    
    query =( 
    select(User.name).order_by(User.age.desc()).limit(3)
        # .join(Address)
        .where(
            (User.gender=='male') &
            ((User.name.like ('Y%')) |
            (User.name.like('A%')))
            )
            )           
                          
    with engine.connect() as conn:
        cursor = conn.execute(query)
        users = list(cursor)
    for i in users:
        print (dict(i))
        
select_users()
    
     
def delete_duplicate_user():
    query = delete (User).where(User.id==2)
    execute(query)
# delete_duplicate_user()


def insert_adress():
    execute(insert(Address)
            .values (email_address='vit_los@mail.ru',user_id=6))
# insert_adress()
    

def update_age():
    query = (update(User)
        .where(User.name=='Tatsiana')
        .values(age=32))
    execute(query)
# update_age()