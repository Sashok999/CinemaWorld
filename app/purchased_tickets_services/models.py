from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  nullable=False)
    cinema_id = Column(Integer, nullable=False)
    row = Column(Integer, nullable=False)
    place = Column(Integer, nullable=False)
