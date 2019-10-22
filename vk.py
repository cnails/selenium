import time
import random
import re
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wat
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request

def dwnpc(i = 0):
	driver.get(random.choice(groups))
	time.sleep(0.2)
	imgs = []
	photos = driver.find_elements_by_css_selector("div.wall_text  [onclick*='.userapi']")
	photos1 = [pht.get_attribute("style") for pht in photos]
	for photo in photos1:
		i = 0
		print(photo)
		src = ""
		while photo[i] != ')':
			if photo[i] == '(':
				i += 2
				if photo[i] == '\"':
					break
				while photo[i] != '\"':
					src += photo[i]
					i += 1
			i += 1
		imgs.append(src)
	img = random.choice(imgs)
	return (img)


driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
link2 = "http://kquote.ru/quotes/pulp-fiction.html"
driver.get(link2)
time.sleep(0.2)
groups = ["https://vk.com/wtf.rasha", "https://vk.com/dank_memes_ayylmao", "https://vk.com/ru9gag"]
elements = driver.find_elements_by_css_selector(".text_quote")
elem1 = [elen.get_attribute('innerHTML') for elen in elements]
elem2 = [re.sub('<br>', '\t', elen1) for elen1 in elem1]
elems = [re.sub('\n', '', elen2) for elen2 in elem2]
link = "https://vk.com/im"
time.sleep(0.2)
driver.get(link)
emailarea = driver.find_element_by_css_selector("#email.big_text")
emailarea.send_keys("89859064657")
passarea = driver.find_element_by_css_selector("#pass.big_text")
passarea.send_keys("Bongowert11")
loginarea = driver.find_element_by_css_selector("#login_button")
loginarea.click()
time.sleep(0.5)
img = dwnpc()
i = 1
time.sleep(0.3)
driver.get(link)
while (i != 0):
	try:
		messagetest = driver.find_element_by_css_selector(".nim-dialog_unread")
		if messagetest:
			messagetest.click()
			inputarea = driver.find_element_by_css_selector("input[type='file'][name='media']")
			# elem = random.choice(elems)
			logo = urllib.request.urlopen(img).read()
			f = open("mem.jpg", "wb")
			f.write(logo)
			time.sleep(0.5)
			inputarea.send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mem.jpg"))
				# inputarea.send_keys(img)
				# for ch in elem:
				# 	if ch == '\t':
				# 		inputarea.send_keys(Keys.COMMAND + Keys.ENTER)
				# 	else:
				# 		inputarea.send_keys(ch)
			time.sleep(0.1)
			driver.find_element_by_css_selector(".im-send-btn._im_send").click()
			nazad = driver.find_element_by_css_selector(".im-page--back-btn[href=\"/im?tab=all\"]").click()
			img = dwnpc()
			time.sleep(0.3)
			driver.get(link)
	except:
		time.sleep(1)
