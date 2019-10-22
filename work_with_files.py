# import os
# from selenium import webdriver
# import time

# driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
# driver.get("http://suninjuly.github.io/file_input.html")
# [elem.send_keys("Test") for elem in driver.find_elements_by_css_selector("[type='text']")]
# driver.find_element_by_name("file").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.txt"))
# driver.find_element_by_class_name("btn").click()
# time.sleep(5)
# driver.quit()

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver")
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)  
driver.get("https://www.google.com")
driver.get_screenshot_as_file("capture.png")
time.sleep(10)
driver.close()
