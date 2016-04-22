# from __future__ import absolute_import

import re
import scrapy

from harvestman import settings
from harvestman.utils import update_url_start_index_parameter
from harvestman.items import HarvestmanItem

class GoogleSerpSpider(scrapy.Spider):
    name = 'google_serp_spider'
    domain_name = 'google'
    allowed_domains = settings.ALLOWED_DOMAINS
    start_index = settings.START_INDEX
    rank = settings.RANK 
    results_per_page = 10

    def __init__(self, *args, **kwargs):

        super(GoogleSerpSpider, self).__init__(*args, **kwargs)
        
        if kwargs.get('phrase'):
            self.phrase = kwargs['phrase']
            
        if kwargs.get('country'):
            self.base_url = settings.BASE_SEARCH_URLS[kwargs['country']]

        if kwargs.get('results_per_page'):
            self.results_per_page = int(kwargs['results_per_page'])

        query_url = self.base_url.format(self.phrase,
                                         self.start_index,
                                         self.results_per_page)
        self.start_urls.append(query_url)

    def parse(self, response):
        """
        Parse the crawled serp results page
        :param response:    scrapy response object
        :returns items:     dict of items to be processed
        """
        if response.status != 200:
            scrapy.log.msg('{} - {} - {}'.format(
                response.body, self.query, self.user_agent))
            raise scrapy.CloseSpider(response.body)

        results = None
        # Get the section containing the results
        results = response.xpath('//div[@class="g"]')
        estimated = "".join(
            response.xpath('//div[@id="resultStats"]/text()').extract())
        estimated = estimated.replace(',', '')
        estimated = estimated.replace('.', '')

        tokens = estimated.split()
        nums = []

        # todo - refactor this grabbing of the estimated results number.
        for i in range(0, len(tokens)):
            if tokens[i].isdigit():
                nums.append(tokens[i])
        try:
            estimated = int(''.join(map(str, nums)))
        except:
            estimated = 0
        items = []

        if self.rank <= 100:
            start_param_to_replace = update_url_start_index_parameter(
                self.start_index)
            
            self.start_index += self.results_per_page
            
            start_param_replacement = update_url_start_index_parameter(
                self.start_index)

            next_page_url = response.request.url.replace(
                start_param_to_replace, start_param_replacement)

            yield scrapy.Request(next_page_url, self.parse)

        for result in results:
            if result.xpath('div[@class="s"]'):
                if self.rank <= 100:
                    item = HarvestmanItem()

                    item['keyphrase'] = self.phrase
                    item['rank'] = self.rank
                    item['estimated'] = estimated

                    try:
                        title = result.xpath('h3[@class="r"]/a').extract()
                        title = re.sub(r'<[^>]*?>', '', title[0])
                        title = title.encode('utf-8')
                    except IndexError:
                        print('IndexError')
                        continue

                    try:
                        snippet = result.xpath(
                            'div[@class="s"]//span[@class="st"]').extract()
                        snippet = re.sub(r'<[^>]*?>', '', snippet[0])
                        snippet = snippet.encode('utf-8')
                    except IndexError:
                        print('IndexError')
                        continue

                    item['title'] = title
                    item['snippet'] = snippet
                    item['link'] = "".join(result.xpath(
                        'h3[@class="r"]/a/@href').extract())

                    if not item['link'].startswith('/images?q='):
                        if item['link'].startswith('/url?q='):
                            item['link'] = item['link'].replace('/url?q=', '')
                        items.append(item)
                        self.rank += 1
                    yield item
