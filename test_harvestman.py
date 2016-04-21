import json
import tempfile

from crawl_runner import parse_arguments, CrawlRunner
from utils import split_list_of_queries, update_url_start_index_parameter

def create_input_file():
    content = 'some keyword\nanother keyword\nsome more keywords\n'
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.write(content)
    tmp_file.close()
    return tmp_file

def create_class_instance(arg_list):
    arguments = parse_arguments(arg_list)
    cr = CrawlRunner(arguments)
    return cr

def test_split_list_of_queries():
    expected = ['some keyword', 'another keyword', 'some more keywords']
    content = create_input_file()
    keyword_list = split_list_of_queries(content.name)
    assert keyword_list == expected
    content.delete

def test_update_url_start_index_parameter():
    start_index = 10
    expected = '&start=10'
    assert update_url_start_index_parameter(start_index) == expected

def test_parse_arguments_required():
    short_args = parse_arguments(['-f', '/this/is/a/file/path',
                                  '-c', 'gb'])

    long_args = parse_arguments(['--file_path', '/this/is/a/file/path',
                                 '--country', 'gb'])

    expected_file_path = ['/this/is/a/file/path']
    expected_country = ['gb']

    assert short_args.file_path == expected_file_path
    assert long_args.file_path == expected_file_path
    assert short_args.country == expected_country
    assert long_args.country == expected_country

def test_parse_arguments_required_and_results_per_page():
    short_args = parse_arguments(['-f', '/this/is/a/file/path',
                                  '-c', 'gb',
                                  '-r', '50'])

    long_args = parse_arguments(['--file_path', '/this/is/a/file/path',
                                 '--country', 'gb',
                                 '--results_per_page', '50'])

    expected_file_path = ['/this/is/a/file/path']
    expected_country = ['gb']
    expected_results_per_page = [50]

    assert short_args.file_path == expected_file_path
    assert long_args.file_path == expected_file_path
    assert short_args.country == expected_country
    assert long_args.country == expected_country
    assert short_args.results_per_page == expected_results_per_page
    assert long_args.results_per_page == expected_results_per_page

def test_argument_vars():
    cr = create_class_instance(['-f', '/this/is/a/file/path', '-c', 'gb'])
    assert cr.arguments.country[0] == 'gb'
    assert cr.arguments.file_path[0] == '/this/is/a/file/path' 

def test_create_json_list_of_strings():
    content = create_input_file()
    cr = create_class_instance(['-f', content.name, '-c', 'gb'])
    crawl_request_json_payloads = []
    for phrase in split_list_of_queries(cr.arguments.file_path[0]):
        json_payload = {
            'phrase': phrase,
            'country': cr.arguments.country[0], 
        }
        crawl_request_json_payloads.append(json.dumps(json_payload))

    expected = [
        '{"phrase": "some keyword", "country": "gb"}',
        '{"phrase": "another keyword", "country": "gb"}',
        '{"phrase": "some more keywords", "country": "gb"}'
    ]
    assert crawl_request_json_payloads == expected

def test_create_json_payload():
    content = create_input_file()
    cr = create_class_instance(['-f', content.name, '-c', 'gb'])
    crawl_request_json_payloads = []
    
    for phrase in split_list_of_queries(cr.arguments.file_path[0]):
        crawl_request_json_payloads.append(
            cr.create_crawl_request_json_payload(phrase))

    expected = [
        '{"phrase": "some keyword", "country": "gb"}',
        '{"phrase": "another keyword", "country": "gb"}',
        '{"phrase": "some more keywords", "country": "gb"}'
    ]
    
    assert crawl_request_json_payloads == expected
