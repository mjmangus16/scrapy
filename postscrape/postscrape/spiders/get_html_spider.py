import scrapy
import json

failed = []


class PostsSpider(scrapy.Spider):
    name = "get_html"

    start_urls = [
        "https://infinitediscs.com/category/Discmania/",
    ]

    def parse(self, response):
        page = response.url
        filename = 'page.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
