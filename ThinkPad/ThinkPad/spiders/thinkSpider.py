# -*- coding: utf-8 -*-
import scrapy

from ThinkPad.items import ThinkpadItem


class ThinkspiderSpider(scrapy.Spider):
    name = 'thinkSpider'
    allowed_domains = ['detail.zol.com.cn']
    # start_urls = ['http://detail.zol.com.cn/index.php?c=SearchList&keyword=ThinkPad&page=1']
    start_urls = ['https://www.jinyongwang.com/book/']
    cookie = {'Cookie': 'UM_distinctid=166d3282a5840a-0ff0a4a63309b2'
                        '-1e386652-fa000-166d3282a5a29a; Hm_lvt_581788f461708'
                        'b27b0f6ad74c67039df=1541140919; redconfig=0%7C0%7C0%'
                        '7C1%7C0; lastbook=%u7B2C01%u7AE0%u3000%u5927%u96E8%u554'
                        '6%u5BB6%u5821%7Chttps%3A//www.jinyongwang.com/fei/484.html'
                        '%7Chttps%3A//www.jinyongwang.com/fei/%7C%u98DE%u72D0%u5916%u4'
                        'F20%u4FEE%u8BA2%u7248; CNZZDATA1261114680=811014928-1541137125-'
                        'https%253A%252F%252Fwww.google.com%252F%7C1541142525; Hm_lpvt_5'
                        '81788f461708b27b0f6ad74c67039df=1541143642'}

    def start_requests(self):
        for url in self.start_urls:
            # print(url)
            yield scrapy.Request(url, callback=self.parse, cookies=self.cookie)

    def parse(self, response):

        print('step1')
        all_books = response.xpath('//div[@class="booklist"]/ul[@class="list"]/li')
        # print(all_books)

        # book = all_books[0]
        # new_url = book.xpath('.//p[1]/a/@href').get()
        # new_url = 'https://www.jinyongwang.com' + new_url
        # book_title = book.xpath('.//p[2]/a/text()').get()
        # yield scrapy.Request(new_url, meta={'book_title': book_title}, callback=self.parse2, dont_filter=True)

        for book in all_books:
            new_url = book.xpath('.//p[1]/a/@href').get()
            new_url = 'https://www.jinyongwang.com' + new_url
            book_title = book.xpath('.//p[2]/a/text()').get()
            yield scrapy.Request(new_url, meta={'book_title': book_title}, callback=self.parse2, dont_filter=True)

    def parse2(self, response):
        new_lis = response.xpath('//ul[@class="mlist"]/li')
        book_title = response.meta['book_title']

        # li = new_lis[0]
        # new_url = li.xpath('.//a/@href').get()
        # new_url = 'https://www.jinyongwang.com' + new_url
        # print(new_url, book_title)
        # yield scrapy.Request(new_url, meta={'book_title': book_title}, callback=self.parse3, dont_filter=True)

        for li in new_lis:
            new_url = li.xpath('.//a/@href').get()
            new_url = 'https://www.jinyongwang.com' + new_url
            print(new_url, book_title)
            yield scrapy.Request(new_url, meta={'book_title': book_title}, callback=self.parse3, dont_filter=True)

        # yield {}

    def parse3(self, response):
        book_title = response.meta['book_title']
        caption = response.xpath('//div[@class="top"]/h1/text()').get()
        detail = ''.join(response.xpath('//div[@id="vcon"]/p/text()').extract())
        item = ThinkpadItem()
        item['book_title'] = book_title
        item['caption'] = caption
        item['detail'] = detail
        # print(detail)
        yield item

