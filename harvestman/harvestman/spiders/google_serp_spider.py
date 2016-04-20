import scrapy

from haravestman import settings
from harvestman.items import HarvestmanItem

class GoogleSerpSpider(scrapy.Spider):
	name = 'google_serp_spider'
	domain_name = 'google'
	allowed_domains = settings.ALLOWED_DOMAINS
	start_urls = []

	def parse(self, response):
		filename  = ''
		with open(filename, 'wb') as f:
			f.write(response.body)

