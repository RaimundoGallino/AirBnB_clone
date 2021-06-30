#!/usr/bin/python3
'''Unitest for base_model'''

import json
import unittest
from time import sleep
from os import path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.amenity import Amenity
import pep8


class TestFileStorage(unittest.TestCase):
    '''Test Cases'''

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_isInstance(self):
        '''Test'''
        b = FileStorage()
        self.assertIsInstance(b, FileStorage)
        self.assertIsInstance(storage, FileStorage)


    def test_all_method(self):
        '''Test'''
        b = BaseModel()
        dict_ = storage.all()
        self.assertIsNotNone(dict_)
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


    def test_FileStorage_arg(self):
        """testing file storage with an argument"""
        with self.assertRaises(TypeError):
            FileStorage("Holberton")
        with self.assertRaises(TypeError):
            FileStorage("89")
        with self.assertRaises(TypeError):
            FileStorage(None)

        def test_reload(self):
            """tests the reload"""
            if not path.exists("file.json"):
                new_file = FileStorage()
                new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.86",
                                    updated_at="2021-02-17T22:46:38.86")
                new_city = City()
                new_file.new(new_base)
                new_file.new(new_city)
                new_file.save()
            with open("file.json", "r") as f:
                obj = json.load(f)
            self.assertEqual(type(obj), dict)


if __name__ == "__main__":
    unittest.main()
