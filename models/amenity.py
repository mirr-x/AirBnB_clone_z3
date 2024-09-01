#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
    @name: string - empty string
    '''
    __tablename__ = 'amenities'

    name = Column(
        String(128),
        nullable=False
    )

    # place_amenities = relationship(
    #     'Place',
    #     secondary='place_amenity'
    # )