#!/usr/bin/python3

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    '''
    @city_id: string - empty string: it will be the City.id
    @user_id: string - empty string: it will be the User.id
    @name: string - empty string
    @description: string - empty string
    @number_rooms: integer - 0
    @number_bathrooms: integer - 0
    @max_guest: integer - 0
    @price_by_night: integer - 0
    @latitude: float - 0.0
    @longitude: float - 0.0
    @amenity_ids: list of string - empty list: it will be the list of Amenity.id later
    '''
    __tablename__ = 'places'

    city_id = Column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False
    )

    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False
    )

    name = Column(
        String(128),
        nullable=False
    )

    description = Column(
        String(1024),
        nullable=True
    )

    number_rooms = Column(
        Integer,
        nullable=False,
        default=0
    )

    number_bathrooms = Column(
        Integer,
        nullable=False,
        default=0
    )

    max_guest = Column(
        Integer,
        nullable=False,
        default=0
    )

    price_by_night = Column(
        Integer,
        nullable=False,
        default=0
    )
    latitude = Column(
        Float,
        nullable=True
    )

    longitude = Column(
        Float,
        nullable=True
    )

    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            cascade='all, delete, delete-orphan',
            backref='place'
        )
        # amenities = relationship(
        #     'Amenity',
        #     secondary='place_amenity',
        #     viewonly=False,
        #     back_populates='place_amenities'
        # )
    else:
        @property
        def reviews(self):
            '''
            Getter attribute in case of file storage
            '''
            review_list = []
            all_reviews = models.storage.all(Review)

            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            '''
            Getter attribute in case of file storage
            '''
            amenity_list = []
            all_amenities = models.storage.all(Amenity)

            for amenity in all_amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list
        
        @amenities.setter
        def amenities(self, obj):
            '''
            Setter attribute in case of file storage
            '''
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)


