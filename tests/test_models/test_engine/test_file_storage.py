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


    def test_reload_with_arg(self):
        """testing file storage with an argument"""
        with self.assertRaises(TypeError):
            storage.reload(None)


    def test_new(self):
        '''Test new method'''
        new_file = FileStorage()
        new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.883036",
                                updated_at="2021-02-17T22:46:38.883036")
        new_city = City()
        new_amenity = Amenity()
        new_user = User()
        new_place = Place()
        new_review = Review()
        new_state = State()
        new_file.new(new_base)
        new_file.new(new_city)
        new_file.new(new_amenity)
        new_file.new(new_place)
        new_file.new(new_state)
        new_file.new(new_user)
        new_file.new(new_review)
        objs = new_file.all()
        key = new_base.__class__.__name__ + "." + new_base.__dict__["id"]
        key_2 = new_city.__class__.__name__ + "." + new_city.__dict__["id"]
        key_user = new_user.__class__.__name__ + "." + new_user.__dict__["id"]
        key_review = new_review.__class__.__name__ + "." + new_review.__dict__["id"]
        key_place = new_place.__class__.__name__ + "." + new_place.__dict__["id"]
        key_state = new_state.__class__.__name__ + "." + new_state.__dict__["id"]
        key_amenity = new_amenity.__class__.__name__ + "." + new_amenity.__dict__["id"]
        self.assertIn(key, objs)
        self.assertIn(key_2, objs)
        self.assertIn(key_user, objs)
        self.assertIn(key_review, objs)
        self.assertIn(key_place, objs)
        self.assertIn(key_state, objs)
        self.assertIn(key_amenity, objs)

    def test_save(self):
        '''Test save method'''
        objs = storage
        new_base = BaseModel()
        new_user = User()
        new_state = State()
        new_place = Place()
        new_city = City()
        new_amenity = Amenity()
        new_review = Review()
        objs.new(new_base)
        objs.new(new_user)
        objs.new(new_state)
        objs.new(new_place)
        objs.new(new_city)
        objs.new(new_amenity)
        objs.new(new_review)
        objs.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + new_base.id, save_text)
            self.assertIn("User." + new_user.id, save_text)
            self.assertIn("State." + new_state.id, save_text)
            self.assertIn("Place." + new_place.id, save_text)
            self.assertIn("City." + new_city.id, save_text)
            self.assertIn("Amenity." + new_amenity.id, save_text)
            self.assertIn("Review." + new_review.id, save_text)


if __name__ == "__main__":
    unittest.main()
