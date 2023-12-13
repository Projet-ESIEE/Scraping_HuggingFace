import scrapy


class TwtchSpider(scrapy.Spider):
    name = "twtch"
    allowed_domains = ["www.twitch.tv"]
    start_urls = ["https://www.twitch.tv"]

    def parse(self, response):
        pass
