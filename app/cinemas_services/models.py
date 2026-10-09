from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Cinema(Base):
    __tablename__ = 'cinema'

    id = Column(Integer, primary_key=True)
    cinema_title = Column(VARCHAR)
    address = Column(VARCHAR)
