import time
import random
import re
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wat
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests

# def	readmes():

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1980")
link_effects = ["https://www.imgonline.com.ua/water-ripples.php", "https://www.imgonline.com.ua/mirror-reflections-from-halves-of-image.php", "https://www.imgonline.com.ua/sphere-effect-from-panorama.php", "https://www.imgonline.com.ua/droste-effect.php", "https://www.imgonline.com.ua/photo-recursion.php", "https://www.imgonline.com.ua/sketch-from-photo.php", "https://www.imgonline.com.ua/abstraction-from-strokes-and-dots.php", "https://www.imgonline.com.ua/dark-fairy-tale-picture.php", "https://www.imgonline.com.ua/mirror-collage.php", "https://www.imgonline.com.ua/oil-painting-strokes.php", "https://www.imgonline.com.ua/make-negative.php", "https://www.imgonline.com.ua/kaleidoscope-effect.php" , "https://www.imgonline.com.ua/hope-poster.php" , "https://www.imgonline.com.ua/fire-picture.php" , "https://www.imgonline.com.ua/tetris.php", "https://www.imgonline.com.ua/andy-warhol-effect.php", "https://www.imgonline.com.ua/mix-picture.php", "https://www.imgonline.com.ua/grid-square.php", "https://www.imgonline.com.ua/whirlpool-effect.php", "https://www.imgonline.com.ua/radial-waves.php", "https://www.imgonline.com.ua/triangular-pixelization.php", "https://www.imgonline.com.ua/picture-distortion.php"]

def retsrc(photos):
	imgs = []
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
	return (imgs)

def readwrds():
	sels = driver.find_elements_by_class_name("im-mess--text")
	href = ""
	messages = [sel.text for sel in sels]
	if messages[-1] == "Бот, фото" or messages[-1] == "бот, фото" or messages[-1] == "бот фото" or messages[-1] == "Бот фото":
		href = prettyphoto()
	if messages[-1] == "Бот, эффект" or messages[-1] == "бот, эффект" or messages[-1] == "бот эффект" or messages[-1] == "Бот эффект" or messages[-1] == "эффект" or messages[-1] == "Эффект":
		href = effphoto()
	if href == "":
		driver.get(link)
	return href

def effphoto():
	href = ""
	photos = driver.find_elements_by_css_selector("[onclick*='.userapi']")
	imgs = retsrc(photos)
	img = imgs[-1]
	logo = requests.get(img)
	if logo.status_code==200:
		with open("mem.jpg",'wb') as imgfile:
			imgfile.write(logo.content)
	time.sleep(0.5)
	# link_ef = random.choice(link_effects)
	link_ef = "http://editor.pho.to/ru/edit/"
	driver.get(link_ef)
	# time.sleep(1)
	driver.find_element_by_css_selector("[type='file']").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mem.jpg"))
	time.sleep(0.7)
	driver.find_element_by_css_selector(".i-textures").click()
	textures = driver.find_elements_by_css_selector("#bokeh-accordion .panel")
	randimg = random.randint(1, 10)
	texture = textures[randimg]
	time.sleep(0.5)
	print(texture)
	texture.click()
	print("text")
	time.sleep(2)
	# driver.find_element_by_css_selector("[id=bokeh_" + str(randimg) + "-settings] span.btn").click()
	print("debag")
	# time.sleep(0.5)
	driver.find_element_by_css_selector("[id='save-share']").click()
	time.sleep(0.5)
	driver.find_element_by_css_selector("[id='confirm-btn-apply']").click()
	time.sleep(0.5)
	driver.find_element_by_css_selector("[id='btn-share']").click()
	time.sleep(3)
	driver.switch_to.window(driver.window_handles[-1])
	time.sleep(3)
		# print(driver.find_element_by_css_selector(".story-image [src]").get_attribute("src"))
	linkpht = driver.find_element_by_css_selector("[src*='.jpeg']").get_attribute("src")
	print(linkpht)
		# href = driver.find_element_by_css_selector("[href*='.jpg']").get_attribute("href")
	response=requests.get(linkpht)
	if response.status_code==200:
		print("hello")
		with open("mem.jpg","wb") as imgfile:
			imgfile.write(response.content)
	return linkpht

def	prettyphoto():
	href = ""
	photos = driver.find_elements_by_css_selector("[onclick*='.userapi']")
	imgs = retsrc(photos)
	img = imgs[-1]
	logo = requests.get(img)
	if logo.status_code==200:
		with open("mem.jpg",'wb') as imgfile:
			imgfile.write(logo.content)
	time.sleep(0.5)
	link_ef = random.choice(link_effects)
	driver.get(link_ef)
	time.sleep(1)
	driver.find_element_by_css_selector("[type='file']").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mem.jpg"))
	time.sleep(0.7)
	driver.find_element_by_css_selector("[type='submit']").click()
		# textures = driver.find_elements_by_css_selector("#bokeh-accordion .panel")
		# randimg = random.randint(1, 12)
		# texture = textures[randimg]
		# texture.click()
		# time.sleep(0.5)
		# texturebutton = driver.find_element_by_css_selector("[id=bokeh_" + str(randimg) + "-settings] span.btn")
		# texture.click()
		# driver.find_element_by_css_selector("[id='save-share']").click()
		# time.sleep(0.5)
		# driver.find_element_by_css_selector("[id='confirm-btn-apply']").click()
		# time.sleep(0.5)
		# driver.find_element_by_css_selector("[id='btn-share']").click()
		# time.sleep(3)
		# driver.switch_to.window(driver.window_handles[1])
	time.sleep(2)
		# print(driver.find_element_by_css_selector(".story-image [src]").get_attribute("src"))
		# linkpht = driver.find_element_by_css_selector("[href*='.jpg']").get_attribute("href")
	href = driver.find_element_by_css_selector("[href*='.jpg']").get_attribute("href")
	response=requests.get(href)
	if response.status_code==200:
		with open("mem.jpg",'wb') as imgfile:
			imgfile.write(response.content)
	return href


def dwnpc(groups):
	driver.get(random.choice(groups))
	imgs = []
	photos = driver.find_elements_by_css_selector("div.wall_text [onclick*='.userapi']")
	photos1 = [pht.get_attribute("style") for pht in photos]
	for photo in photos1:
		i = 0
		# print(photo)
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

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"), options=chrome_options)
driver.implicitly_wait(0.3)
link2 = "http://kquote.ru/quotes/pulp-fiction.html"
driver.get(link2)
time.sleep(0.2)
groups = ["https://vk.com/wtf.rasha", "https://vk.com/dank_memes_ayylmao", "https://vk.com/ru9gag", "https://vk.com/reddit", "https://vk.com/justputin2024"]
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
time.sleep(0.2)
driver.get(link)
while (1):
	try:
		# driver.get(link)
		messagetest = driver.find_element_by_css_selector(".nim-dialog_unread")
		if messagetest:
			messagetest.click()
			# inputarea = driver.find_element_by_css_selector("input[type='file'][name='media']")
			# # elem = random.choice(elems)
			linkpht = readwrds()
			print(linkpht)
			if linkpht:
				driver.get(link)
				messagetest = driver.find_element_by_css_selector(".nim-dialog")
				messagetest.click()
				inputarea = driver.find_element_by_css_selector("input[type='file'][name='media']")
			# logo = urllib.request.urlopen(img).read()
			# f = open("mem.jpg", "wb")
			# f.write(logo)
			# driver.get(link)
				inputarea.send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mem.jpg"))
				# inputarea.send_keys(linkpht)
				# inputarea.send_keys(img)
				# for ch in elem:
				# 	if ch == '\t':
				# 		inputarea.send_keys(Keys.COMMAND + Keys.ENTER)
				# 	else:
				# 		inputarea.send_keys(ch)
				while driver.find_element_by_css_selector(".im-send-btn._im_send").get_attribute("aria-label") != "Отправить":
					time.sleep(0.7)
				driver.find_element_by_css_selector(".im-send-btn._im_send").click()
			# nazad = driver.find_element_by_css_selector(".im-page--back-btn[href=\"/im?tab=all\"]").click()
			# img = dwnpc(groups)
			driver.get(link)
	except Exception as e:
		print(e)
	except:
		time.sleep(1)
