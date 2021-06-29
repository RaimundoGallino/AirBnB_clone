#!/usr/bin/python3
'''User Module'''

from models.base_model import BaseModel


class User(BaseModel):
    '''User Class'''

    email = str('')
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        '''Class Constructor'''
        super().__init__(*args, **kwargs)
