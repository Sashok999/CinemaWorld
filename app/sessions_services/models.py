from sqlalchemy import Column, Integer, VARCHAR, Date
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer, primary_key=True)
    session_date = Column(Date, nullable=False)
    session_time = Column(TIMESTAMP, nullable=False)
    price = Column(Integer, nullable=False)
