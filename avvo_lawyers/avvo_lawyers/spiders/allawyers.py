# -*- coding: utf-8 -*-
import scrapy


class AllawyersSpider(scrapy.Spider):
    name = 'allawyers'
    allowed_domains = ['www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['https://www.avvo.com/attorneys/10601-ny-andrew-proto-964289.html']

    def parse(self, response):
        name =  response.xpath('//span[@itemprop="name"]/text()').extract_first()
	print name
	license = response.xpath('//ul[@class="icon-list"]//text()')[3].extract()
	print license
	image =  response.xpath('//img/@src').extract_first()
	print image
	avvo_rating = response.xpath('//span[@itemprop="ratingValue"]/text()').extract()
	print avvo_rating
	client_rating = response.xpath('//div[@itemprop="aggregateRating"]//text()').extract()
	print client_rating
	practise_areas = response.xpath('//*[@id="practice_areas"]/div/div[2]/ol/li/a/text()').extract()
	print practise_areas
	payment_type = response.xpath('//*[@id="payments"]/div/div/div/div/div/div[2]/p/small/text()').extract()
	print payment_type
	address = response.xpath('//span[@itemprop="address"]//text()')[:8].extract()
	print address
	phone =  response.xpath('//span[@itemprop="address"]//text()')[8:14].extract()
	print phone

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

