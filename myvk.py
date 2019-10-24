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
import platform
import hashlib
from getpass import getpass

# def	readmes():

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1980")
link_effects = ["https://www.imgonline.com.ua/water-ripples.php", "https://www.imgonline.com.ua/mirror-reflections-from-halves-of-image.php", "https://www.imgonline.com.ua/sphere-effect-from-panorama.php", "https://www.imgonline.com.ua/droste-effect.php", "https://www.imgonline.com.ua/photo-recursion.php", "https://www.imgonline.com.ua/sketch-from-photo.php", "https://www.imgonline.com.ua/abstraction-from-strokes-and-dots.php", "https://www.imgonline.com.ua/dark-fairy-tale-picture.php", "https://www.imgonline.com.ua/mirror-collage.php", "https://www.imgonline.com.ua/oil-painting-strokes.php", "https://www.imgonline.com.ua/make-negative.php", "https://www.imgonline.com.ua/kaleidoscope-effect.php" , "https://www.imgonline.com.ua/hope-poster.php" , "https://www.imgonline.com.ua/fire-picture.php" , "https://www.imgonline.com.ua/tetris.php", "https://www.imgonline.com.ua/andy-warhol-effect.php", "https://www.imgonline.com.ua/mix-picture.php", "https://www.imgonline.com.ua/grid-square.php", "https://www.imgonline.com.ua/whirlpool-effect.php", "https://www.imgonline.com.ua/radial-waves.php", "https://www.imgonline.com.ua/triangular-pixelization.php", "https://www.imgonline.com.ua/picture-distortion.php"]
groups = ["https://vk.com/wtf.rasha", "https://vk.com/dank_memes_ayylmao", "https://vk.com/ru9gag", "https://vk.com/reddit", "https://vk.com/justputin2024"]
osplat = platform.system()
link_citata = "http://kquote.ru/quotes/pulp-fiction.html"
link = "https://vk.com/im"
driver = (webdriver.Chrome() if osplat == "Windows" else webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver")))

def citata():
	driver.get(link_citata)
	elements = driver.find_elements_by_css_selector(".text_quote")
	elem1 = [elen.get_attribute('innerHTML') for elen in elements]
	elem2 = [re.sub('<br>', '\t', elen1) for elen1 in elem1]
	elems = [re.sub('\n', '', elen2) for elen2 in elem2]
	elem = random.choice(elems)
	inputarea.send_keys(linkpht)
	inputarea.send_keys(img)
	for ch in elem:
		if ch == '\t':
			inputarea.send_keys(Keys.COMMAND + Keys.ENTER)
		else:
			inputarea.send_keys(ch)

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
	time.sleep(0.5)
	sels = driver.find_elements_by_class_name("im-mess--text")
	href = ""
	messages = [sel.text for sel in sels]
	if messages[-1] == "Бот, фото" or messages[-1] == "бот, фото" or messages[-1] == "бот фото" or messages[-1] == "Бот фото":
		print("debag")
		href = prettyphoto()
	if messages[-1] == "Бот, эффект" or messages[-1] == "бот, эффект" or messages[-1] == "бот эффект" or messages[-1] == "Бот эффект" or messages[-1] == "эффект" or messages[-1] == "Эффект":
		href = effphoto()
	if messages[-1] == "Бот, мем" or messages[-1] == "бот, мем" or messages[-1] == "бот мем" or messages[-1] == "Бот мем":
		href = dwnpc(groups) 
	if href == "":
		driver.get(link)
	return href

def effphoto():
	href = ""
	photos = driver.find_elements_by_css_selector("[onclick*='.userapi']")
	imgs = retsrc(photos)
	img = imgs[-1]
	logo = requests.get(img)
	with open("mem.jpg",'wb') as imgfile:
		imgfile.write(logo.content)
	time.sleep(0.5)
	link_ef = "http://editor.pho.to/ru/edit/"
	driver.get(link_ef)
	driver.find_element_by_css_selector("[type='file']").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mem.jpg"))
	time.sleep(0.7)
	driver.find_element_by_css_selector(".i-textures").click()
	textures = driver.find_elements_by_css_selector("#bokeh-accordion .panel")
	randimg = random.randint(1, 10)
	texture = textures[randimg]
	texture.click()
	time.sleep(0.5)
	driver.find_element_by_css_selector("[id='save-share']").click()
	time.sleep(0.5)
	driver.find_element_by_css_selector("[id='confirm-btn-apply']").click()
	time.sleep(0.5)
	driver.find_element_by_css_selector("[id='btn-share']").click()
	time.sleep(3)
	driver.switch_to.window(driver.window_handles[-1])
	time.sleep(3)
	linkpht = driver.find_element_by_css_selector("[src*='.jpeg']").get_attribute("src")
	response=requests.get(linkpht)
	with open("mem.jpg","wb") as imgfile:
		imgfile.write(response.content)
	return linkpht

def	prettyphoto():
	href = ""
	photos = driver.find_elements_by_css_selector("[onclick*='.userapi']")
	imgs = retsrc(photos)
	img = imgs[-1]
	logo = requests.get(img)
	with open("mem.jpg",'wb') as imgfile:
		imgfile.write(logo.content)
	time.sleep(0.5)
	link_ef = random.choice(link_effects)
	driver.get(link_ef)
	time.sleep(1)
	driver.find_element_by_css_selector("[type='file']").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mem.jpg"))
	time.sleep(0.7)
	driver.find_element_by_css_selector("[type='submit']").click()
	time.sleep(2)
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
	response = requests.get(img)
	with open("mem.jpg", "wb") as imgfile:
	    imgfile.write(response.content)
	return (img)

def authorizate():
	driver.get(link)
	emailarea = driver.find_element_by_css_selector("#email.big_text")
	emailarea.send_keys("79996237427")
	passarea = driver.find_element_by_css_selector("#pass.big_text")
	with open(os.path.join(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0], ".pswd")) as fd:
		passarea.send_keys(fd.read())
	passarea.send_keys("\n")
	driver.get(link)
	time.sleep(1000)
	return (True)

def waitmsg():
	while (1):
		try:
			messagetest = driver.find_element_by_css_selector(".nim-dialog_unread")
			if messagetest:
				messagetest.click()
				linkpht = readwrds()
				if linkpht == "":
					time.sleep(15)
					driver.quit()
				if linkpht:
					driver.get(link)
					messagetest = driver.find_element_by_css_selector(".nim-dialog")
					messagetest.click()
					inputarea = driver.find_element_by_css_selector("input[type='file'][name='media']")
					inputarea.send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mem.jpg"))
					while driver.find_element_by_css_selector(".im-send-btn._im_send").get_attribute("aria-label") != "Отправить":
						time.sleep(0.7)
					driver.find_element_by_css_selector(".im-send-btn._im_send").click()
				driver.get(link)
		except Exception as e:
			print(e)
		except:
			time.sleep(1)

if __name__ == "__main__":
	assert hashlib.md5(str(getpass("pass >> ")).encode('utf-8')).hexdigest() == "098f6bcd4621d373cade4e832627b4f6", "Incorrect password"
	print("\033[A                             \033[A")
	assert authorizate() == True, "Something wrong"
	waitmsg()
	
