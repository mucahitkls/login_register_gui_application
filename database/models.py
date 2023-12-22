from sqlalchemy import Column, Integer, String
from .db_session import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(256), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

