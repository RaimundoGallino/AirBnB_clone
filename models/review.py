#!/usr/bin/python3
'''file that defines the Base_model class4'''

from models.base_model import BaseModel


class Review(BaseModel):

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        '''Class Constructor'''
        super().__init__(*args, **kwargs)
