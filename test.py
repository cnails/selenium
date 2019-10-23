import time
from selenium import webdriver
# import urllib.request
import requests


url = "https://www.imgonline.com.ua/result_img/imgonline-com-ua-FRACTAL-6qNVU6gyMqx5.jpg"
driver = webdriver.Chrome("/Users/cnails/Downloads/chromedriver")
driver.get("https://google.com")
# logo = urllib.request.urlopen(link).read()
# logo = requests.get(link)
# print(logo)
# with open("mem.jpg", "wb") as fd:
#     for chunk in logo.iter_content:
#         print(chunk)
response=requests.get(url)
if response.status_code==200:
  with open("mem.jpg",'wb') as imgfile:
    imgfile.write(response.content)
# f.write(logo)
time.sleep(12)
driver.quit()
