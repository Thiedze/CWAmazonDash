'''
Created on 11.01.2018

@author: Sebastian.Thiems
'''


class DashButton(object):

    def __init__(self, number, asin, image_url):
        self.number = number
        self.asin = asin
        self.image_url = image_url
        
    def __cmp__(self, other):
        return cmp(self.number, other.number)