#!/usr/bin/pythons3
"""
city.py

This module serves as City class and inherits from BaseModel
"""

from models.base_model import BaseModel

class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
