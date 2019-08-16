#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from sqlalchemy import *


place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False))

metadata = Base.metadata


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
            price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    'Info of the place'

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place")
    amenity_ids = []
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, backref="place_amenities")


    @property
    def amenities(self, obj):
        """returns the list of Amenity instances"""
        amenitys_list = ()
        dict_amenitys = models.storage.all(models.Amenity)
        for key, value in dict_amenitys.items():
            for search_id in self.amenity_ids:
                if value.id == search_id:
                amenitys_list.append(value)
        return(amenitys_list)

    @amenities.setter
    def amenities(self, obj):
        """append method for adding an Amenity.id to attribute amenity_ids"""
        if (type(obj).__Classname__) == Amenity:
            self.amenity_ids.append(obj.id)


