import scrapy


class DummyOtaHotelsSpider(scrapy.Spider):
    """ scrapy crawl hotels -o hotels.json """
    name = "hotels"

    def start_requests(self):
        yield scrapy.Request(url='https://www.google.com/', callback=self.parse_function)

    def parse_function(self, response):
        yield {"Success": True}
