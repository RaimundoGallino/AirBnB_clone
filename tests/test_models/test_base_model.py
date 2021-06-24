#!/usr/bin/python3
'''Unitest for base_model'''
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_Base(self):
        '''Test'''
        b = BaseModel()
        b.name = "Test"
        self.assertEqual(b.name, "Test")


if __name__ == "__main__":
    unittest.main()
