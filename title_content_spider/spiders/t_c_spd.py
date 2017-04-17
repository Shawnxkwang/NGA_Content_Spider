import scrapy
from scrapy import Selector
from scrapy import Request
from ..items import ContentItem

class NgaSpider(scrapy.Spider):
    name = "NgaSpider"
    host = "http://bbs.nga.cn"
    # first page to crawl
    start_urls = ["http://bbs.ngacn.cc/thread.php?fid=414",]

    def start_requests(self):
        for url in self.start_urls:
            # add the url into queue
            yield Request(url=url, callback=self.parse_page)


    # response to the crawled content
    def parse_page(self, response):
        #print(response.body)
        selector = Selector(response)
        title_list = selector.xpath("//*[@class='topic']")
        for title in title_list:
            topic = title.xpath('string(.)').extract_first()
            print(topic)
            url = self.host +title.xpath("@href").extract_first()
            print(url)
            yield Request(url=url, callback=self.parse_topic)
        # can parse more pages here

    # responsible for every tiezi every floor
    def parse_topic(self,response):
        selector = Selector(response)
        floor_list = selector.xpath("//*[@class='postcontent ubbcode']")
        for floor in floor_list:
            fl = floor.xpath('string(.)').extract_first()
            #print(fl)
        # can parse mpre pages here
        item = ContentItem()
        item["url"] = response.url
        item["title"] = fl
        item["author"] = ""
        yield item
