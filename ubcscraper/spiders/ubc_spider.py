import scrapy
from ubcscraper.loaders import CourseLoader, SectionLoader
from ubcscraper.items import Course, Section

class UBCSpider(scrapy.Spider):
    name = 'UBC Spider'

    def start_requests(self):
        yield scrapy.Request('https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=1&dept={0}&sessyr={1}&sesscd={2}'.format(self.dept, self.year, self.session), self.parse)

    def parse(self, response):
        for href in response.xpath('body/div/div/table//a/@href'):
            yield response.follow(href, self.parse_course)

    def parse_course(self, response):
        cl = CourseLoader(item=Course(), response=response)
        cl.add_xpath('code', '//h4', re='(\w{4}\s\w{3,4})')
        cl.add_xpath('name', '//h4', re='\w{4}\s\w{3,4}\s(.+)')
        cl.add_xpath('credits', 'body/div/div/p[2]', re='Credits:\s(\d+)')
        cl.add_xpath('prereqs', 'body/div/div/p[3]', re='(\w{4}\s\w{3,4})')
        cl.add_xpath('coreqs', 'body/div/div/p[3]', re='(\w{4}\s\w{3,4})')
        cl.add_xpath('activities', 'body/div/div/ul/li', re='(\d+)')
        sections = []
        for row in response.xpath('body/div/div/table/tr'):
            sl = SectionLoader(item=Section(), selector=row)
            sl.add_xpath('course', './td[2]/a/text()', re='(\w{4}\s\w{3,4})')
            sl.add_xpath('code', './td[2]/a/text()')
            sl.add_xpath('status', './td[1]')
            sl.add_xpath('activity', './td[3]')
            sl.add_xpath('term', './td[4]', re='(\d+)')
            sl.add_xpath('days', './td[6]', re='(\w{3})')
            sl.add_xpath('start', './td[7]')
            sl.add_xpath('end', './td[8]')
            s = sl.load_item()
            sections.append(s)
        c = cl.load_item()
        c['sections'] = sections
        yield c
