import scrapy
import json

# ACTIVATE VENV
# --- source venv/bin/activate
# --- cd into top postscrape folder


# RUN SCRAPER
# --- scrapy crawl *name*
# To write to a json file
# --- scrapy crawl *name* -0 *name of json file*

# This spider will grab the html of a specific page
# This is a great place to start as it is easier to view the layout of the page and find the correct css selectors for grabbing the data you want.


class PostsSpider(scrapy.Spider):
    name = "get_inbounds_data"

    start_urls = [
        "http://www.inboundsdiscgolf.com/content/?page_id=431",
    ]

    def parse(self, response):
        allData = response.css("#inFlightGuide td::text").getall()
        

        string = " ".join(allData)
        
        b = open("postscrape/spiders/inboundsData.txt", 'a+')

        b.write(string)
            