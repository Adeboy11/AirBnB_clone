#!/usr/bin/python3
"""the User class"""

from models.base_model import BaseModel

class User(BaseModel):
    """User inherits from the base class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
