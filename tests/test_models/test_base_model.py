#!/usr/bin/pythons3
"""
test_base_model.py

This module serves as the entry point into console
"""
import os
import unittest
from models.base_model import add

class BaseTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 6), 10)
