#!/usr/bin/pythons3
"""
state.py

This module serves as State class and inherits from BaseModel
"""

from models.base_model import BaseModel

class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
