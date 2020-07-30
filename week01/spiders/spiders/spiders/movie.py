import scrapy
from scrapy.selector import Selector
from ..items import SpidersItem


class MovieSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'movie'
    allowed_domains = ['manyan.com']
    # 起始url队列
    start_urls = ['http://manyan.com/']

#    def parse(self, response):
#        pass

    MOVIE_COUNT = 10

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        i = 0
        for movie in movies:
            if i == self.MOVIE_COUNT:
                break
            i += 1
            item = SpidersItem()
            movie_name = movie.xpath('./div[1]/span/text()')
            movie_type = movie.xpath('./div[2]/text()')
            movie_date = movie.xpath('./div[4]/text()')
            print("".join(movie_name.extract()).strip())
            item['movie_name'] = "".join(movie_name.extract()).strip()
            print("".join(movie_type.extract()).strip())
            item['movie_type'] = "".join(movie_type.extract()).strip()
            print("".join(movie_date.extract()).strip())
            item['movie_date'] = "".join(movie_date.extract()).strip()
            yield item

