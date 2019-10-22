import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("/Users/cnails/Downloads/chromedriver")
driver.get("http://suninjuly.github.io/selects1.html")
time.sleep(0.2)
x = int(driver.find_element_by_css_selector("#num1").text)
y = int(driver.find_element_by_css_selector("#num2").text)
sum = str(x + y)
select = Select(driver.find_element_by_id("dropdown"))
select.select_by_visible_text(sum)
driver.find_element_by_css_selector(".btn").click()
time.sleep(5)
driver.quit()