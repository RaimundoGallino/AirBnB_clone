#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.city import City


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_User(self):
        '''Test'''
        b = City()
        b.email = "Test"
        self.assertEqual(b.email, "Test")


if __name__ == "__main__":
    unittest.main()
