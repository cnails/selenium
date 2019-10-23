import time
import unittest
import os
from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def	check(link):
	driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
	driver.get(link)
	driver.find_element_by_css_selector(".first_block .first").send_keys("Andrey")
	driver.find_element_by_css_selector(".first_block .second").send_keys("Andreev")
	driver.find_element_by_css_selector(".first_block .third").send_keys("Andreevandrey")
	driver.find_element_by_css_selector(".second_block .first").send_keys("88005553535")
	driver.find_element_by_css_selector(".second_block .second").send_keys("Moscow")
	driver.find_element_by_css_selector(".btn").click()
	text = driver.find_element_by_tag_name("h1").get_attribute('innerHTML')
	driver.quit()
	return text

class mytest(unittest.TestCase):
	def test_simple(self):
		assert "Congratulations! You have successfully registered!" == check(link), f"problem with {link}"
		assert "Congratulations! You have successfully registered!" == check(link2), f"problem with {link2}" 

if __name__ == "__main__":
	unittest.main()
