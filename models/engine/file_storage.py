#!/usr/bin/python3
'''file that defines the Base_model class'''

import json
from os import path
from models.base_model import BaseModel as base


class FileStorage:

    __file_path = 'file.json'
    __objects = {}


    def all(self):
        return self.__objects
    
    def new(self, obj):
        name = type(obj).__name__ + "." + obj.id
        temp = {name: obj}
        self.__objects.update(temp)

    def save(self):
        obj = {}
        for k in self.__objects:
            obj[k] = self.__objects[k].to_dict()

        with open(self.__file_path, "w+") as json_file:
            json.dump(obj, json_file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as json_file:
                content = json.load(json_file)
                for k in content:
                    self.__objects[k] = base(**content[k])
        except:
            pass
