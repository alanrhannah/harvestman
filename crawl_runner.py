import os
import argparse
import requests
import general_settings as settings
import sys

from harvestman.harvestman_spider.utils import split_list_of_queries


class CrawlRunner(object):
    """
    Parse command line arguments, split input file into a list, generate 
    data payloads and send request to scrapyd api.
    """

    def __init__(self, arguments):
        """
        Accept parsed command line arguments.

        Set object variable. 

        :param arguments:  argparse namespace arguments 
        """
        self.arguments = arguments

    def main(self):
        """
        Build a list of crawl request payloads.
        Iterate through a list of payloads.
        """
        self.payloads = self.build_list_of_crawl_request_payloads()
        self.iterate_list_of_crawl_request_payloads()
        
    def build_list_of_crawl_request_payloads(self):
        """
        Iterate through a list of queries from an input file.
        Append a dictionary of values to a list

        :returns crawl_request_payloads:  A list of dictionaries.
        """
        crawl_request_payloads = []
        for phrase in split_list_of_queries(self.arguments.file_path[0]):
            crawl_request_payloads.append(
                self.create_crawl_request_payload(phrase))

        return crawl_request_payloads

    def iterate_list_of_crawl_request_payloads(self):
        """
        Iterate through a list of dictionaries, make a request and handle
        any response errors.
        """
        for payload in self.payloads:
            request = self.send_crawl_request(payload)
            response = self.handle_crawl_request_response(request)
            if not response:
                break

    def send_crawl_request(self, payload):
        """
        Send a request to the scrayd schedule job API endpoint.
        Process exceptions if required.

        :param payload:     A dictionary 
        :returns response:  A requests response object (if request sucessful)
        """
        response = None
        try:
            response = requests.post(settings.SCRAPYD_SCHEDULE_JOB,
                                     data=payload,
                                     allow_redirects=False)
        except requests.ConnectionError, e:
            # TODO - Change to logging and raise exception
            print(e)
        return response
        
    def handle_crawl_request_response(self, response):
        """
        Process a requests response. 

        Raise an exception in the event that the server is unreachable.

        :params response:  A request.Response object
        :returns bool:     True or False depending on response.status_code
        """
        if response.status_code >= 400:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                return False  
        else:
            return True

    def create_crawl_request_payload(self, phrase):
        """
        Populate a dictionary with data and return the dictionary.

        :params phrase:    a string
        :returns payload:  a dictionary
        """
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
    """
    Add arguments to command line.
    Parse arguments to argparse namesapce.

    :params arguments:  a list of arguments from sys.argv
    :returns parser.parse_args(arguments):  argparse namespace object 
    """
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
