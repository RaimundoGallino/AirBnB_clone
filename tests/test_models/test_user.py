#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.user import User


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_User(self):
        '''Test'''
        b = User()
        b.email = "Test"
        self.assertEqual(b.email, "Test")


    
    def test_user(self):
        '''  Test for User '''
        u = User()
        self.assertEqual(str, type(u.email))
        self.assertEqual(str, type(u.password))
        self.assertEqual(str, type(u.first_name))
        self.assertEqual(str, type(u.last_name))


if __name__ == "__main__":
    unittest.main()
