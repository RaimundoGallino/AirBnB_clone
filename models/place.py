#!/usr/bin/python3
'''file that defines the Base_model class4'''

from models.base_model import BaseModel


class Place(BaseModel):

    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = ''
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''Class Constructor'''
        super().__init__(*args, **kwargs)
