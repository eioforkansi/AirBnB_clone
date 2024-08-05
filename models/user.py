#!/usr/bin/pythons3
"""
user.py

This module serves as User class that inherit from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

