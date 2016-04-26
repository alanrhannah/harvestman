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

### Project Requirements

```bash
# local environment
$ pip install -r requirements/dev.txt
```

```bash
# production environment
$ pip install -r requirements/prod.txt
```
