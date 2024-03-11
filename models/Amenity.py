#!/usr/bin/python3
"""Defines class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenities"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)
