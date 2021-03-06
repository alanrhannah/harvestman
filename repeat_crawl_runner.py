import requests
import subprocess

import general_settings as settings

run_crawl_runner = ['/home/queryclick/.virtualenvs/harvestman/bin/python',
                    '/home/queryclick/harvestman/crawl_runner.py',
                    '-f',
                    '/home/queryclick/data/scrapy_input/long_list.txt',
                    '-c',
                    'gb',
                    '-r',
                    '10']

def main():
    list_jobs = request_list_jobs()
    if len(list_jobs.json()['pending']) == 0:
        subprocess.call(run_crawl_runner)

def request_list_jobs():
    url = settings.SCRAPYD_LIST_JOBS + '?project=harvestman'
    r = requests.get(url)
    if r.status_code != 200:
        return False
    else:
        return r

if __name__ == '__main__':
    main()
