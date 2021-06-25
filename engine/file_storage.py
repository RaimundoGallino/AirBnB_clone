#!/usr/bin/python3
'''file that defines the Base_model class'''

import uuid
import json
from datetime import datetime

class FileStorage:

    __file_path = ''
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        temp = {}
        self.__objects = obj
    
    def save(self):

