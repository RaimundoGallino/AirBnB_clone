#!/usr/bin/python3
'''Unitest for base_model'''

import json
import unittest
from time import sleep
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import pep8


class TestFileStorage(unittest.TestCase):
    '''Test Cases'''

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setUp(self):
        """la puta que lo aprio"""
        pass

    def tearDown(self):
        """la puta que lo aprio"""
        if os.path.exists("file.json"):
            os.rename("file.json", "eae")

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
        b.save()
        bool = os.path.exists('file.json')
        self.assertTrue(bool)


    def test_reload_method(self):
        '''test'''
        b = BaseModel()
        file = FileStorage()
        dict_ = storage.all().copy()
        storage.reload()
        dict_reloaded = storage.all()
        self.assertEqual(len(dict_), len(dict_reloaded))

        di = {}
        b.save()
        self.assertEqual(str, type(file._FileStorage__file_path))
        self.assertEqual(dict, type(file._FileStorage__objects))
        f = os.path.exists('file.json')
        self.assertTrue(f)



if __name__ == "__main__":
    unittest.main()
