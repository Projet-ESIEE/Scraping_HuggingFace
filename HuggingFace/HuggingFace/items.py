# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HuggingfaceItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    model_name = scrapy.Field()
    model_type = scrapy.Field()
    model_update = scrapy.Field()
    model_downloads = scrapy.Field()
    model_likes = scrapy.Field()
    pass

    # def __str__(self):
    #     print("Nom de l'entreprise", self.company_name)
    #     print("Nom du model", self.model_name)
    #     print("type du model", self.model_type)
    #     print("date", self.model_update)
    #     print("Nombre de téléchargements", self.model_downloads)
    #     print("Nombre de likes", self.model_likes)
