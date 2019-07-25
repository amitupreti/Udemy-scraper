# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


count = 0
visited = []
current = ''


class UdemySpider(scrapy.Spider):
    name = 'ruralvacantland'
    rotate_user_agent = True

    allowed_domains = ['www.ruralvacantland.com']
    start_url = [
        'https://www.ruralvacantland.com/properties/?filter-location=108&filter-property-type=&filter-contract-type=']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(self.start_url[0], self.parse)

    def parse(self, response):
        from scrapy.utils.response import open_in_browser
        import ipdb
        ipdb.set_trace()
        open_in_browser(response)
        print(response)

    def parse_article(self, response):
        product_name = response.xpath('//h1/text()').extract_first()
