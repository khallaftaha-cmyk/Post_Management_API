from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor 
from .config import settings


SQLALCHEMY_DATABASE_url = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_url)

SesseionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SesseionLocal()
    try:
        yield db
    finally:
        db.close()


#while True:

    #try :
        #conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
                            #password='khallaf',cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print('DATABASE CONNECTION WAS SUCCEFULL')
        #break
    #except Exception as error:
        #print("Connecting to the database has failed")
        #print("Error:", error)
        #time.sleep(2)