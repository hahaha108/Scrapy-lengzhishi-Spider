# -*- coding: utf-8 -*-

from scrapy.spider import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from lengzhishi.items import LengzhishiItem


class LengdouSpider(CrawlSpider):
    name = 'lengdou'
    allowed_domains = ['lengdou.net']
    start_urls = ['http://lengdou.net/']

    linkextractor = LinkExtractor(allow=(r'/lengzhishi/\d+',))
    rules = [
        Rule(linkextractor,callback="parseContent",follow=True)
    ]

    def parseContent(self, response):
        content = response.xpath("//div[@class='list-content']/p/text()").extract()[0]
        item = LengzhishiItem()
        item['content'] = content
        yield item

