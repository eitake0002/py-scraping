import scrapy
from pprint import pprint
import pandas as pd
from bs4 import BeautifulSoup
from scrapy.http import FormRequest

class LinkedInSpider(scrapy.Spider):
    name = "linkedin"

    def start_requests(self):
        url = "https://twitter.com/login/"
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Referer': 'https://twitter.com/explore',
        }

        formdata = {
            "headers": headers,
            "session[username_or_email]": "email", 
            "session[password]": "password",
        }
        pprint("---- before FormRequest ----")
        return [FormRequest(url, formdata=formdata, callback=self.after_login)]


    def after_login(self, response):
        pprint("---- after login ----")
        pprint(response)
        pprint(response.status)
        pprint(response.body)
    
    def parse(self, response):

        pprint(response)
        # Get item name.
