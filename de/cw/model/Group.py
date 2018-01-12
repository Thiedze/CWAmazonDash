'''
Created on 11.01.2018

@author: Sebastian.Thiems
'''


class Group(object):
    
    def __init__(self, name, rows):
        self.rows = rows
        self.name = name
        self.dash_buttons = list()