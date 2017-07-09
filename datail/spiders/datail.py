import scrapy
from ..items import DatailItem
class datailSpide(scrapy.Spider):
	name='datail'
	start_urls=['http://699pic.com/tupian/lvxing.html']
	def parse(self,response):
		urls=response.xpath(".//div[@class='swipeboxEx']/div/div[3]/h2/a/@href").extract()
		for datail_url in urls:
			url=[]
			url.append(datail_url)
			yield scrapy.Request(datail_url,callback=self.parse_datail,meta={'url':url})
		next_url=response.xpath(".//a[@class='downPage']/@href").extract()[0]
		if next_url:
			next_url='http://699pic.com'+next_url
			yield scrapy.Request(next_url,callback=self.parse)
	def parse_datail(self,response):
		item=DatailItem()
		title=response.xpath(".//*[@id='wrapper']/div[1]/div/div/div[1]/div[1]/h1/text()").extract()
		img=response.xpath(".//*[@id='photo']/@src").extract()
		url=response.meta['url']
		for t,i,u in zip(title,img,url):
			item['title']=t
			item['img']=i
			item['url']=u
			yield item

		

