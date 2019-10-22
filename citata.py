import time
import random
from selenium import webdriver

link = "http://kquote.ru/quotes/pulp-fiction.html"

driver = webdriver.Chrome(executable_path=r'/Users/cnails/Downloads/chromedriver')
driver.get(link)
time.sleep(0.2)
elements = driver.find_elements_by_css_selector(".text_quote")
elem = random.choice(elements)
print(elem.get_attribute('innerHTML'))
driver.quit()