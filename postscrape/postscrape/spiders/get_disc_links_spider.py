import scrapy
import json

# ACTIVATE VENV
# --- cd into top postscrape folder
# --- source venv/bin/activate

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
    name = "get_disc_links"

    start_urls = [
        "https://infinitediscs.com/category/Discmania/",
        "https://infinitediscs.com/category/Discraft/",
        "https://infinitediscs.com/category/Dynamic-Discs/",
        "https://infinitediscs.com/category/Gateway/",
        "https://infinitediscs.com/category/Infinite-Discs/",
        "https://infinitediscs.com/category/Innova/",
        "https://infinitediscs.com/category/Latitude-64/",
        "https://infinitediscs.com/category/MVP/",
        "https://infinitediscs.com/category/prodigy/",
        "https://infinitediscs.com/category/abc/",
        "https://infinitediscs.com/category/Above-Ground-Level/",
        "https://infinitediscs.com/category/AquaFlight/",
        "https://infinitediscs.com/category/Arsenal-Discs/",
        "https://infinitediscs.com/category/Axiom'/",
        "https://infinitediscs.com/category/Crosslap/",
        "https://infinitediscs.com/category/Daredevil/",
        "https://infinitediscs.com/category/DGA/",
        "https://infinitediscs.com/category/Disc-King/",
        "https://infinitediscs.com/category/Element-Discs/",
        "https://infinitediscs.com/category/Fourth-Circle-Discs/",
        "https://infinitediscs.com/category/Full-Turn/",
        "https://infinitediscs.com/category/Galaxy-Disc-Golf/",
        "https://infinitediscs.com/category/Guru-Disc-Golf/",
        "https://infinitediscs.com/category/Hyzer-Bomb/",
        "https://infinitediscs.com/category/Kastaplast/",
        "https://infinitediscs.com/category/Kaufinator-Discs/",
        "https://infinitediscs.com/category/Legacy/",
        "https://infinitediscs.com/category/Lightning-Discs/",
        "https://infinitediscs.com/category/Millennium/",
        "https://infinitediscs.com/category/Mint-Discs/",
        "https://infinitediscs.com/category/Nite-Ize/",
        "https://infinitediscs.com/category/Ozone-Discs/",
        "https://infinitediscs.com/category/Plastic-Addicts/",
        "https://infinitediscs.com/category/Prodiscus/",
        "https://infinitediscs.com/category/Reptilian-Disc-Golf/",
        "https://infinitediscs.com/category/RPM-Discs/",
        "https://infinitediscs.com/category/Salient/",
        "https://infinitediscs.com/category/Skyquest/",
        "https://infinitediscs.com/category/Storm-Disc-Golf/",
        "https://infinitediscs.com/category/Streamline/",
        "https://infinitediscs.com/category/Thought-Space-Athletics/",
        "https://infinitediscs.com/category/TOBU/",
        "https://infinitediscs.com/category/UB/",
        "https://infinitediscs.com/category/Vibram/",
        "https://infinitediscs.com/category/Viking-Discs/",
        "https://infinitediscs.com/category/Yikun/"
    ]

    def parse(self, response):
        baseURL = response.url[:25]
        originalURL = response.url

        if response.css('#ContentPlaceHolder1_lblCategoryName::text').get() is not None:
            brand = response.css(
                '#ContentPlaceHolder1_lblCategoryName::text').get().strip()
        else:
            brand = "N/A"

        indiv_links = []

        # There are 4 different loops happening for grabbing discs. This is done because there is a header item that says whether a disc is a distance driver, fairway, mid range or putter.
        # We loop through each section seperately so we can store that discs type inside its dict.

        for post in response.css('div#ContentPlaceHolder1_pnlDD div.row article.col-sm-6'):
            next_page = baseURL + \
                post.css('.thumbnail .caption p .btn::attr(onclick)').get()[
                    22:-1].strip()
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
            indiv_links.append(next_page)

            yield {
                'brand': brand,
                'title': post.css('.thumbnail .caption h4::text')[0].get().strip(),
                'infinite_ratings': post.css('.thumbnail .caption .pull-left small::text').get().strip(),
                'image': post.css('.thumbnail .img-responsive::attr(src)').get().strip(),
                'type': "Putter",
                'link': next_page
            }

        b = open("postscrape/spiders/links.txt", 'a+')

        for l in indiv_links:
            b.write(f"'{l}',\n")
