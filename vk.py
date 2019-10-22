import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'/Users/cnails/Downloads/chromedriver')
link2 = "http://kquote.ru/quotes/pulp-fiction.html"
driver.get(link2)
time.sleep(0.2)
elements = driver.find_elements_by_css_selector(".text_quote")
elem1 = [elen.get_attribute('innerHTML') for elen in elements]
elem2 = [re.sub('<br>', '\t', elen1) for elen1 in elem1]
elems = [re.sub('\n', '', elen2) for elen2 in elem2]
link = "https://vk.com/im"
driver.get(link)
emailarea = driver.find_element_by_css_selector("#email.big_text")
emailarea.send_keys("89859064657")
passarea = driver.find_element_by_css_selector("#pass.big_text")
passarea.send_keys("Bongowert11")
loginarea = driver.find_element_by_css_selector("#login_button")
loginarea.click()
time.sleep(0.5)
i = 1
while (i != 0):
	try:
		messagetest = driver.find_element_by_css_selector(".nim-dialog_unread")
		if messagetest:
			messagetest.click()
			inputarea = driver.find_element_by_css_selector(".im_editable")
			elem = random.choice(elems)
			for ch in elem:
				if ch == '\t':
					inputarea.send_keys(Keys.COMMAND + Keys.ENTER)
				else:
					inputarea.send_keys(ch)
			inputarea.send_keys("\n")
			nazad = driver.find_element_by_css_selector(".im-page--back-btn[href=\"/im?tab=all\"]").click()
			time.sleep(0.1)
	except:
		time.sleep(1)
