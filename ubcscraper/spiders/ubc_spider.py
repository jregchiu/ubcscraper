import scrapy
from ubcscraper.loaders import SectionLoader
from ubcscraper.items import Section

class UBCSpider(scrapy.Spider):
    name = 'UBC'
    filters = ('Unreleased', 'Cancelled', 'STT', 'Waiting List')

    def start_requests(self):
        yield scrapy.Request('https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=0&sessyr={0}&sesscd={1}'.format(self.year, self.session.upper()), self.parse)

    def parse(self, response):
        for row in response.xpath('body/div/div/table//a'):
            if row.xpath('./text()').extract()[0] in self.to_scrape:
                href = row.xpath('./@href')[0]
                yield response.follow(href, self.parse_department)

    def parse_department(self, response):
        for href in response.xpath('body/div/div/table//@href'):
            yield response.follow(href, self.parse_course)

    def parse_course(self, response):
        for row in response.xpath('body/div/div/table/tr'):
            if any(f in self.filters for f in [str.strip(s) for s in row.xpath('./td[1]/text()|./td[3]/text()').extract()]) or '' in [str.strip(s) for s in row.xpath('./td[6]/text()|./td[7]/text()|./td[8]/text()').extract()] or not row.xpath('./td[2]/a/@href'):
                continue
            href = row.xpath('./td[2]/a/@href')[0]
            yield response.follow(href, self.parse_section)

    def parse_section(self, response):
        td = response.xpath('body/div/div/table[2]//td')
        for i in range(len(td) // 6):
            sl = SectionLoader(item=Section(), response=response)
            sl.add_xpath('course', 'body/div/div/h4', re='(\w{4}\s\w{3,4})')
            sl.add_value('year', self.year)
            sl.add_value('session', self.session.upper())
            sl.add_xpath('code', 'body/div/div/h4', re='(\w{4}\s\w{3,4}\s\w{3,4})')
            sl.add_xpath('activity', 'body/div/div/h4', re='\((.+)\)')
            sl.add_value('term', td[0 + 6 * i].re(r'(\d+)'))
            sl.add_value('days', td[1 + 6 * i].re(r'(\w{3})'))
            sl.add_value('start', td[2 + 6 * i].extract())
            sl.add_value('end', td[3 + 6 * i].extract())
            yield sl.load_item()
