import scrapy
from ubcscraper.loaders import CourseLoader, SectionLoader
from ubcscraper.items import Course, Section

class UBCSpider(scrapy.Spider):
    name = 'UBC Spider'

    def start_requests(self):
        yield scrapy.Request('https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=0&sessyr={0}&sesscd={1}'.format(self.year, self.session.upper()), self.parse)

    def parse(self, response):
        for row in response.xpath('body/div/div/table//a'):
            if row.xpath('./text()').extract()[0] in self.to_scrape:
                href = row.xpath('./@href')[0]
                yield response.follow(href, self.parse_department)

    def parse_department(self, response):
        for href in response.xpath('body/div/div/table//a/@href'):
            yield response.follow(href, self.parse_course)

    def parse_course(self, response):
        for row in response.xpath('body/div/div/table/tr'):
            yield self.parse_section(row)

    def parse_section(self, row):
        sl = SectionLoader(item=Section(), selector=row)
        sl.add_xpath('course', './td[2]/a/text()', re='(\w{4}\s\w{3,4})')
        sl.add_xpath('code', './td[2]/a/text()')
        sl.add_xpath('status', './td[1]')
        sl.add_xpath('activity', './td[3]')
        sl.add_xpath('term', './td[4]', re='(\d+)')
        sl.add_xpath('days', './td[6]', re='(\w{3})')
        sl.add_xpath('start', './td[7]')
        sl.add_xpath('end', './td[8]')
        return sl.load_item()
