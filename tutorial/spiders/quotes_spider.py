import scrapy

class QuotesSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        urls = [
            'https://www.technomarket.bg/laptopi',
            'https://www.technomarket.bg/telefoni',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1];
        filename = 'products-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)