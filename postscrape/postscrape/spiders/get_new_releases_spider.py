import scrapy
import json

# ACTIVATE VENV
# --- source venv/bin/activate
# --- cd into top postscrape folder


# RUN SCRAPER
# --- scrapy crawl *name*
# To write to a json file
# --- scrapy crawl *name* -o *name of json file*

# This file is used to get an array of dictonaries containing all the available discs on the site.
# It sets the basic data that is needed for getting discs but doesn't add all the details yet.
# Each link contains all of that manufacture's discs and the link to that discs individual page.
# We create an array of objects that contains the disc's name along with some other details.
# We also create a seperate array that contains ALL the individual links of each disc and then write those links to a text file.
# Once in a text file we can use those links in step 3.


class PostsSpider(scrapy.Spider):
    name = "get_new_releases_links"

    start_urls = [
       "https://infinitediscs.com/New-Releases"
    ]

    def parse(self, response):
        baseURL = response.url[:25]
        originalURL = response.url

        indiv_links = []
        old_link_set = set()

        old_links = open("postscrape/spiders/links.txt", 'r')
        for l in old_links:
            old_link_set.add(l[1:-3])


        # There are 4 different loops happening for grabbing discs. This is done because there is a header item that says whether a disc is a distance driver, fairway, mid range or putter.
        # We loop through each section seperately so we can store that discs type inside its dict.

        for post in response.css('div#ContentPlaceHolder1_pnlDD div.row article.col-sm-6'):
            next_page = baseURL + \
                post.css('.thumbnail .caption p .btn::attr(onclick)').get()[
                    22:-1].strip()
            splitLink = next_page.split("/")
            linkData = splitLink[-1:]
            brand = linkData[0].split("-")[0]

            if next_page not in old_link_set:
                indiv_links.append(next_page)

                

                yield {
                    'brand': brand,
                    'title': post.css('.thumbnail .caption h4::text')[0].get().strip(),
                    'infinite_ratings': post.css('.thumbnail .caption .pull-left small::text').get().strip(),
                    'image': post.css('.thumbnail .img-responsive::attr(src)').get().strip(),
                    'type': "Distance Driver",
                    'link': next_page
                }

        for post in response.css('div#ContentPlaceHolder1_pnlCD div.row article.col-sm-6'):
            next_page = baseURL + \
                post.css('.thumbnail .caption p .btn::attr(onclick)').get()[
                    22:-1].strip()
            splitLink = next_page.split("/")
            linkData = splitLink[-1:]
            brand = linkData[0].split("-")[0]

            if next_page not in old_link_set:
                indiv_links.append(next_page)

                yield {
                    'brand': brand,
                    'title': post.css('.thumbnail .caption h4::text')[0].get().strip(),
                    'infinite_ratings': post.css('.thumbnail .caption .pull-left small::text').get().strip(),
                    'image': post.css('.thumbnail .img-responsive::attr(src)').get().strip(),
                    'type': "Fairway Driver",
                    'link': next_page
                }

        for post in response.css('div#ContentPlaceHolder1_pnlMR div.row article.col-sm-6'):
            next_page = baseURL + \
                post.css('.thumbnail .caption p .btn::attr(onclick)').get()[
                    22:-1].strip()
            splitLink = next_page.split("/")
            linkData = splitLink[-1:]
            brand = linkData[0].split("-")[0]

            if next_page not in old_link_set:
                indiv_links.append(next_page)

                yield {
                    'brand': brand,
                    'title': post.css('.thumbnail .caption h4::text')[0].get().strip(),
                    'infinite_ratings': post.css('.thumbnail .caption .pull-left small::text').get().strip(),
                    'image': post.css('.thumbnail .img-responsive::attr(src)').get().strip(),
                    'type': "Mid Range",
                    'link': next_page
                }

        for post in response.css('div#ContentPlaceHolder1_pnlPT div.row article.col-sm-6'):
            next_page = baseURL + \
                post.css('.thumbnail .caption p .btn::attr(onclick)').get()[
                    22:-1].strip()
            splitLink = next_page.split("/")
            linkData = splitLink[-1:]
            brand = linkData[0].split("-")[0]

            if next_page not in old_link_set:
                indiv_links.append(next_page)

                yield {
                    'brand': brand,
                    'title': post.css('.thumbnail .caption h4::text')[0].get().strip(),
                    'infinite_ratings': post.css('.thumbnail .caption .pull-left small::text').get().strip(),
                    'image': post.css('.thumbnail .img-responsive::attr(src)').get().strip(),
                    'type': "Putter",
                    'link': next_page
                }

        b = open("postscrape/spiders/new_releases_links.txt", 'a+')

        for l in indiv_links:
            b.write(f"'{l}',\n")