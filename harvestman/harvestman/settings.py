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
#USER_AGENT = 'harvestman (+http://www.yourdomain.com)'

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
            'https://www.google.com.qa', # Qatar
            'https://www.google.ae', # United Arab Emirates
            'https://www.google.co.jp', # Japan
            'https://www.google.ru', # Russia
            'https://www.google.co.in', # India
            'https://www.google.cn', # China not working
            # Europe
            'https://www.google.co.uk', # UK
            'https://www.google.ie', # Ireland
            'https://www.google.bg', # Bulgaria
            'https://www.google.pl', # Poland
            'https://www.google.fi', # Finland
            'https://www.google.no', # Norway
            'https://www.google.se', # Sweden
            'https://www.google.it', # Italy
            'https://www.google.pt', # Portugal
            'https://www.google.es', # Spain
            'https://www.google.at', # Austria
            'https://www.google.fr', # France
            'https://www.google.de', # Germany
            'https://www.google.nl', # Netherlands
            'https://www.google.ch', # Switzerland
            'https://www.google.ro', # Romania
            # North America
            'https://www.google.com', # US
            'https://www.google.ca', # Canada
            'https://www.google.com.mx', # Mexico
            # South America
            'https://www.google.cl', # Chile
            'https://www.google.com.co', # Colombia
            'https://www.google.com.br', # Brazil
            'https://www.google.com.pe', # Peru
            'https://www.google.com.ar', # Argentina
            'https://www.google.com.bo', # Bolivia
            'https://www.google.co.ve', # Venezuela
            # Australia & New Zealand
            'https://www.google.com.au', # Australia
            'https://www.google.co.nz', # New Zealand
            # Africa
            'https://www.google.com.ng', # Nigeria
            'https://www.google.co.za', # South Africa
            'https://www.google.dz', # Algeria
	]
