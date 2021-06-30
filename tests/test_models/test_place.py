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


    def test_place(self):
        '''  Test for User '''
        p = Place()
        self.assertEqual(str, type(p.city_id))
        self.assertEqual(str, type(p.user_id))
        self.assertEqual(str, type(p.name))
        self.assertEqual(int, type(p.number_rooms))
        self.assertEqual(int, type(p.number_bathrooms))
        self.assertEqual(int, type(p.max_guest))
        self.assertEqual(int, type(p.price_by_night))
        self.assertEqual(float, type(p.latitude))
        self.assertEqual(float, type(p.longitude))
        self.assertEqual(list, type(p.amenity_ids))


if __name__ == "__main__":
    unittest.main()
