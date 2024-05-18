#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone."""
import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """This class manages storage of hbnb models in db"""
    __engine = None
    __session = None

    def __init__(self):
        """inistantiate the engine"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Apply query on the current database session"""
        objects = {}
        for new_cls in classes:
            if cls is None or cls is classes[new_cls] or cls is new_cls:
                objs = self.__session.query(classes[new_cls]).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """remove on the private session attribute"""
        self.__session.remove()
