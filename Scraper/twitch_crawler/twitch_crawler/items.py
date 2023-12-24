# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitchStreamItem(scrapy.Item):
    """
    The list of all fields collected
    """
    name_streamer = scrapy.Field()
    name_game = scrapy.Field()
    live_title = scrapy.Field()
    live_label = scrapy.Field()
    live_description = scrapy.Field()

