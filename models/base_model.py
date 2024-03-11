#!/usr/bin/python3
"""defines  the base model class"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """represents the BaseModel Class of the Airbnb clone project."""
    
    def __init__(self, *args, **kwargs):
        """initialize a new BaseModel
        
        Args:
           *args(any) : not used
           **kwargs(dict) : Key/value pairs of attributes
        
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key,value in kwargs.items():
                if key == "created_at" or key =="updated_at":
                    self.__dict__[key] = datetime.strptime(value,timeformat)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)
        

    def __str__(self):
        """returns a string representation of the instance"""
        class_name = self.__class__.__name__
        return f"[ {class_name} ]({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
        
        
        
        
    def to_dict(self):
        """A function that returns the dic"""
        ret_dict = self.__dict__.copy()
        ret_dict["created_at"] = ret_dict["created_at"].isoformat()
        ret_dict["__class__"] = self.__class__.__name__
        ret_dict["updated_at"] = ret_dict["updated_at"].isoformat()
        return ret_dict
