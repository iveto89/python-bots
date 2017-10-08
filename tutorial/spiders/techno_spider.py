import scrapy
import csv

class TechnoSpider(scrapy.Spider):
    name = "techno"
    count = 0
    filename = "tech_data.csv"

    def start_requests(self):
        self.deleteContent()

        url = "https://www.technomarket.bg/product/filter?filter_form%5Bsort%5D=default&filter_form%5Bprice%5D%5Bmin%5D=529&filter_form%5Bprice%5D%5Bmax%5D=5299&filter_form%5Bspec_tv_screen%5D%5Bmin%5D=&filter_form%5Bspec_tv_screen%5D%5Bmax%5D=&filter_form%5Bspec_laptop_hdd%5D%5Bmin%5D=&filter_form%5Bspec_laptop_hdd%5D%5Bmax%5D=&filter_form%5Bspec_laptop_wg%5D%5Bmin%5D=&filter_form%5Bspec_laptop_wg%5D%5Bmax%5D=&filter_key=%2Flaptopi%2Flenovo%7Cstatic%7Cstatic&from=0&size=20"

        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        figure = response.css('figure');
        self.count += len(figure)
        print("count %s" % self.count)

        for item in response.css('figure'):
            name = item.css('figcaption  span::text').extract_first()
            url = item.css('a::attr(href)').extract_first()
            price = item.css('figcaption  .product-price span::text').extract_first()
            price_second = item.css('figcaption  .product-price sup::text').extract_first()
            total_price = price + price_second
            currency = item.css('figcaption  .product-price small::text').extract_first()
            currency_name = u''.join(currency)

            # data = u' '.join(("Name: %s, Url: %s, Price: %s %s" % (name, url, total_price, currency_name))).encode('utf-8').strip()
            # print("Saved data %s" % data)

            fields = [name.encode('utf-8'), url.encode('utf-8'), total_price.encode('utf-8'), currency_name.encode('utf-8')]
            # @Todo refactor this using Scrapy
            with open(self.filename, "ab") as f:
                writer = csv.writer(f)
                writer.writerow(fields)


        if response.body:

            url = "https://www.technomarket.bg/product/filter?filter_form%5Bsort%5D=default&filter_form%5Bprice%5D%5Bmin%5D=529&filter_form%5Bprice%5D%5Bmax%5D=5299&filter_form%5Bspec_tv_screen%5D%5Bmin%5D=&filter_form%5Bspec_tv_screen%5D%5Bmax%5D=&filter_form%5Bspec_laptop_hdd%5D%5Bmin%5D=&filter_form%5Bspec_laptop_hdd%5D%5Bmax%5D=&filter_form%5Bspec_laptop_wg%5D%5Bmin%5D=&filter_form%5Bspec_laptop_wg%5D%5Bmax%5D=&filter_key=%2Flaptopi%2Flenovo%7Cstatic%7Cstatic&from=" + str(self.count) + "&size=20"

            yield scrapy.Request(url=url, callback=self.parse)

    def deleteContent(self):

        with open(self.filename, "w"):
            pass




