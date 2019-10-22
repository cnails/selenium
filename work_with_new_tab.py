import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from math import log, sin

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
driver.get("http://suninjuly.github.io/redirect_accept.html")
driver.find_element_by_class_name("btn").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_css_selector("#answer").send_keys(str(log(abs((12 * sin(int(driver.find_element_by_css_selector("#input_value").text)))))))
driver.find_element_by_class_name("btn").click()
time.sleep(10)
driver.quit()