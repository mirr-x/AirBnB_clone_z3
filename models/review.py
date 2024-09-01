#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    '''
    @place_id: string - empty string: it will be the Place.id
    @user_id: string - empty string: it will be the User.id
    @text: string - empty string
    '''
    __tablename__ = 'reviews'

    text = Column(
        String(1024),
        nullable=False
    )

    place_id = Column(
        String(60),
        ForeignKey('places.id'),
        nullable=False
    )

    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False
    )