#!/usr/bin/python3
"""This is the database storage class for AirBnB"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        " Starts the engine to connect with the DataBase "
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        " List all the objects taking in account the object class"
        dict_all = {}
        if cls is None:
            for cls_name in [State, City, User, Place]:
                for each_cls in self.__session.query(cls_name).all():
                    key = "{}.{}".format(type(each_cls).__name__, each_cls.id)
                    dict_all[key] = each_cls
        else:
            cls_all = self.__session.query(cls).all()
            for each_cls in cls_all:
                key = "{}.{}".format(type(each_cls).__name__, each_cls.id)
                dict_all[key] = each_cls
        return (dict_all)

    def new(self, obj):
        " creating a new object inside the table "
        self.__session.add(obj)

    def save(self):
        " commit all changes of the current session "
        self.__session.commit()

    def delete(self, obj=None):
        " delete from the current database session "
        if obj:
            obj.delete(synchronize_session=False)
            self.save()

    def reload(self):
        " create all tables and create the current session"
        Base.metadata.create_all(self.__engine)
        ses_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_fac)
        self.__session = Session()
