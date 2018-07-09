# UBC Course Scraper

UBC Course Scraper is a program that collects and parses course information from the [UBC Course Schedule](https://courses.students.ubc.ca). The application uses [Scrapy](https://scrapy.org) - a web crawling framework - to implement the web scraping functions.

### Requirements

Python 3.6.5 and Scrapy 1.5.0 or higher are required to execute this program. The use of a virtual environment is recommended, preferrably through [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/). All other dependencies are managed through `pip` once the user clones the repository via `pip install -r requirements.txt`.

### Usage

```shell
cd ubcscraper
scrapy crawl 'UBC' -a dept=<4 letter department code> -a year=<4 digit year> -a session=<W for winter or S for summer>
```

Scrapy outputs the scraped data to a 'JSON lines' file in the `data/` directory, named in the format `<dept code><year><session code>.jl`

### Settings

Review the [Avoiding Getting Banned](https://docs.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned) and [AutoThrottle extension](https://docs.scrapy.org/en/latest/topics/autothrottle.html) documents for additional information. The settings for spiders can be edited in `ubcscraper.settings`, but could also be set in the `myspider.py` files. More information is available in the [Scrapy documents](https://docs.scrapy.org/en/latest/topics/settings.html).
