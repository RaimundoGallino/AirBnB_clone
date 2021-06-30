#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User



class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_User(self):
        '''Test'''
        b = Amenity()
        b.email = "Test"
        self.assertEqual(b.email, "Test")

    def test_Init(self):
        """test instance"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))


if __name__ == "__main__":
    unittest.main()
