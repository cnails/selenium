import time
import math
from selenium import webdriver

def type_info():
	time.sleep(0.2)
	driver.find_element_by_css_selector("[name=\"first_name\"]").send_keys("Andrey")
	driver.find_element_by_css_selector("[name=\"last_name\"]").send_keys("Andreev")
	driver.find_element_by_css_selector(".city").send_keys("Moscow")
	driver.find_element_by_css_selector("#country").send_keys("Russia")
	driver.find_element_by_css_selector(".btn").click()

link = "http://suninjuly.github.io/find_link_text"
href = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
	driver = webdriver.Chrome(executable_path=r'/Users/cnails/Downloads/chromedriver')
	driver.get(link)
	time.sleep(0.2)
	driver.find_element_by_link_text(href).click()
	type_info()
finally:
	time.sleep(10)
	driver.quit()
