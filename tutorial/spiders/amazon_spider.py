import scrapy
from pprint import pprint
import pandas as pd

class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = [
            'https://global.rakuten.com/en/search/?k=iphone&p=2&l-id=search_regular'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item_names = response.css("div.b-mod-item-vertical").css("div.b-fix-2lines").css("a::text").getall()
        
        pd.DataFrame(item_names).to_csv("item_names.csv", index=False)
