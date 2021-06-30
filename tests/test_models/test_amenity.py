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


    def test_pub_attrs(self):

        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

        new_d = user.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in user.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)


if __name__ == "__main__":
    unittest.main()
