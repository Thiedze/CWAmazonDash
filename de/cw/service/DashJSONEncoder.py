'''
Created on 12.01.2018

@author: Sebastian.Thiems
'''

from flask.json import JSONEncoder

from Group import Group
from DashButton import DashButton


class DashJSONEncoder(JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Group):
            return {
                'name': obj.name,
                'dash_buttons': obj.dash_buttons
            }
        elif isinstance(obj, DashButton):
            return {
                'row' : obj.row,
                'column' : obj.column,
                'asin' : obj.asin,
                'image_url' : "'" + obj.image_url + "'"
            }
        
        return super(DashJSONEncoder, self).default(obj)
