import scrapy
from ..items import DatailItem
class datailSpide(scrapy.Spider):
	name='datail'
	start_urls=['http://699pic.com/tupian/lvxing.html']
	def parse(self,response):
		item=DatailItem()
		title=response.xpath(".//div[@class='swipeboxEx']/div/div[3]/h2/a/text()").extract()
		img=response.xpath(".//div[@class='swipeboxEx']/div/a/img/@data-original").extract()
		url=response.xpath(".//div[@class='swipeboxEx']/div/div[3]/h2/a/@href").extract()