import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'/Users/cnails/Downloads/chromedriver')

try:
	driver.get("http://suninjuly.github.io/simple_form_find_task.html")
	time.sleep(0.2)
	driver.find_element_by_css_selector("[name=\"first_name\"]").send_keys("Andrey")
	driver.find_element_by_css_selector("[name=\"last_name\"]").send_keys("Andreev")
	driver.find_element_by_css_selector(".city").send_keys("Moscow")
	driver.find_element_by_css_selector("#country").send_keys("Russia")
	driver.find_element_by_css_selector(".btn").click()
finally:
	time.sleep(10)
	#driver.quit()