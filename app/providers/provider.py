import scrapy


class Provider(scrapy.spider):
    def scrape(self) -> dict:
        raise NotImplementedError
