import scrapy
from scrapy import Request
from Douban_movie_top250.items import DoubanMovieTop250Item


class DoubanSpider(scrapy.Spider):
    name = 'Douban'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        for i in range(10):
            url = f'https://movie.douban.com/top250?start={25 * i}&filter='
            yield Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for li in response.xpath("//ol[@class='grid_view']/li"):
            item = DoubanMovieTop250Item()
            item['rank'] = li.xpath(".//div[@class='pic']/em/text()").extract_first()
            item['name'] = li.xpath(".//div[@class='hd']/a/span[@class='title']/text()").extract_first()
            item['pic_link'] = li.xpath(".//div[@class='pic']/a/img/@src").extract_first()
            item['info'] = li.xpath(".//div[@class='bd']/p/text()").extract()[1].strip()
            item['director_actor'] = li.xpath(".//div[@class='bd']/p/text()").extract_first().strip()
            item['rating_score'] = li.xpath(".//div[@class='star']/span[2]/text()").extract_first()
            item['rating_num'] = li.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            item['introduce'] = li.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield item