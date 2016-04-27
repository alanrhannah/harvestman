import random
from harvestman.harvestman_spider import settings

class ProxyMiddleware(object):
	"""Custom middleware to route requests via a proxy."""

	def process_request(self, request, spider):
		"""
		Select a random proxy from a list and assign to the request meta 
		information
		"""
		proxy_string = random.choice(settings.PROXIES)
		request.meta['proxy'] = "http://{}".format(proxy_string)


class CustomStatusCodeMiddleware(object):
	"""
	Custom middleware to handle anything other than a 200 status response
	code from the spider.
	"""

	def process_response(self, request, response, spider):
		"""
		Process response status codes and update response body if required.
		:return response: a scrapy html response object
		"""
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
