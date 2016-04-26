# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HarvestmanItem(scrapy.Item):
    """
    Define the fields for your item here like:

    `name = scrapy.Field()`
    """
    
    keyphrase = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    snippet = scrapy.Field()
    estimated = scrapy.Field()
