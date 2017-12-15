# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request

class AllawyersSpider(scrapy.Spider):
    name = 'allawyers'
    allowed_domains = ['www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['https://www.avvo.com/all-lawyers/ny/new_york.html']

    def parse(self, response):
	links = []
	print links
     for link in set(response.xpath('/html/body/div[1]/div/div/div[4]/div/div[2]/div/div/div[1]/ol/li/a/@href').extract()):
	 url = urlparse.urljoin(response.url, str(link))
     	 print url

    

    
