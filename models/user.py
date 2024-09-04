#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """User class"""
    __tablename__ = 'users'

    email = Column(
        String(128),
        nullable=False
    )

    _password = Column(
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

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = hashlib.md5(value.encode()).hexdigest()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = kwargs['password']