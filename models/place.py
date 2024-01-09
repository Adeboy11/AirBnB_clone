#!/usr/bin/python3
"""the Place class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """ a place that inherits from the base class

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of 
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
