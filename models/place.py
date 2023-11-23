#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,
                              nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False,
                            primary_key=True)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity = relationship('Amenity', secondary=place_amenity, viewonly=False)
        reviews = relationship('Review', cascade='all, delete, delete-orphan', backref='place')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to the current Place.id"""
            from models import storage
            review_list = []
            for review in storage.all(Review).values:
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """ gets list of amenites """
            from models import storage
            from models.amenity import Amenity
            amenity_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """ sets ammenities ids to the ammenity_ids attribute """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
