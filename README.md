# harvestman
SERP Scraper

## Usage

### System Requirements / Setup

Make sure you have the following system dependencies installed and up to date for **Ubuntu/Debian**:

```bash
$ sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

Install virtualenv and virtualenvwrapper (if not existing):

```bash
$ pip install virtualenv virtualenvwrapper
```

Add additional information to your `~/.bashrc` file.

Firstly, find the `virtualenvwrapper.sh` script by

```bash
$ which virtualenvwrapper.sh
/usr/local/bin/virtualenvwrapper.sh
```

Take the file path from the above command and add the following environment variables in your `~/.bashrc` file with the editor of your choice:

```
# where to store our virtual envs
export WORKON_HOME=$HOME/.virtualenvs
# where projects will reside
export PROJECT_HOME=$HOME/development
# where is the virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper.sh
```

Once you have saved the file, re-source the `~/.bashrc` file with:

```bash
$ . ~/.bashrc
```

Create a new virtual environment to install the project requirements too.

```bash
$ mkvirtualenv harvestman
```

Your terminal should look like:

```bash
(harvestman) alan@QC-LX00297:$
```

To activate the virtualenv:

```bash
$ workon harvestman
```

To deactivate the virtualenv:
```bash
$ deactivate
```

You will need to set some environment variables in your `.bashrc` file:

set `DATA_EXPORT_DIR` to a directory of your choice
set `PROXIES` to a comma seperated string of proxies with the format `<ip address>:<port>`

### Project Requirements

```bash
# local environment
$ pip install -r requirements/dev.txt
```

```bash
# production environment
$ pip install -r requirements/prod.txt
```
---

## Running the spider(s)

With your virtualenv actiavted, run `scrapyd &` from the root directory of the harvestman project to start the server in the background.

Run spiders via `python crawl_runner.py`. 

Full usage:

```bash
$ python crawl_runner.py --help

usage: crawl_runner.py [-h] -f FILE_PATH -c COUNTRY [-r RESULTS_PER_PAGE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PATH, --file_path FILE_PATH
                        The absolute path to the file containing your
                        keyphrases
  -c COUNTRY, --country COUNTRY
                        The two letter ISO_3166-1_alpha-2 code for the country
                        you wish to crawl google in.
  -r RESULTS_PER_PAGE, --results_per_page RESULTS_PER_PAGE
                        The number of results per page to scrape. This
                        defaults to 10.
```
