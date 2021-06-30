#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.city import City


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_city(self):
        '''  Test for City '''
        c = City()
        self.assertEqual(str, type(c.state_id))
        self.assertEqual(str, type(c.name))


if __name__ == "__main__":
    unittest.main()
