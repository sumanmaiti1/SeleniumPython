import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

obj_option, obj_service = Options(), Service()
obj_option.add_argument('--start-maximized')
obj_option.add_experimental_option('detach', True)
obj_option.add_experimental_option('excludeSwitches', ['enable-automation'])
prefs = {'user_experience_metrics': {'personalization_data_consent_enabled': True}}
obj_option.add_experimental_option('prefs', prefs)

obj_driver = webdriver.Edge(options=obj_option, service=obj_service)
obj_driver.get(r'https://www.tutorialspoint.com/selenium/practice/check-box.php')

time.sleep(2)
print(obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 1']/preceding-sibling::input").is_selected())
if not obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 1']/preceding-sibling::input").is_selected():
    obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 1']/preceding-sibling::input").click()
    print(obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 1']/preceding-sibling::input").is_selected())

print(obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 2']/preceding-sibling::input").is_selected())
if not obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 2']/preceding-sibling::input").is_selected():
    obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 2']/preceding-sibling::input").click()
    print(obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 2']/preceding-sibling::input").is_selected())

time.sleep(2)

if obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 2']/preceding-sibling::input").is_selected():
    obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 2']/preceding-sibling::input").click()
    print(obj_driver.find_element(By.XPATH, "//span[normalize-space()='Main Level 2']/preceding-sibling::input").is_selected())
