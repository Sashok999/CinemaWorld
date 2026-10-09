from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    name = Column(VARCHAR(60), nullable=False)
    surname = Column(VARCHAR(60), nullable=False)
    hash_pass = Column(VARCHAR, nullable=False)