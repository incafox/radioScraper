
from selenium import webdriver

start_urls = 'http://www.radiosdelperu.pe/radio-sicuani'

driver = webdriver.Firefox()
driver.get(start_urls)
driver.implicitly_wait(30)

tr = driver.page_source 
tr = str(tr)
fil = open('tmr.txt','w')
fil.write(tr)
#lol = driver.find_element_by_css_selector('audio')
print (lol)
#next = driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

'''
            try:
                next.click()

                # get the data and write it to scrapy items
            except:
                break

        self.driver.close()


'''