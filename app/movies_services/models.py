from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR, nullable=False)
    duration_min = Column(Integer, nullable=False)
    age_limit = Column(Integer, nullable=False)
    year_release = Column(Integer, nullable=False)
    genre = Column(VARCHAR, nullable=False)
    director = Column(VARCHAR, nullable=False)
    starring = Column(VARCHAR, nullable=False)
    description = Column(Text, nullable=False)
    avatar = Column(Text, nullable=False)