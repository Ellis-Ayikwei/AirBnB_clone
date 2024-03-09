#!/usr/bin/python3
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
