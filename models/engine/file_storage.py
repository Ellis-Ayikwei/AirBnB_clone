#!/usr/bin/python3
<<<<<<< HEAD
""" defines a FileStroage class """
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine.

Attributes:
    ___file_path (str): The name of the file to save objects to.
    ___objects (dict): A dictionary of instantiated objects.
"""



    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ returns the dictionary ___objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in ___objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ saves objects into json file thats the ___file_path"""
        pdict = FileStorage.__objects
        obj_dict = {obj: pdict[obj].to_dict()
                    for obj in pdict.keys() 
                    if isinstance(pdict[obj], BaseModel)}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file ___file_path to ___objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)  
        except FileNotFoundError:
            return
=======
"""
Contains class 'FileStorage'
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances / python objects

    Attributes:
        __file_path (str) : the name of the JSON file to save objects to.
        __objects (dict) : dictionary - empty but will store all
                           objects by <class name>.id
    
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary '__objects'"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj, with: key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes the __objects to the JSON file(path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(json_objects, json_file)

    def reload(self):
        """deserializes the JSON file to __objects if it exists,otherwise,
        do nothing. If file doesn’t exist, no exception should be raised"""
        try:
            with open(self.__file_path, "r") as json_file:
                new_obj = json.load(json_file)
            for key in new_obj:
                self.__objects[key] = classes[new_obj[key]["__class__"]](**new_obj[key])
        except FileNotFoundError:
            pass
>>>>>>> james/AirBnB
