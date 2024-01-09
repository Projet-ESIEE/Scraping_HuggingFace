import scrapy


class TwitchSpiderSpider(scrapy.Spider):
    name = "twitch"
    allowed_domains = ["twitch.tv"]
    start_urls = ["https://twitch.tv/directory"]

    def parse(self, response):
        pass
