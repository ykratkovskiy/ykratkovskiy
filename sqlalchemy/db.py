from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

#SQLite
url = 'sqlite:///local.db'

#Postgres
#user = 'postgres'
# password = 'y***6'
# host = 'localhost'
# port = 5432
# db = 'postgres'
#url = f'postgresql://{user}:{password}@{host}:{port}/{db}'

engine = create_engine(url,echo=False)
Base = declarative_base()

def execute(*args,**kwargs):
    with engine.connect() as conn:
        return conn.execute(*args,**kwargs) 