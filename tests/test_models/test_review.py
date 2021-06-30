#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.review import Review


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_review(self):
        '''  Test for Review '''
        r = Review()
        self.assertEqual(str, type(r.place_id))
        self.assertEqual(str, type(r.user_id))
        self.assertEqual(str, type(r.text))


if __name__ == "__main__":
    unittest.main()
