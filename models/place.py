#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, overlaps="place_amenities")
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """getter attribute for reviews"""
            from models import storage
            rvs = []
            reviews = storage.all("Review").values()
            for review in reviews:
                if review.place_id == self.id:
                    rvs.append(review)
            return rvs

        @property
        def amenities(self):
            """getter attribute for amenities"""
            from models import storage
            from models.amenity import Amenity
            amenities_lst = []
            ameninties = storage.all("Ameninty").values()
            for ameninty in ameninties:
                if ameninty.id in self.amenity_ids:
                    amenities_lst.append(ameninty)
            return amenities_lst

        @amenities.setter
        def amenities(self, obj):
            """Adds an amenity to this Place"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self,*args,**kwargs):
        """New Place instance"""
        super().__init__(**kwargs)
