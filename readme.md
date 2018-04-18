# UBC Course Scraper

This is a [Scrapy](https://scrapy.org) project built to collect and parse course information from the [UBC Course Schedule](https://courses.students.ubc.ca).

### Requirements

Python 3.6.5 and Scrapy 1.5.0 or higher are required. It's recommended to use a virtual environment, most likely through [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/). All other dependencies are managed through `pip` after cloning the repo via `pip install -r requirements.txt`.

### Usage

```shell
cd ubcscraper
scrapy crawl 'UBC' -a dept=<4 letter department code> -a year=<4 digit year> -a session=<W for winter or S for summer>
```

Scrapy will then output the scraped data to a 'JSON lines' file in the `data/` directory, named in the format `<dept code><year><session code>.jl`

### Settings

Take a look at [Avoiding Getting Banned](https://docs.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned) and the [AutoThrottle extension](https://docs.scrapy.org/en/latest/topics/autothrottle.html). The settings for the spiders can be found in `ubcscraper.settings`, but could also be set in the `myspider.py` files themselves. More info available in the [Scrapy docs](https://docs.scrapy.org/en/latest/topics/settings.html).
