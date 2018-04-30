import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, TakeFirst, MapCompose
from w3lib.html import remove_tags

def filter_status(text):
    return None if text == '\xa0' else text

class CourseLoader(ItemLoader):
    default_input_processor = MapCompose(remove_tags, str.strip)
    default_output_processor = TakeFirst()
    prereqs_out = Identity()
    coreqs_out = Identity()

class SectionLoader(ItemLoader):
    default_input_processor = MapCompose(remove_tags, str.strip)
    default_output_processor = TakeFirst()
    days_out = Identity()
    term_out = Identity()
