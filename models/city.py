#!/usr/bin/python3
"""Contains class city"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes city"""
        super().__init__(*args, kwargs)
