'''
Created on 11.01.2018

@author: Sebastian.Thiems
'''


class DashButton(object):

    def __init__(self, column, row, asin):
        self.row = row
        self.column = column
        self.asin = asin
        self.image_url = None
        self.price = None
        self.title = None
        
    def __cmp__(self, other):
        return cmp(self.row, other.row) and cmp(self.column, other.column)
