# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.spiders import Spider
from scrapy.http import Request


class AllawyersSpider(scrapy.Spider):
    name = 'allawyers'
    allowed_domains = ['www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['https://www.avvo.com/all-lawyers/ny/new_york.html']

    def parse(self, response):
     link = []
     for link in set(response.xpath('/html/body/div[1]/div/div/div[4]/div/div[2]/div/div/div[1]/ol/li/a/@href').extract()):
	 links = urlparse.urljoin(response.url, str(link))
         yield scrapy.Request(links,callback=self.parse_following_urls,dont_filter=True)

    def parse_following_urls(self, response):
     url = []
     for url in set(response.xpath('/html/body/div[1]/div/div/div[5]/div[2]/section/div[2]/div[5]/ul/li/div/div/div/div[1]/div[2]/a/@href').extract()):
 	 urls = urlparse.urljoin(response.url, str(url))
	 yield scrapy.Request(urls,callback=self.parse_following_urls1,dont_filter=True)

    def parse_following_urls1(self, response):
         name =  response.xpath('//span[@itemprop="name"]/text()').extract_first()
         #print name
	 license = response.xpath('//ul[@class="icon-list"]//text()')[3].extract()
	 #print license
	 image =  response.xpath('//img/@src').extract_first()
	 #print image
	 avvo_rating = response.xpath('//span[@itemprop="ratingValue"]/text()').extract()
	 #print avvo_rating
	 client_rating = response.xpath('//div[@itemprop="aggregateRating"]//text()').extract()
	 #print client_rating
	 practise_areas = response.xpath('//*[@id="practice_areas"]/div/div[2]/ol/li/a/text()').extract()
	 #print practise_areas
	 payment_type = response.xpath('//*[@id="payments"]/div/div/div/div/div/div[2]/p/small/text()').extract()
	 #print payment_type
	 address = response.xpath('//span[@itemprop="address"]//text()')[:8].extract()
	 #print address
	 phone =  response.xpath('//span[@itemprop="address"]//text()')[8:14].extract()
	 #print phone
	 #Give the extracted content row wise
	 output = {
		   	"Name":name,
		   	"License":license,
	           	"Image":image,
	           	"Avvo rating" :avvo_rating,
	           	"Client rating" :client_rating,
	           	"Practise areas" :practise_areas,
	           	"Payment type" :payment_type,
	           	"Address" :address,
	           	"Phone" :phone 
	    	}
         yield output   
 	     

    
