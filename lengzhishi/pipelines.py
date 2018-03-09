# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LengzhishiPipeline(object):

    def __init__(self):
        self.file = open('1.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(item['content'])
        self.file.flush()
        return item

    def __del__(self):
        self.file.close()
