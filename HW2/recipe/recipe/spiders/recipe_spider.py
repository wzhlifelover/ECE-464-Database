from scrapy import Spider
from scrapy.selector import Selector
from recipe.items import RecipeItem

class RecipeSpider(Spider):
    name = "recipe"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

def parse(self, response):
    rinfos = Selector(response).xpath('//div[@class="summary"]/h3')

    for rinfo in rinfos:
        item = RecipeItem()
        item['title'] = rinfo.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
        yield item



