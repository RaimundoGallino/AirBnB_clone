#!/usr/bin/python3
'''file that defines the Base_model class'''

import uuid
from datetime import datetime
import models

coso = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:

    id = ''
    created_at = ''
    updated_at = ''
    name = ''
    my_number = ''
    

    def __init__(self, *args, **kwargs):

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if (k == "created_at" or k == "updated_at"):
                    vi = datetime.strptime(v, coso)
                    setattr(self, k, vi)
                elif (k == "__class__"):
                    continue
                else:
                    setattr(self, k, v)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict = {'my_number': self.my_number, 'name': self.name, '__class__': type(self).__name__, 'updated_at': self.updated_at.isoformat(), 'id': self.id , 'created_at': self.created_at.isoformat()}

        return dict
