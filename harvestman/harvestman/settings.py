# -*- coding: utf-8 -*-

# Scrapy settings for harvestman project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'harvestman'

SPIDER_MODULES = ['harvestman.spiders']
NEWSPIDER_MODULE = 'harvestman.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
	'(KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 '
	'Safari/537.36')

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'harvestman.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'harvestman.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'harvestman.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

ALLOWED_DOMAINS = [
    # Asia
    'google.com.qa', # Qatar
    'google.ae', # United Arab Emirates
    'google.co.jp', # Japan
    'google.ru', # Russia
    'google.co.in', # India
    'google.cn', # China not working
    # Europe
    'google.co.uk', # UK
    'google.ie', # Ireland
    'google.bg', # Bulgaria
    'google.pl', # Poland
    'google.fi', # Finland
    'google.no', # Norway
    'google.se', # Sweden
    'google.it', # Italy
    'google.pt', # Portugal
    'google.es', # Spain
    'google.at', # Austria
    'google.fr', # France
    'google.de', # Germany
    'google.nl', # Netherlands
    'google.ch', # Switzerland
    'google.ro', # Romania
    # North America
    'google.com', # US
    'google.ca', # Canada
    'google.com.mx', # Mexico
    # South America
    'google.cl', # Chile
    'google.com.co', # Colombia
    'google.com.br', # Brazil
    'google.com.pe', # Peru
    'google.com.ar', # Argentina
    'google.com.bo', # Bolivia
    'google.co.ve', # Venezuela
    # Australia & New Zealand
    'google.com.au', # Australia
    'google.co.nz', # New Zealand
    # Africa
    'google.com.ng', # Nigeria
    'google.co.za', # South Africa
    'google.dz' # Algeria
]

START_INDEX = 0
RANK = 1
