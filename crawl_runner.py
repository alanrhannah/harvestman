import argparse
import requests
import sys

from utils import split_list_of_queries

# from harvestman.utils import split_list_of_queries

class CrawlRunner(object):

    def __init__(self, arguments):
        self.arguments = arguments

    def main(self):
        crawl_request_json_payloads = []
        for phrase in split_list_of_queries(self.arguments.file_path[0]):
            crawl_request_json_payloads.append(
                create_crawl_request_json_payload)
        
        import ipdb; ipdb.set_trace()
        pass
        

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