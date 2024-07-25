import scrapy
import csv
import os

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet/page-7"]

    def __init__(self):
        # Проверка, существует ли файл
        file_exists = os.path.isfile('svetnewpars.csv')

        # Открыть файл в режиме добавления
        self.file = open('svetnewpars.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)

        # Записать заголовки только если файл только что создан
        if not file_exists:
            self.writer.writerow(['name', 'price', 'url'])

    def parse(self, response):
        svets = response.css('div.WdR1o')
        for svet in svets:
            name = svet.css('div.wYUX2 span::text').get()
            price = svet.css('div.q5Uds span::text').get()
            url = response.urljoin(svet.css('a').attrib['href'])
            self.writer.writerow([name, price, url])

    def closed(self, reason):
        # Закрыть файл при завершении работы паука
        self.file.close()

# scrapy crawl svetnewpars - код запуска
