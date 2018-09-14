# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeItem(scrapy.Item):
    # define the fields for your item here like:
     Title=scrapy.Field()
     Code = scrapy.Field()
     Description=scrapy.Field()
     URL=scrapy.Field()
     Language=scrapy.Field()
     subtitle = scrapy.Field()
