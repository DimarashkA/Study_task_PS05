import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css('div.WdR1o')
        for svet in svets:
            yield {
                'name' : svet.css('div.wYUX2 span::text').get(),
                'price' : svet.css('div.ui-LD-ZU KIkOH span::text').get(),
                'url' : svet.css('a').attrib['href']
            }
