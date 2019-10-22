import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"

try:
	driver = webdriver.Chrome(executable_path=r'/Users/cnails/Downloads/chromedriver')
	driver.get(link)
	time.sleep(0.2)
	driver.find_element_by_css_selector(".first_block .first").send_keys("Andrey")
	driver.find_element_by_css_selector(".first_block .second").send_keys("Andreev")
	driver.find_element_by_css_selector(".first_block .third").send_keys("Andreevandrey")
	driver.find_element_by_css_selector(".second_block .first").send_keys("88005553535")
	driver.find_element_by_css_selector(".second_block .second").send_keys("Moscow")
	driver.find_element_by_css_selector(".btn").click()
	text = driver.find_element_by_tag_name("h1").get_attribute('innerHTML') #получаем текст
	assert "Congratulations! You have successfully registered!" == text
finally:
	time.sleep(5)
	driver.quit()
