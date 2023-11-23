#!/usr/bin/python3
""" Amenities Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.place import Place, place_amenity
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ class for amenities objects """
    __tablename__ = 'amenities'
    if os.getenv('HBNB_ENV') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    else:
        name = ""
