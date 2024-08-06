#!/usr/bin/python3
"""
base_model.py

This module serves as the entry point into console
"""
import uuid
from datetime import datetime
import models

class BaseModel():
    """
    Base class for all models.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    new_value = datetime.fromisoformat(value)
                    setattr(self, key, new_value)
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
         """Updates the `updated_at` attribute with the current datetime."""
         self.updated_at = datetime.utcnow()
         models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


