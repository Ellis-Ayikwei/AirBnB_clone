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
        return f"[ {self.__class__.__name__} ] ({self.id}) {self.__dict__}"

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
=======
"""
Contains class BaseModel
"""

from datetime import datetime
from models.engine.file_storage import FileStorage
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future models will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model

        Args:
            *args(any) : not used
            **kwargs(dict) : key/value pairs of attributes

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of BaseModel class"""
        return f"{self.__class__.__name__} ({self.id}){self.__dict__}"

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a new dictionary containing all keys/values
        of '__dict__' of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
