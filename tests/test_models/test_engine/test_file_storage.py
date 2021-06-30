'''Unitest for base_model'''
import unittest
from time import sleep
from os import path
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    '''Test Cases'''

    def test_all_method(self):
        '''Test'''
        b = BaseModel()
        dict_ = storage.all()
        self.assertIsInstance(dict_, dict)

    def test_new_method(self):
        '''Test'''
        dict1 = storage.all().copy()
        b = BaseModel()
        dict2 = storage.all()
        self.assertGreater(len(dict2), len(dict1))

    def test_save_method(self):
        '''Test'''
        b = BaseModel()
        storage.save()
        bool = path.exists('file.json')
        self.assertTrue(bool)

    def test_reload_method(self):
        '''test'''
        b = BaseModel()
        dict_ = storage.all().copy()
        storage.reload()
        dict_reloaded = storage.all()
        self.assertEqual(len(dict_), len(dict_reloaded))

        

