#!/usr/bin/pythons3
"""
Handles storage of instances
"""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    """
    FileStorage class that
    - serializes instances to a JSON file
    - and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Dictionary to map class names to class object
        """
        self.classes = {
            "BaseModel": BaseModel,
            "User": User
        }

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj


    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj
                    elif class_name == "User":
                        obj = User(**value)
                        FileStorage.__objects[key] = obj


        except Exception:
            pass









