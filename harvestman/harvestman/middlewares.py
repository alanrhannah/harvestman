import random
from harvestman import settings

class ProxyMiddleware(object):

	def process_request(self, request, spider):
		proxy_string = random.choice(settings.PROXIES)
		request.meta['proxy'] = "http://{}".format(proxy_string)