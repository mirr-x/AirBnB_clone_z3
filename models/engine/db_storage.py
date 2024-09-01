#!/usr/bin/python3

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):

        user = getenv('HBNB_MYSQL_USER')
        passw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, passw, host, db), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Return a dictionary of objects in the current database session."""
        new_dict = {}
        if cls is not None:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for c in classes:
                objects = self.__session.query(c).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """Add the object to the current database session Table."""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes to the current database session Table."""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete the object from the current database session Table."""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database and create a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """Call remove() method on the private session attribute."""
        self.__session.close()

