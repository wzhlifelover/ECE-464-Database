from scrapy import Spider
from scrapy.selector import Selector

from recipe.items import RecipeItem

class RecipeSpider(Spider):
	name = "recipe"
	allowed_domains = ["www.tasteofhome.com/recipes/"]
	start_urls = [
			"https://www.tasteofhome.com/recipes/",
	]

	def parse(self, response):
		rinfos = Selector(response).xpath('//li[@class="single-recipe"]')
		
		for rinfo in rinfos:
			item = RecipeItem()
			item['title'] = rinfo.xpath('a/div[@class="recipe-content"]/div[@class="recipe-text"]/h4/text()').extract()[0]
			item['url'] = rinfo.xpath('a/@href').extract()[0]
			yield item
