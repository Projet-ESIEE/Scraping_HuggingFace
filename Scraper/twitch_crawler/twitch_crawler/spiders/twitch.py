import scrapy, logging
from scrapy import Request

from ..items import TwitchStreamItem


class TwitchSpider(scrapy.Spider):
    name = "twitch"
    allowed_domains = ["www.twitch.tv"]
    start_urls = ["https://www.twitch.tv"]

    def parse(self, response):
        title = response.css("title::text").extract_first()
        logging.warning("\nParse : " + title + "\n")
        all_links = ["https://www.twitch.tv"]
        for link in all_links:
            yield Request(link, callback=self.parse_landing_page)

    def parse_landing_page(self, response):
        logging.info("showcase live : ")
        logging.info(response.css('Layout-sc-1xcs6mc-0 cwtKyw find-me'))

        p_elements = response.css('footer div#twilight-sticky-footer-root p::text').extract()
        for p in p_elements:
            logging.info(p)


        # showcase live : 'Chaînes live qui pourraient vous plaire'
        # for live in response.css('Layout-sc-1xcs6mc-0 cwtKyw find-me'):
        #     logging.fatal("Start")
        #     print(live)
        #     logging.fatal("Start")
        # response.class="Layout-sc-1xcs6mc-0 lcHstp"

        name = "name"
        game = "game"
        title = "title"
        label = "label"
        description = "description"

        yield TwitchStreamItem(
            name_streamer=name,
            name_game=game,
            live_title=title,
            live_label=label,
            live_description=description,
        )
