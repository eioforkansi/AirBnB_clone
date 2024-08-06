#!/usr/bin/pythons3
"""
city.py

This module serves as Place class and inherits from BaseModel
"""

from base_model import BaseModel

class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathroom = 0
    max_guest = 0
    price_by_night = 0
    lattitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
