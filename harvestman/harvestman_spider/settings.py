# -*- coding: utf-8 -*-
import os
# Scrapy settings for harvestman project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Mozilla'

SPIDER_MODULES = ['harvestman_spider.spiders']
NEWSPIDER_MODULE = 'harvestman_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
	'(KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 '
	'Safari/537.36')

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=5

COOKIES_ENABLED=False

DOWNLOADER_MIDDLEWARES = {
	'harvestman_spider.middlewares.CustomStatusCodeMiddleware': 120,
	'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
	'harvestman_spider.middlewares.ProxyMiddleware': 100,
}

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = { 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Connection': 'keep-alive',
}

ITEM_PIPELINES = {
    'harvestman_spider.pipelines.HarvestmanPipeline': 300,
}

ALLOWED_DOMAINS = [
    # Asia
    'google.com.qa',
    'google.ae',
    'google.co.jp',
    'google.ru',
    'google.co.in',
    'google.cn',
    # Europe
    'google.co.uk',
    'google.ie',
    'google.bg',
    'google.pl',
    'google.fi',
    'google.no',
    'google.se',
    'google.it',
    'google.pt',
    'google.es',
    'google.at',
    'google.fr',
    'google.de',
    'google.nl',
    'google.ch',
    'google.ro',
    # North America
    'google.com',
    'google.ca',
    'google.com.mx',
    # South America
    'google.cl',
    'google.com.co',
    'google.com.br',
    'google.com.pe',
    'google.com.ar',
    'google.com.bo',
    'google.co.ve',
    # Australia & New Zealand
    'google.com.au',
    'google.co.nz',
    # Africa
    'google.com.ng',
    'google.co.za',
    'google.dz' # Algeria
]

BASE_SEARCH_URLS = {
	# Asia
	'qa': 'https://www.google.com.qa/search?gl=qa&q={}&start={}&num={}&gbv=1',
	'ae': 'https://www.google.ae/search?gl=ae&q={}&start={}&num={}&gbv=1',
	'jp': 'https://www.google.co.jp/search?gl=jp&q={}&start={}&num={}&gbv=1',
	'ru': 'https://www.google.ru/search?gl=ru&q={}&start={}&num={}&gbv=1',
	'in': 'https://www.google.co.in/search?gl=in&q={}&start={}&num={}&gbv=1',
	'cn': 'https://www.google.cn/search?gl=cn&q={}&start={}&num={}&gbv=1',
	# Europe
	'gb': 'https://www.google.co.uk/search?gl=gb&q={}&start={}&num={}&gbv=1',
	'ie': 'https://www.google.ie/search?gl=ie&q={}&start={}&num={}&gbv=1',
	'bg': 'https://www.google.bg/search?gl=bg&q={}&start={}&num={}&gbv=1',
	'pl': 'https://www.google.pl/search?gl=pl&q={}&start={}&num={}&gbv=1',
	'fi': 'https://www.google.fi/search?gl=fi&q={}&start={}&num={}&gbv=1',
	'no': 'https://www.google.no/search?gl=no&q={}&start={}&num={}&gbv=1',
	'se': 'https://www.google.se/search?gl=se&q={}&start={}&num={}&gbv=1',
	'it': 'https://www.google.it/search?gl=it&q={}&start={}&num={}&gbv=1',
	'pt': 'https://www.google.pt/search?gl=pt&q={}&start={}&num={}&gbv=1',
	'es': 'https://www.google.es/search?gl=es&q={}&start={}&num={}&gbv=1',
	'at': 'https://www.google.at/search?gl=at&q={}&start={}&num={}&gbv=1',
	'fr': 'https://www.google.fr/search?gl=fr&q={}&start={}&num={}&gbv=1',
	'de': 'https://www.google.de/search?gl=de&q={}&start={}&num={}&gbv=1',
	'nl': 'https://www.google.nl/search?gl=nl&q={}&start={}&num={}&gbv=1',
	'ch': 'https://www.google.ch/search?gl=ch&q={}&start={}&num={}&gbv=1',
	'ro': 'https://www.google.ro/search?gl=ro&q={}&start={}&num={}&gbv=1',
	# North America
	'us': 'https://www.google.com/search?gl=us&q={}&start={}&num={}&gbv=1',
	'ca': 'https://www.google.ca/search?gl=ca&q={}&start={}&num={}&gbv=1',
	'mx': 'https://www.google.com.mx/search?gl=mx&q={}&start={}&num={}&gbv=1',
	# South America
	'cl': 'https://www.google.cl/search?gl=cl&q={}&start={}&num={}&gbv=1',
	'co': 'https://www.google.com.co/search?gl=co&q={}&start={}&num={}&gbv=1',
	'br': 'https://www.google.com.br/search?gl=br&q={}&start={}&num={}&gbv=1',
	'pe': 'https://www.google.com.pe/search?gl=pe&q={}&start={}&num={}&gbv=1',
	'ar': 'https://www.google.com.ar/search?gl=ar&q={}&start={}&num={}&gbv=1',
	'bo': 'https://www.google.com.bo/search?gl=bo&q={}&start={}&num={}&gbv=1',
	've': 'https://www.google.co.ve/search?gl=ve&q={}&start={}&num={}&gbv=1',
	# Australia & New Zealand
	'au': 'https://www.google.com.au/search?gl=au&q={}&start={}&num={}&gbv=1',
	'nz': 'https://www.google.co.nz/search?gl=nz&q={}&start={}&num={}&gbv=1',
	# Africa
	'ng': 'https://www.google.com.ng/search?gl=ng&q={}&start={}&num={}&gbv=1',
	'za': 'https://www.google.co.za/search?gl=za&q={}&start={}&num={}&gbv=1',
	'dz': 'https://www.google.dz/search?gl=dz&q={}&start={}&num={}&gbv=1'
}
	
PROXIES = os.environ['PROXIES'].split(',')

START_INDEX = 0
RANK = 1

BASE_DIR = os.environ['DATA_EXPORT_DIR']

CSV_FILE_OUTPUT_DIR = os.path.join(
    BASE_DIR, 'scrapy_results/{}_{}_{}.csv')

LOG_LEVEL = 'INFO'
