'''
Created on 11.01.2018

@author: Sebastian.Thiems
'''

from Group import Group
from DashButton import DashButton

import ConfigParser

import amazonproduct


class ConfigurationService(object):

    def __init__(self):
        self.config_parser = ConfigParser.RawConfigParser()
        self.config_parser.read('configuration.ini')
        self.amazon_api = amazonproduct.API(locale='de')
        
    def reloadConfigParser(self):
        self.config_parser = ConfigParser.RawConfigParser()
        self.config_parser.read('configuration.ini')
    
    def get_asins(self):
        asins = list()
        for section in self.config_parser.sections():
            for value in dict(self.config_parser.items(section)).values():
                asins.append(value)
        print(",".join(asins))
        return ",".join(asins)
        
    def create_dash_button(self, item, column, row):
        dash_button = DashButton(column, row, item.ASIN.text)
        if item.LargeImage != None :
            dash_button.image_url = item.LargeImage.URL.text
            
        if item.ItemAttributes != None:
            dash_button.title = item.ItemAttributes.Title.text
            if item.ItemAttributes.ListPrice != None:
                dash_button.price = item.ItemAttributes.ListPrice.FormattedPrice.text
        
        return dash_button
        
    def get_groups(self):
        self.reloadConfigParser()
        groups = list()
        items = self.amazon_api.item_lookup(self.get_asins(), ResponseGroup='Images, ItemAttributes, OfferFull', Condition='All').Items.Item
        print(items)
        for section in self.config_parser.sections():
            print(section.split("_"))
            group = Group(section.split("_")[2], section.split("_")[1])
            for (key, value) in self.config_parser.items(section):
                for item in items:
                    if item.ASIN.text == value:
                        group.dash_buttons.append(self.create_dash_button(item, key.split("_")[0], key.split("_")[1]))
            group.dash_buttons.sort()
            print([(dash_button.row, dash_button.column) for dash_button in group.dash_buttons])
            groups.append(group)
        return groups
