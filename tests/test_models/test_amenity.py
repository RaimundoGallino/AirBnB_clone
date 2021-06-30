#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User



class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_User(self):
        '''Test'''
        b = Amenity()
        b.email = "Test"
        self.assertEqual(b.email, "Test")

    def test_constructor(self):
        """test init"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_pub_attrs(self):

        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

        new_d = user.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in user.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_dictval(self):
        """ test if it generate unique id"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """ test if it generate unique id"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test_uniid(self):
        """ test if it generate unique id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1, user2)

    def test_module_docstring(self):
        """asdas asd asd asd"""
        self.assertIsNot(User.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_class_docstring(self):
        """asdas asd asd asd"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_func_docstrings(self):
        """asdas asd asd asd"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


if __name__ == "__main__":
    unittest.main()
