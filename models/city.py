#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", cascade="all, delete", backref="cities")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        def places(self):
            """getter attribute for places"""
            from models import storage
            all_places = storage.all("Place")
            return [place for place in all_places.values() if place.city_id == self.id]
        
    def __init__(self,*args,**kwargs):
        """New City instance"""
        super().__init__(*args,**kwargs)
