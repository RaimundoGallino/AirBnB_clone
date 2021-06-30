#!/usr/bin/python3
'''Unitest for base_model'''
import unittest
from time import sleep
from models.base_model import BaseModel
from datetime import datetime


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_Base(self):
        '''Test'''
        b = BaseModel()
        b.name = "Test"
        self.assertEqual(b.name, "Test")

    def test_type_Base(self):
        '''Test if the instance is the correct class'''
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.id, str)

    def test_str_method(self):
        '''test methods documentation'''
        b = BaseModel()
        str_basmodel = "[{}] ({}) {}".format(b.__class__.__name__, b.id,
                                             b.__dict__)
        self.assertEqual(b.__str__(), str_basmodel)

    def test_todict_method(self):
        b = BaseModel()
        dict_ = b.to_dict()
        self.assertIsInstance(dict_, dict)
        class_name = b.__class__.__name__
        id = b.id
        self.assertEqual(class_name, dict_["__class__"])
        self.assertEqual(id, dict_["id"])

    def test_save_method(self):
        b = BaseModel()
        sleep(2)
        date = b.updated_at
        b.save()
        self.assertGreater(b.updated_at, date)

    



if __name__ == "__main__":
    unittest.main()
