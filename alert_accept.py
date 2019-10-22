import time
import os
from math import sin, log
from selenium import webdriver

def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

driver = webdriver.Chrome(os.path.join(os.path.abspath(os.path.dirname(__file__)), "chromedriver"))
driver.get("http://suninjuly.github.io/alert_accept.html")
driver.find_element_by_class_name("btn").click()
driver.switch_to.alert.accept()
driver.find_element_by_css_selector("#answer").send_keys(str(log(abs((12 * sin(int(driver.find_element_by_css_selector("#input_value").text)))))))
driver.find_element_by_class_name("btn").click()
answer = str(get_num(driver.switch_to.alert.text))
driver.switch_to.alert.accept()
driver.get("https://stepik.org/catalog?auth=login&language=en")
time.sleep(2)
driver.find_element_by_css_selector("[title='Sign in with Google']").click()
time.sleep(0.2)
driver.find_element_by_css_selector("[type='email']").send_keys("andreyandreevgr@gmail.com")
driver.find_element_by_id("identifierNext").click()
input()
driver.get("https://stepik.org/lesson/184253/step/4?unit=158843")
time.sleep(5)
driver.find_element_by_class_name("textarea").send_keys(answer)
time.sleep(0.1)
driver.find_element_by_class_name("submit-submission").click()
time.sleep(5)
print("EZ")
driver.quit()
