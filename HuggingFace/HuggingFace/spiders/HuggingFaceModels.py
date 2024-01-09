import scrapy


class HuggingfacemodelsSpider(scrapy.Spider):
    name = "HuggingFaceModels"
    allowed_domains = ["huggingface.co"]
    start_urls = ["https://huggingface.co/models?sort=trending"]

    def parse(self, response):
        pass
