import scrapy

class TechnoSpider(scrapy.Spider):
    name = "techno"

    def start_requests(self):

        url = "https://www.technomarket.bg/laptopi/lenovo"

        yield scrapy.Request(url=url, callback=self.parse)
        self.log(url)

    def parse(self, response):

        for item in response.css('figure'):
            text = item.css('figcaption  span::text').extract_first()
            url = item.css('a::attr(href)').extract_first()
            price = item.css('figcaption  .product-price span::text').extract_first()
            price_second = item.css('figcaption  .product-price sup::text').extract_first()
            currency = item.css('figcaption  .product-price small::text').extract_first()

            print(dict(text=text, url=url, price=price + price_second + currency));



