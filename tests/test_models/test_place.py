#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.place import Place


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_User(self):
        '''Test'''
        b = Place()
        b.email = "Test"
        self.assertEqual(b.email, "Test")


if __name__ == "__main__":
    unittest.main()
