import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver")
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)  
driver.get("https://www.google.com")
driver.get_screenshot_as_file("capture.png")
time.sleep(10)
driver.close()
