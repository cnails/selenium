import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wat
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from math import log, sin

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
driver.get("http://suninjuly.github.io/explicit_wait2.html")
i = wat(driver, 100).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
driver.find_element_by_id("book").click()
driver.find_element_by_css_selector("#answer").send_keys(str(log(abs((12 * sin(int(driver.find_element_by_css_selector("#input_value").text)))))))
driver.find_element_by_id("solve").click()
time.sleep(10)
driver.quit()
