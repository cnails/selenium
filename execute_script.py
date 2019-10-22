from selenium import webdriver
from math import sin, log
import time

driver = webdriver.Chrome("/Users/cnails/Downloads/chromedriver")
link = "https://SunInJuly.github.io/execute_script.html"
driver.get(link)
time.sleep(0.2)
driver.find_element_by_css_selector("#answer").send_keys(str(log(abs((12 * sin(int(driver.find_element_by_css_selector("#input_value").text)))))))
button = driver.find_element_by_tag_name("button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
[driver.find_element_by_id(sel).click() for sel in ["robotCheckbox", "robotsRule"]]
button.click()
time.sleep(5)
driver.quit()
