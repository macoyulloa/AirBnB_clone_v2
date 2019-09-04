#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
    name """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            'list of City instances with state_id equals the current State.id'
            allcities = []
            filter_cities = models.storage.all(models.city.City)
            for key, value in filter_cities.items():
                if value.state_id == self.id:
                    allcities.append(value)
            return(allcities)
