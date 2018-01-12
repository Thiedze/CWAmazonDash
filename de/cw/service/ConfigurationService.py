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
        
    def get_asins(self):
        asins = list()
        for section in self.config_parser.sections():
            for value in dict(self.config_parser.items(section)).values():
                asins.append(value)
        print(",".join(asins))
        return ",".join(asins)
        
    def get_groups(self):
        groups = list()
        items = self.amazon_api.item_lookup(self.get_asins(), ResponseGroup='Images', Condition='All').Items.Item
        print(items)
        for section in self.config_parser.sections():
            print(section.split("_"))
            group = Group(section.split("_")[2], section.split("_")[1])
            for (key, value) in self.config_parser.items(section):
                for item in items:
                    if item.ASIN.text == value:
                        group.dash_buttons.append(DashButton(key.split("_")[0], key.split("_")[1], value, item.LargeImage.URL))
            group.dash_buttons.sort()
            print([(dash_button.row, dash_button.column) for dash_button in group.dash_buttons])
            groups.append(group)
        return groups
