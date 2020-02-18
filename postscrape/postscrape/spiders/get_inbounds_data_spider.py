import scrapy
import json

# ACTIVATE VENV
# --- source venv/bin/activate
# --- cd into top postscrape folder


# RUN SCRAPER
# --- scrapy crawl *name*
# To write to a json file
# --- scrapy crawl *name* -o *name of json file*

# This spider will grab the html of a specific page
# This is a great place to start as it is easier to view the layout of the page and find the correct css selectors for grabbing the data you want.


class PostsSpider(scrapy.Spider):
    name = "get_inbounds_data"

    start_urls = [
        "http://www.inboundsdiscgolf.com/content/?page_id=431",
    ]

    def parse(self, response):
        allData1 = response.css("td.l input::attr(value)").getall()
        allData2 = response.css("td.lp input::attr(value)").getall()

        allData = allData1 + allData2
        splitData = list()

        for d in allData:
            cont = d.split("|")
            splitData.append(cont)

        for d in splitData:

            yield {
                'title': d[1],
                'inboundRating': f"{d[3]}/{d[4]}/{d[5]}/{d[6]}"
            }
