import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
driver.get("http://suninjuly.github.io/alert_accept.html")
time.sleep(2)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
while (1):
	driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[1])

# driver.switch_to.window("htttps://google.com")
# driver.switch_to.window("htttps://google.com")
# driver.switch_to.window("htttps://google.com")
# driver.switch_to.window("htttps://google.com")
# driver.switch_to.window("htttps://google.com")
time.sleep(10)
driver.quit()
