#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.state import State


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_User(self):
        '''Test'''
        b = State()
        b.email = "Test"
        self.assertEqual(b.email, "Test")

    
    def test_user(self):
        '''  Test for State '''
        s = State()
        self.assertEqual(str, type(s.name))


if __name__ == "__main__":
    unittest.main()
