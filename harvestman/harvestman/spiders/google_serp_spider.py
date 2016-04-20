import os
import scrapy

from harvestman import settings
# from harvestman.items import HarvestmanItem
from harvestman.utils import split_list_of_queries


class GoogleSerpSpider(scrapy.Spider):
    name = 'google_serp_spider'
    domain_name = 'google'
    allowed_domains = settings.ALLOWED_DOMAINS
    start_index = settings.START_INDEX
    rank = settings.RANK 

    def __init__(self, *args, **kwargs):

        super(GoogleSerpSpider, self).__init__(*args, **kwargs)
        if kwargs.get('file'):
            filepath = kwargs['file']
            if os.path.exists(filepath):
                self.queries = split_list_of_queries(filepath)

        if kwargs.get('country'):
            self.base_url = settings.BASE_SEARCH_URLS[kwargs['country']]

        for query in self.queries:
            query_url = self.base_url.format(query, self.start_index)
            self.start_urls.append(query_url)

        import ipdb; ipdb.set_trace()

    def parse(self, response):
        pass

