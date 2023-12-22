from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser


def get_db_url():
    config = ConfigParser()
    config.read('..\\app.config')
    return config['database']['DB_URL']


DB_URL = get_db_url()

engine = create_engine(url=DB_URL)
Localsession = sessionmaker(bind=engine)
Base = declarative_base()
