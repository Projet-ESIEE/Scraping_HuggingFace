import scrapy, logging
from scrapy import Request

from ..items import HuggingfaceItem


class HuggingfacemodelsSpider(scrapy.Spider):
    name = "HuggingFaceModels"
    allowed_domains = ["huggingface.co"]
    start_urls = ["https://huggingface.co/models?sort=trending"]

    def parse(self, response):
        title = response.css("title::text").extract_first()
        logging.warning("\nParse : " + title + "\n")

        models = response.css("a.block.p-2")
        for model in models:
            title = model.css("h4::text").extract_first()

            company_name = title.split("/")[0]
            model_name = title.split("/")[1]
            model_update = model.css("time::attr(datetime)").extract_first()
            model_stat = model.css("div::text").extract()
            i = 0

            if len(model.css("svg.mr-1\.5.text-\[\.8rem\]")) == 0:
                i += 2
                model_type = None
            else:
                model_type = model_stat[1][4:-4]

            if len(model.css("svg.flex-none.w-3.text-gray-400.mr-0\.5")) == 0:
                i += 2
                model_downloads = None
            else :
                model_downloads = model_stat[5-i][5:-4]

            if len(model.css("svg.flex-none.w-3.text-gray-400.mr-1")) == 0 :
                model_likes = "0"
            else :
                model_likes = model_stat[7-i][5:-4]

            yield HuggingfaceItem(
                company_name=company_name,
                model_name=model_name,
                model_type=model_type,
                model_update=model_update,
                model_downloads=model_downloads,
                model_likes=model_likes,
            )
