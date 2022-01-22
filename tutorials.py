from email import header
from tracemalloc import start
from unicodedata import name
import scrapy


class tutorial(scrapy.Spider):
    name='tutor'
    start_urls =[
        'https://www.coursef.com/'
    ]

    def parse(self, response):
        h3=response.css('h3::text').extract()
        yield {'header':h3}
    