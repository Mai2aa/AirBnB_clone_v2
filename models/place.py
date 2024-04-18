#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.state import State


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    reviews = relationship("Review", cascade="all, delete", backref="place")
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False)
                          )

    @property
    def amenity_ids(self):
        """Getter for amenity_ids"""
        return [amenity.id for amenity in self.amenities_list]

    @amenity_ids.setter
    def amenity_ids(self, amenity_id):
        """Setter for amenity_ids"""
        if amenity_id not in self.amenity_ids:
            self.amenities_list.append(amenity_id)
    
    @property
    def amenities(self):
        """Getter attribute amenities"""
        return self.amenities_list

    @amenities.setter
    def amenities(self, amenity):
        """Setter attribute amenities"""
        if isinstance(amenity, Amenity):
            self.amenity_ids = amenity.id
