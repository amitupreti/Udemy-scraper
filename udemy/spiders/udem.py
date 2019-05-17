# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import scrapy_proxies



count=0
visited=[]
current=''
class UdemySpider(scrapy.Spider):
    name = 'udem'
    rotate_user_agent = True

    allowed_domains = ['drizly.com']
    start_urls = ['https://drizly.com/beer/c2','https://drizly.com/wine/c3','https://drizly.com/liquor/c4']

    def parse(self, response):
        global visited
        # global current
        # current = response.url

        
        links  = response.xpath('//*[@class="CatalogResults__CatalogListItem___2qCwP"]//a/@href').extract()
        links = list(set(links))

        next_page = response.xpath('//*[@class="Pagination__Pagination__chevron__right___2LaS5"]/@href').extract_first()


        for link in links:
            # print('\n\nVisiting next page:',link)
            # print(response.url)
            yield SplashRequest('https://drizly.com'+link, callback=self.parse_article, dont_filter=True)
        
        # next_page='https://www.templecellars.com'+str(next_page)
        print('\n\nNext Page: ',next_page)

        if next_page not in visited and next_page is not None:
            print('Visiting next page:',next_page)
            yield scrapy.Request(next_page, dont_filter=True)

            visited.append(next_page)


    def parse_article(self,response):
        product_name = response.xpath('//h1/text()').extract_first()
        product_brand= response.xpath('//*[@class="product-vendor vendor"]/text()').extract_first()


    
        product_price =  response.xpath('//*[@class="product-meta-info"]/span/text()').extract_first()




        # if product_price is None:
        #     product_price = response.xpath('//*[@class="product-price-minimum money"]/text()').extract_first()


        # product_price = str(product_price.replace('\n','').strip())
        product_image = response.xpath('//*[@class="ProductMeta__product-image"]//img//@src').extract_first()

  


        prodcut_description =  response.xpath('//*[@class="Product__section ProductDescription"]//div[@class="TextWidget__TextWidget___2tHNI"]//text()').extract() + response.xpath('//*[@class="Product__section ProductDescription"]//p//text()').extract()



        prodcut_description = ''.join(prodcut_description)


        try:
            category1   = response.xpath('/html/body/nav/ol/li[1]/a/span/text()').extract_first()
        except:
            category1=''
        
        try:
            category2  = response.xpath('/html/body/nav/ol/li[2]/a/span/text()').extract_first()
        except:
            category2=''

        try:
            category3   = response.xpath('/html/body/nav/ol/li[3]/a/span/text()').extract_first()
        except:
            category3=''
        try:    
            category4   = response.xpath('/html/body/nav/ol/li[4]/a/span/text()').extract_first()
        except:
            category4=''
        # category5   = response.xpath('/html/body/nav/ol/li[1]/a/span/text()').extract_first()
        cat1=''
        region1=''
        abv1=''
        tasting_notes1=''
        food_pairing1=''
        sugggested_glassware1=''
        
        try:
            cat = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][1]//text()').extract()[1:]
            cat1 = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][1]//text()').extract_first()
        except:
            cat=[]

        try:
            region = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][2]//text()').extract()[1:]
            region1 = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][2]//text()').extract_first()
        except:
            region=[]
            
        try:
            abv = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][3]//text()').extract()[1:]
            abv1 = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][3]//text()').extract_first()
        except:
            abv=[]


        try:
            tasting_notes = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][4]//text()').extract()[1:]
            tasting_notes1 = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][4]//text()').extract_first()

        except:
            tasting_notes=[]

        try:
            food_pairing = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][5]//text()').extract()[1:]
            food_pairing1 = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][5]//text()').extract_first()

        except:
            food_pairing=[]

        try:
            sugggested_glassware = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][6]//text()').extract()[1:]
            sugggested_glassware1 = response.xpath('//*[@class="PDPAttributesAndReviews__rowWrapper___2ejXN "]/div[@class="PDPAttributesAndReviews__row___3T_tv"][6]//text()').extract_first()

        except:
            sugggested_glassware=[]


        expert= response.xpath('//*[@class="ProductScrivitoContent__ProductScrivitoContent___2BFAe"]//text()').extract()
        expert = (' '.join(expert)).strip().replace('\n','')
        expert_notes = expert.split('About The Brand')[0]
        expert_notes=  expert_notes.replace('Drizly Expert Notes','')
        try:
            about_the_brand = expert.split('About The Brand')[1]
        except:
            about_the_brand=''        
        # category = response.xpath('//*[@id="ProductSection"]/nav/a[2]/text()').extract_first()
   

        global count
        count+=1

        yield{
            
            'category1':category1,
            'category2':category2,
            'category3':category3,
            'category4':category4,
            'Product_url':response.url,
            'Name':product_name,
            'Price':product_price,
            'Image':product_image,
            'Description_raw':prodcut_description.strip(),
            'expert notes':expert_notes,
            'about the brand':about_the_brand,
            'cat':''.join(cat),
            'region':''.join(region),
            'abv':''.join(abv),
            'tasting_notes':''.join(tasting_notes),
            'food_pairing':''.join(food_pairing),
            'sugggested_glassware':''.join(sugggested_glassware)
   

            }
        print("total: ",count)
        print('\n\n\n\n\n\n\n')
