from __future__ import absolute_import

import datetime
import re
import scrapy

from harvestman.harvestman_spider import settings
from harvestman.harvestman_spider.utils import update_url_start_index_parameter
from harvestman.harvestman_spider.items import HarvestmanItem

class GoogleSerpSpider(scrapy.Spider):
    name = 'google_serp_spider'
    domain_name = 'google'
    allowed_domains = settings.ALLOWED_DOMAINS
    start_index = settings.START_INDEX
    rank = settings.RANK 
    results_per_page = 10

    phrase = 'kalignite market share'
    base_url = 'https://www.google.co.uk/search?gl=gb&q={}&start={}&num={}&gbv=1'
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


    def log_response_code(self, response):
        """Log response codes if not 200"""
        self.logger.warning('{} - {} - {}'.format(
                response.body, self.query, self.user_agent))

    def parse(self, response):
        """
        Parse the crawled serp results page

        :param response:    scrapy response object
        :returns items:     dict of items to be processed
        """
        if response.status >= 300:
            self.log_response_code(response)
            yield scrapy.Request(response.request.url, self.parse)

        with open('ip_log.log', 'a+') as ip_log_file:
            dt = datetime.datetime.today().strftime('%d-%m-%y %H:%M:%S')
            url = response.request.url
            proxy_ip = response.headers['X-Crawlera-Slave']
            log_line = '{}, {}, {}'.format(dt, url, proxy_ip)
            ip_log_file.write(log_line)

        results = None
        # Get the section containing the results
        results = response.xpath('//div[@class="g"]')

        duplicated_results_para = False
        duplicated_results_para = response.xpath('//p[@id="ofr"]').extract()

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

        if estimated < 100:
            ex_results = estimated
        else: 
            ex_results = 100

        if results and self.rank < ex_results and not duplicated_results_para:
            start_param_to_replace = update_url_start_index_parameter(
                self.start_index)
            self.start_index += self.results_per_page
            start_param_replacement = update_url_start_index_parameter(
                self.start_index)
            next_page_url = response.request.url.replace(
                start_param_to_replace,
                start_param_replacement)
            self.logger.info('requesting: {}'.format(next_page_url))
            yield scrapy.Request(next_page_url, self.parse)
        
        elif duplicated_results_para:
            duplicated_results_para = re.sub(r'<[^>]*?>',
                                             '',
                                             duplicated_results_para[0])
            self.logger.info('Duplicated Results, < 100: {}'.format(
                duplicated_results_para))

        if results:
            for result in results:
                if result.xpath('div[@class="s"]'):
                    if self.rank <= ex_results:
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
                        link = "".join(result.xpath(
                            'h3[@class="r"]/a/@href').extract())

                        if not link.startswith('/images?q='):
                            if link.startswith('/url?q='):
                                link = link.split('&sa')
                                item['link'] = link[0].replace('/url?q=', '')
                            items.append(item)
                            self.rank += 1
                        
                        yield item
