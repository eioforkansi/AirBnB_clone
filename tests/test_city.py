#!/usr/bin/python3

"""
City class unit test
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_default_attributes(self):
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == '__main__':
    unittest.main()
