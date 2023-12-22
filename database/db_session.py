import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser


def get_db_url():
    config = ConfigParser()
    config.read('..\\login_gui_with_tkinter\\app.config')
    return config['database']['DB_URL']

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname) -%(message)s', filename='app.log', filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname) -8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


DB_URL = get_db_url()
try:
    engine = create_engine(url=DB_URL)
    Localsession = sessionmaker(bind=engine)
    Base = declarative_base()
except Exception as e:
    logging.error(f"An error occurred while setting up the database: {e}", exc_info=True)

