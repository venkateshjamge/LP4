'''scrapy runspider quoteCrawler.py
Output in terminal
'''
import scrapy

class QuoteCrawlerSpider(scrapy.Spider):
    name = 'quoteCrawler'
    start_urls = ['https://quotes.toscrape.com/']

    counter = 0

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }
            if self.counter == 5:
                break

        next_page_url = response.css("li.next > a::attr(href)").extract_first()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

        self.counter += 1
        