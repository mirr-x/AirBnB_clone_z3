#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel


class FileStorage():
    """ privat attr """
    __file_path = "file.json"
    __objects = {}

    ''' __init__(self) method : 
    > storing attrubuites 
    '''

    def __init__(self):

        self.key_id = None
        self.bs_objet = None

    ''' all(self) method : 
    > returning dict of  > self.__objects <
    '''

    def all(self, cls=None):
        if cls is not None:
            new_dict = {}
            for k, v in self.__objects.items():
                cls_obj = v["__class__"]
                if cls_obj == cls.__name__:
                    new_dict[k] = v
            return new_dict
        else:
            return self.__objects


    ''' new(self, obj) method : 
    > @obj is an object name 
      in this method we will get the id of @obj 
      and make it as this format " <obj class name>.id " 
      and add it to self.__objects dict
    '''

    def new(self, obj):
        frmt = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        self.__objects[frmt] = obj
        self.key_id = frmt
        self.bs_objet = obj

    ''' save(self) method : 
    > serializesing means >> turning object into dict (json-format)
      and store it to a json file
    '''

    def save(self):
        from models.base_model import BaseModel

        if self.key_id is not None and self.bs_objet is not None:
            self.__objects[self.key_id] = self.bs_objet.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, indent=2)

    ''' reload(self) method :
    > deserializesing means >> turning dict (json-format) into object
      and store objectes into a __objects
    '''

    def reload(self):
        bol = os.path.exists(self.__file_path)

        if bol:
            with open(self.__file_path, "r") as x:
                self.__objects = json.load(x)

    ''' delete(self, obj=None) method :
    > if @obj is not None
      we will get the id of @obj 
      and delete it from self.__objects dict
    '''

    def delete(self, obj=None):
        if obj is not None:
            formatx = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
            del self.__objects[formatx]
            self.save()

    def close(self):
        """Call reload() method for deserializing the JSON file to objects."""
        self.reload()

    #! XXXXXXXXXXXXXXXX
