# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter

class UbcscraperPipeline(object):
    def process_item(self, item, spider):
        return item

class PerDeptJsonLinesPipeline(object):
    def open_spider(self, spider):
        self.dept_to_exporter = {}

    def close_spider(self, spider):
        for exporter in self.dept_to_exporter.values():
            exporter.finish_exporting()
            exporter.file.close()

    def _exporter_for_item(self, item, spider):
        dept = item['course'][0:4]
        if dept not in self.dept_to_exporter:
            f = open('data/{0}{1}{2}.jl'.format(dept.lower(), spider.year, spider.session), 'wb')
            exporter = JsonLinesItemExporter(f)
            exporter.start_exporting()
            self.dept_to_exporter[dept] = exporter
        return self.dept_to_exporter[dept]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item, spider)
        exporter.export_item(item)
        return item
