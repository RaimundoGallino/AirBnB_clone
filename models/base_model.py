
#!/usr/bin/python3
'''file that defines the Base_model class'''

import uuid
from datetime import datetime


class BaseModel:

    id = ''
    created_at = ''
    update_at = ''

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):

        return {"'name': '{}', '__class__': '{}', 'updated_at': '{}', 'id': '{}', 'created_at': '{}'".format(self.name, type(self).__name__, self.update_at, self.id, self.created_at)}
