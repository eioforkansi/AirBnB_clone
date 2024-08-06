#!/usr/bin/pythons3
"""
city.py

This module serves as Review class and inherits from BaseModel
"""

from base_model import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
