#!/usr/bin/python3
'''file that defines the Base_model class'''

import uuid
from datetime import datetime
import models

class BaseModel:

    id = ''
    created_at = ''
    update_at = ''
    name = ''
    my_number = ''

    def __init__(self, *args, **kwargs):

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            models.storage.new(self.__dict__)
        else:
            for k, v in kwargs.items():
                if (k == "created_at" or k == "updated_at"):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
                elif (k == "__class__"):
                    continue
                else:
                    setattr(self, k, v)
            
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict = {'my_number': self.my_number, 'name': self.name, '__class__': type(self).__name__, 'updated_at': str(self.update_at.isoformat()), 'id': self.id , 'created_at': str(self.created_at.isoformat())}

        return dict
