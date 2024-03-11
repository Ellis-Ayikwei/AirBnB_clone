from models.base_model import BaseModel
""" Defines the user  model class"""

class User(BaseModel):
    """A class representing a User object.
    
    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""