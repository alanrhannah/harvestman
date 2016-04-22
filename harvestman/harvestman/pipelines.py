# -*- coding: utf-8 -*-
import datetime
from harvestman import settings

from scrapy import signals
from scrapy.exporters import CsvItemExporter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HarvestmanPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        csv_file = settings.CSV_FILE_OUTPUT_DIR.format(
            datetime.date.today().strftime('%Y-%m-%d'))
        if spider.name == 'google_serp_spider':
            file = open(csv_file, 'ab')
            self.files[spider] = file
            self.exporter = CsvItemExporter(file)
            self.exporter.start_exporting()

    def spider_closed(self, spider):
        if spider.name == 'google_serp_spider':
            self.exporter.finish_exporting()
            file = self.files.pop(spider)
            file.close()

    def process_item(self, item, spider):
        if spider.name == 'google_serp_spider':
            self.exporter.export_item(item)
            return item
