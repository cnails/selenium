import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"

try:
	driver = webdriver.Chrome(executable_path=r"/Users/cnails/Downloads/chromedriver")
	driver.get(link)
	time.sleep(0.2)
	texts = driver.find_elements_by_css_selector("[type=\"text\"]")
	[text.send_keys("answer") for text in texts]
	driver.find_element_by_css_selector(".btn").click()
finally:
	time.sleep(10)
	driver.quit()