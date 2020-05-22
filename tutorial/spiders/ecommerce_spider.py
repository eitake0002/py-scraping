import scrapy
from pprint import pprint
import pandas as pd

class EcommerceSpider(scrapy.Spider):
    name = "ecommerce"

    def start_requests(self):
        urls = [
            'https://global.rakuten.com/en/search/?k=iphone&p=2&l-id=search_regular'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # Get item name.
        item_names = response.css("div.b-mod-item-vertical").css("div.b-fix-2lines").css("a::text").getall()
        price_list = response.css("div.b-mod-item-vertical").css("div.m-shop-top-text").css("span::text").getall()

        # Write as CSV file.
        d = {"item_name": item_names, "price": price_list}
        pd.DataFrame(d).to_csv("item_names.csv", index=False)
