#!/usr/bin/python3
"""Contains class state"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state

    Attributes:
        name (str): name of a state
    """
    name = ""
