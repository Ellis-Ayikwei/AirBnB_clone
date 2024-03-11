#!/usr/bin/python3
"""Defines a test modeule for the file storage module"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.Testcase):
    """unittest for testing FileStorage clasll"""
    
    def setUp(self):
	    pass

