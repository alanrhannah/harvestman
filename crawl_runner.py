import argparse
import requests
import general_settings as settings
import sys

from harvestman.harvestman_spider.utils import split_list_of_queries


class CrawlRunner(object):

    def __init__(self, arguments):
        self.arguments = arguments

    def main(self):
        
        crawl_request_json_payloads = []
        for phrase in split_list_of_queries(self.arguments.file_path[0]):
            crawl_request_json_payloads.append(
                self.create_crawl_request_json_payload(phrase))

        for payload in crawl_request_json_payloads:
            request = self.send_crawl_request(payload)
            response = self.handle_crawl_request_response(request)
            if not response:
                break

    def send_crawl_request(self, payload):
        response = None
        try:
            response = requests.post(settings.SCRAPYD_SCHEDULE_JOB,
                                     data=payload,
                                     allow_redirects=False)
        except requests.ConnectionError, e:
            print(e)

        return response
        
    def handle_crawl_request_response(self, response):
        if response.status_code >= 400:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                return False  
        else:
            return True

    def create_crawl_request_json_payload(self, phrase):
        payload = {
            'spider': 'google_serp_spider',
            'project': 'harvestman',
            'phrase': phrase,
            'country': self.arguments.country[0]
        }
        
        if self.arguments.results_per_page:
            payload['results_per_page'] =\
                str(self.arguments.results_per_page[0])
        
        return payload
       

def parse_arguments(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        '--file_path',
                        help=('The absolute path to the file containing '
                              'your keyphrases'),
                        type=str,
                        nargs=1,
                        required=True)

    parser.add_argument('-c',
                        '--country',
                        help=('The two letter ISO_3166-1_alpha-2 code for '
                              'the country you wish to crawl google in.'),
                        type=str,
                        nargs=1,
                        required=True)

    parser.add_argument('-r',
                        '--results_per_page',
                        help=('The number of results per page to scrape. '
                              'This defaults to 10.'),
                        type=int,
                        nargs=1)

    return parser.parse_args(arguments)

if __name__ == '__main__':
    arguments = parse_arguments(sys.argv[1:])
    CrawlRunner(arguments).main()