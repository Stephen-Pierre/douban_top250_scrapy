import scrapy
from douban_movie.items import DoubanMovieItem

class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        el_list = response.xpath('//*[@id="content"]//div[@class="info"]')
        print(len(el_list))

        for res in el_list:
            item = DoubanMovieItem()
            item['name'] = res.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['score'] = res.xpath('//*[@id="content"]//div/span[@class="rating_num"]/text()').extract_first()
            yield item

        next_page_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_page_url:
            url = response.urljoin(next_page_url)
            yield scrapy.Request(
                url=url
            )


