#!/usr/bin/python3
'''file that defines the Base_model class4'''

import json
from os import path
from models.base_model import BaseModel
from models.users import User


Av_classes = {'BaseModel': BaseModel, 'User': User}
class FileStorage:
    '''Class FileStorage store info in json files'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Return __objects'''
        return self.__objects

    def new(self, obj):
        '''Add a new object in __objects'''
        name = type(obj).__name__ + "." + obj.id
        temp = {name: obj}
        self.__objects.update(temp)

    def save(self):
        '''Save all content of __objects in a json file'''
        obj = {}
        for k in self.__objects:
            obj[k] = self.__objects[k].to_dict()

        with open(self.__file_path, "w+") as json_file:
            json.dump(obj, json_file)

    def reload(self):
        '''Loads the content of a json file into __objects'''
        try:
            with open(self.__file_path, "r") as json_file:
                content = json.load(json_file)
                for k in content:
                    class_name = k.split('.')
                    self.__objects[k] = Av_classes[class_name[0]](**content[k])
        except:
            pass
