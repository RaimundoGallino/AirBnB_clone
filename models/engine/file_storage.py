#!/usr/bin/python3
'''file that defines the Base_model class'''

import json
from os import path
from models.base_model import BaseModel


class FileStorage:

    __file_path = 'file.json'
    __objects = {}


    def all(self):
        return self.__objects
    
    def new(self, obj):
        name = str(type(obj).__name__ + "." + type(obj).id)
        temp = {name: obj}
        self.__objects.update(temp)
    
    def save(self):
        obj = {}
        for k, v in self.__objects.items():
            obj[k] = v.to_dict()

        with open(self.__file_path, "w+", encoding="utf-8") as json_file:
            json.dump(obj, json_file)

    def reload(self):
        if (path.exists(self.__file_path)):
    
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                self.__objects.update(json.load(json_file))
    
                for k in json_file:
                    self.__objects[k] = BaseModel(**json_file[k])
