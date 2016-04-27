import random
from harvestman.harvestman_spider import settings

class ProxyMiddleware(object):

	def process_request(self, request, spider):
		proxy_string = random.choice(settings.PROXIES)
		request.meta['proxy'] = "http://{}".format(proxy_string)

class CustomStatusCodeMiddleware(object):

	def process_response(self, request, response, spider):
		if response.status >= 300 and response.status < 400:
			message = '{} Redirected request, cannot parse results'.format(
				response.status)
			response = response.replace(body=message)
		elif response.status >= 400 and response.status < 500:
			message = '{} Client error, cannot parse results'.format(
				response.status)
			response = response.replace(body=message)
		elif response.status >= 500:
			message = '{} Server error, cannot parse results'.format(
				response.status)
			response = response.replace(body=message)
		return response
