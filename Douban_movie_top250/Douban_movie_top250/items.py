import scrapy


class DoubanMovieTop250Item(scrapy.Item):
    name = scrapy.Field()
    pic_link = scrapy.Field()
    rank = scrapy.Field()
    director_actor = scrapy.Field()
    info = scrapy.Field()
    rating_score = scrapy.Field()
    rating_num = scrapy.Field()
    introduce = scrapy.Field()