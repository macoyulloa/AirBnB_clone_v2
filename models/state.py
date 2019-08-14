#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
    name """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if HBNB_TYPE_STORAGE=db:
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            allcities = ()
            for key, value in models.storage.all((model.city).items()):
                if value.state.id == self.id:
                allcities.append = value
        return(allcities)
