import time
import math
from selenium import webdriver

driver = webdriver.Chrome("/Users/cnails/Downloads/chromedriver")
driver.get("http://suninjuly.github.io/get_attribute.html")
driver.find_element_by_css_selector("#answer").send_keys(str(math.log(abs(12*math.sin(int(driver.find_element_by_css_selector("#treasure").get_attribute("valuex")))))))
[driver.find_element_by_css_selector(sel).click() for sel in ["#robotCheckbox", "#robotsRule", ".btn"]]
time.sleep(5)
driver.quit()