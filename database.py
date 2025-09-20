# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# #URL_DATABASE = "mysql+pymysql://Chinthaka:Sa!123456789@localhost:3306/blogapplication" #admin

# #URL_DATABASE = "mysql+pymysql://admin:Sa!123456789@blogapplication.ctywmsickt9z.ap-southeast-1.rds.amazonaws.com:3306/blogapplication"

# URL_DATABASE = "mysql+pymysql://user:userpassword@db:3306/blogapplication"




# engine  =  create_engine(URL_DATABASE)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

URL_DATABASE = "mysql+pymysql://user:userpassword@db:3306/blogapplication"

# Retry logic for waiting until MySQL is ready
retries = 10
while retries > 0:
    try:
        engine = create_engine(URL_DATABASE)
        # Try a simple connection
        conn = engine.connect()
        conn.close()
        print("Database connected successfully")
        break
    except OperationalError:
        print("Database not ready, waiting 5 seconds...")
        retries -= 1
        time.sleep(5)
else:
    raise Exception("Could not connect to the database after multiple retries")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
