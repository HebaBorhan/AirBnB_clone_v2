#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", cascade="all, delete", backref="cities")

    def __init__(
            self,
            state_id="",
            name="",
            *args,
            **kwargs):
        """New City instance"""
        super().__init__(**kwargs)
        self.state_id = state_id
        self.name = name
