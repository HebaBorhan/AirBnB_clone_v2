#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Class defining Amenity"""
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity", viewonly=False)
    else:
        name = ""

    def __init__(self,*args,**kwargs):
        """New Amenity instance"""
        super().__init__(**kwargs)
