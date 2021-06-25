#!/usr/bin/python3
'''file that defines the Base_model class'''

import json
from os import path

class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        name = (type(obj).__name__ + "." + obj.id)
        temp = {name: obj}
        self.__objects.update(temp)
    
    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            return json.dump(self.__objects, json_file)

    def reload(self):
        if (path.exists(self.__file_path)):
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                self.__objects.update(json.load(json_file))
