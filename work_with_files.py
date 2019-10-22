import os
from selenium import webdriver
import time

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
driver.get("http://suninjuly.github.io/file_input.html")
[elem.send_keys("Test") for elem in driver.find_elements_by_css_selector("[type='text']")]
driver.find_element_by_name("file").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.txt"))
driver.find_element_by_class_name("btn").click()
time.sleep(5)
driver.quit()
