# -*- coding: utf-8 -*-
import scrapy


class GdpDeptSpider(scrapy.Spider):
    name = 'gdp_dept'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries=response.xpath("//table/tbody/tr")
        for country in countries:
            yield {
                'country_name': country.xpath('.//td[1]/a/text()').get(),
                'gdp': country.xpath('.//td[2]/text()').get()
            }
            
            

            