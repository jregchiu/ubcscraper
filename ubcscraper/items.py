# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UbcscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Course(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    credits = scrapy.Field()
    prereqs = scrapy.Field()
    coreqs = scrapy.Field()
    activities = scrapy.Field()
    sections = scrapy.Field()

class Section(scrapy.Item):
    code = scrapy.Field()
    status = scrapy.Field()
    activity = scrapy.Field()
    term = scrapy.Field()
    days = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
