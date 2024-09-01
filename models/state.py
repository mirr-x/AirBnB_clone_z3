#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
    @name : string - empty string
    '''

    __tablename__ = "states"

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship(
        "City",
        cascade='all, delete, delete-orphan',
        backref="state"
    )

    @property
    def cities(self):
        '''
        Getter attribute that returns the list of City instances with state_id
        equals to the current State.id
        '''
        from models import storage
        from models.city import City
        cities = storage.all(City)
        result = []
        for city in cities.values():
            if city.state_id == self.id:
                result.append(city)
        return result
