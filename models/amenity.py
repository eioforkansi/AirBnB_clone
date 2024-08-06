#!/usr/bin/pythons3
"""
city.py

This module serves as Amenity class and inherits from BaseModel
"""

from base_model import BaseModel

class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
