import os 
SCRAPYD_SERVER = 'http://127.0.0.1:6800/{}'
SCRAPYD_SCHEDULE_JOB = SCRAPYD_SERVER.format('schedule.json')
SCRAPYD_LIST_JOBS = SCRAPYD_SERVER.format('listjobs.json')

TEST_ASSETS_DIR = os.path.join(os.getcwd(), 'testing_assets')
