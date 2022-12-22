#!/usr/bin/python3
"""
This script defines a City class that inherits from
Base class to work with MySQLAlchemy ORM.
"""

from model_state import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The City id of the class
        name (str): The City name of the class
        state_id (int): The State id of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")
