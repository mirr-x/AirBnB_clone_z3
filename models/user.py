#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = 'users'

    email = Column(
        String(128),
        nullable=False
    )

    password = Column(
        String(128),
        nullable=False
    )

    first_name = Column(
        String(128),
        nullable=False
    )

    last_name = Column(
        String(128),
        nullable=False
    )

    places = relationship(
        "Place",
        cascade='all, delete, delete-orphan',
        backref="user"
    )

    reviews = relationship(
        "Review",
        cascade='all, delete, delete-orphan',
        backref="user"
    )

