import scrapy


class Provider(scrapy.Spider):
    def scrape(self) -> dict:
        raise NotImplementedError
