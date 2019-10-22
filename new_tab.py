import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
driver.get("http://suninjuly.github.io/alert_accept.html")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[0])
time.sleep(10)
driver.quit()
