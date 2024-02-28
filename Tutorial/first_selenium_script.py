from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

print('This is my First Selenium Script')

obj_service = Service()
obj_options = Options()
obj_options.add_experimental_option('detach', True)
obj_driver = webdriver.Chrome(options=obj_options, service=obj_service)
obj_driver.get(r'https://google.com/')
# print(obj_driver.title)
# obj_driver.close()
