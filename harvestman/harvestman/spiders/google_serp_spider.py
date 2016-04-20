import scrapy

class GoogleSerpSpider(scrapy.Spider):
	name = 'google_serp_spider'
	allowed_domains = []
	start_urls = []

	def parse(self, response):
		filename  = ''
		with open(filename, 'wb') as f:
			f.write(response.body)

