import scrapy
from scrapy import Request
from pymongo import MongoClient


def numberise(nb_str):
    if nb_str[-4:] == "\n\t\t\t":
        nb_str = nb_str[:-4]
    if nb_str[-1] == "k":
        return int(float(nb_str[:-1]) * 1000)
    if nb_str[-1] == "M":
        return int(float(nb_str[:-1]) * 1000000)
    return float(nb_str)


class HuggingfacemodelsSpider(scrapy.Spider):
    name = "HuggingFaceModels"
    allowed_domains = ["huggingface.co"]
    start_urls = ["https://huggingface.co/models?sort=trending"]

    def __init__(self, *args, **kwargs):
        super(HuggingfacemodelsSpider, self).__init__(*args, **kwargs)
        self.data = []

    def parse(self, response):
        # Récupération des informations de la page actuelle
        self.model_page(response)

        # Génération de demandes pour les autres pages
        for i in range(1, 100):
            yield Request("https://huggingface.co/models?p={}&sort=trending".format(i), callback=self.model_page)

    def model_page(self, response):
        models = response.css("a.block.p-2")
        for model in models:
            title = model.css("h4::text").extract_first()

            company_name = title.split("/")[0].strip()
            model_name = title.split("/")[1].strip()
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
            else:
                model_downloads = numberise(model_stat[5 - i][5:-4])

            if len(model.css("svg.flex-none.w-3.text-gray-400.mr-1")) == 0:
                model_likes = 0
            else:
                model_likes = numberise(model_stat[7 - i][5:-4])

            self.data.append({
                "company_name": company_name,
                "model_name": model_name,
                "model_type": model_type,
                "model_update": model_update,
                "model_downloads": model_downloads,
                "model_likes": model_likes
            })

    def closed(self, reason):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['HuggingFace']
        collection = db['Models']
        collection.insert_many(self.data)
