import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

URL_DATABASE = "mysql+pymysql://user:userpassword@db:3306/blogapplication"


def create_database_connection():
    """
    Create database connection with retry logic for waiting until MySQL is ready.

    Returns:
        engine: SQLAlchemy engine instance
    """
    retries = 10
    while retries > 0:
        try:
            db_engine = create_engine(URL_DATABASE)
            # Try a simple connection
            conn = db_engine.connect()
            conn.close()
            print("Database connected successfully")
            return db_engine
        except OperationalError:
            print("Database not ready, waiting 5 seconds...")
            retries -= 1
            time.sleep(5)

    raise Exception("Could not connect to the database after multiple retries")


# Create database connection
engine = create_database_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
