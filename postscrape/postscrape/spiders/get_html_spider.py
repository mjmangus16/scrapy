import scrapy
import json

# ACTIVATE VENV
# --- cd into top postscrape folder
# --- source venv/bin/activate

# RUN SCRAPER
# --- scrapy crawl *name*
# To write to a json file
# --- scrapy crawl *name* -0 *name of json file*

# This spider will grab the html of a specific page
# This is a great place to start as it is easier to view the layout of the page and find the correct css selectors for grabbing the data you want.


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
