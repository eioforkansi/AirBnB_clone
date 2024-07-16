import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()
        self.test_file = "file.json"
        FileStorage._FileStorage__file_path = self.test_file
        FileStorage._FileStorage__objects = {}
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_new_and_save(self):
        """Test adding new objects and saving to JSON."""
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Check if the file was created
        self.assertTrue(os.path.exists(self.test_file))

        # Check if objects are correctly saved in JSON format
        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertIn("BaseModel." + obj1.id, data)
            self.assertIn("BaseModel." + obj2.id, data)

    def test_reload(self):
        """Test reloading objects from JSON."""
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Clear the current objects in memory
        self.storage.__objects = {}

        # Reload objects from the file
        self.storage.reload()

        # Check if objects are correctly reloaded
        all_objects = self.storage.all()
        self.assertIn("BaseModel." + obj1.id, all_objects)
        self.assertIn("BaseModel." + obj2.id, all_objects)

    def test_all(self):
        """Test retrieving all objects."""
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        all_objects = self.storage.all()

        # Check if all objects are correctly retrieved
        self.assertIn("BaseModel." + obj1.id, all_objects)
        self.assertIn("BaseModel." + obj2.id, all_objects)

    def test_empty_file(self):
        """Test handling when the JSON file doesn't exist."""
        # Reload should handle the case where the file doesn't exist
        self.storage.reload()

        # After reload, __objects should be empty
        self.assertEqual(len(self.storage.all()), 0)

if __name__ == '__main__':
    unittest.main()

