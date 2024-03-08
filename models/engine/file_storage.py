#!/usr/bin/python3
""" defines a FileStroage class """
import json

class FileStorage:
    """Represent an abstracted storage engine.

Attributes:
    __file_path (str): The name of the file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
"""



    _file_path = "file.json"
    _objects = {}


    def all(self):
        """ returns the dictionary __objects """
        return FileStorage._objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage._objects[key] = obj

    def save(self):
        """ saves objects into json file thats the __file_path"""
        odict = FileStorage._objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage._file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage._file_path) as f:
                json.load(f)  
        except FileNotFoundError:
            return
