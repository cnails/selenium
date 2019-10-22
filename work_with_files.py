import os
from selenium import webdriver
import time

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
driver.get("https://google.com")
time.sleep(5)
driver.quit()
