import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("http://www.baidu.com")
assert '百度' in browser.title

elem = browser.find_element_by_id('kw')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
time.sleep(30)
browser.quit()