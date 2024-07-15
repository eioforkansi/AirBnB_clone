#!/usr/bin/python3
"""
base_model.py

This module serves as the entry point into console
"""
import uuid
from datetime import datetime

class BaseModel():
    """

    """
    def __init__(self):
        """Initializes a new BaseModel instance."""
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
         """Updates the `updated_at` attribute with the current datetime."""
         self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.created_at.isoformat()

        return dictionary

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


