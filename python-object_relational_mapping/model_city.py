#!/usr/bin/python3
"""
Contains the class definition of a City
and inherits from Base (imported from model_state).
"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    City class inherits from Base and links to MySQL table cities.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
