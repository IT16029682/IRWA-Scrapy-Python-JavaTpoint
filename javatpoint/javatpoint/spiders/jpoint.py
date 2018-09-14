# -*- coding: utf-8 -*-
import scrapy
from ..items import CodeItem

class JpointSpider(scrapy.Spider):
    name = 'jpoint'
    allowed_domains = ['www.javatpoint.com']
    start_urls = ['https://www.javatpoint.com/operators-in-java']

    def parse(self, response):
       # tk=response.css('.codeblock')
       # dess=response.css('p::text').extract()
        #titlelist=dict()
        title=response.css('#h1::text,.h1 ::text')[0].extract()
        language=response.xpath('//*[@id="smoothmenu1"]/ul/li[5]/a/text()').extract_first()
        subtitles=response.xpath('//h2[not(contains(.,"Javatpoint Services") or contains(.,"Training For College Campus") or contains(.,"Please Share") or contains(.,"Learn Latest Tutorials"))]/text()').extract()
        count = 1
        for t in subtitles:
            #code = t.css('.java::text').extract_first()
            description = response.xpath('//p[count(preceding-sibling::h2)=' + str(count) + ']/text()').extract()
          
            #print(code)
            Item=CodeItem()
            Item['Title']=title
            Item['subtitle']=t
            Item['Code']= response.xpath('//div[count(preceding-sibling::h2)=' + str(count) + ']/textarea[@class="java"]/text()').extract() 
            Item['Language']=language
            Item['Description']=description
            Item['URL']= response.request.url
            count+=1
            yield Item
        
        NextLinkSelector= response.xpath('//*[@id="bottomnextup"]/a[1]/@href')
        if NextLinkSelector:
           NextLink=NextLinkSelector.extract_first()
           yield scrapy.Request(url=response.urljoin(NextLink))    


