import time
import math
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html?ruler=people"

# try:
driver = webdriver.Chrome("/Users/cnails/Downloads/chromedriver")
driver.get(link)
driver.find_element_by_css_selector("#answer").send_keys(calc(driver.find_element_by_css_selector("#input_value").text))
driver.find_element_by_css_selector("#robotCheckbox").click()
driver.find_element_by_css_selector("#robotsRule").click()
driver.find_element_by_css_selector(".btn").click()
# finally:
time.sleep(5)
driver.quit()
