#!/usr/bin/python3
'class definition of a State and an instance Base = declarative_base()'

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    ' class city inherits from Basemodel and base'
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade="delete", backref="cities")
