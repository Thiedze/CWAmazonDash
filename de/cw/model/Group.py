'''
Created on 11.01.2018

@author: Sebastian.Thiems
'''


class Group(object):
    
    def __init__(self, name, columns):
        self.columns = columns
        self.name = name
        self.dash_buttons = list()