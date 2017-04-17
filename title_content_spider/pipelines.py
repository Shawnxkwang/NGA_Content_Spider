# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import TopicItem, ContentItem

class TitleContentSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class FilePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, TopicItem):
            # process write to file etc.
            pass
        if isinstance(item, ContentItem):
            # processing wrting to file, etc.
            pass
        return item