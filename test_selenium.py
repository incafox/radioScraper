import scrapy
from selenium import webdriver

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ['ebay.com']
    start_urls = ['http://www.radiosdelperu.pe/radio-sicuani']

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(30)

        while True:
            self.driver.implicitly_wait(30)
            lol = self.driver.find_element_by_css_selector('mediaelementwrapper')
            print ('mierdaaaaaaaaaaaaaaaaaaa')
            print (lol)
            self.driver.implicitly_wait(30)
            print ('start ---------------')
            print (response.css('audio').extract())
            print ('end -----------------')
            #next = self.driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

            #try:
             #   next.click()

                # get the data and write it to scrapy items
            #except:
             #   break

        self.driver.close()
