from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *

obj_option, obj_service = Options(), Service()
obj_option.add_argument('--start-maximized')
obj_option.add_experimental_option('detach', True)
obj_option.add_experimental_option('excludeSwitches', ['enable-automation'])
prefs = {'user_experience_metrics': {'personalization_data_consent_enabled': True}}
obj_option.add_experimental_option('prefs', prefs)

obj_driver = webdriver.Chrome(options=obj_option, service=obj_service)
obj_driver.implicitly_wait(5)
obj_driver.get(r'https://rahulshettyacademy.com/AutomationPractice/')
print(obj_driver.title)

obj_wait = WebDriverWait(obj_driver, timeout=10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
                                                                                        ElementNotVisibleException])

obj_driver.find_element(By.ID, 'autocomplete').clear()
obj_driver.find_element(By.ID, 'autocomplete').send_keys('Argen')
obj_wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='Argentina' and contains(@id,'ui')]"))).click()
print(obj_driver.find_element(By.ID, 'autocomplete').get_property('value'))

print(obj_driver.find_element(By.ID, 'name').get_property('value'))
print(obj_driver.find_element(By.ID, 'name').get_attribute('placeholder'))
print(obj_driver.find_element(By.ID, 'name').is_enabled())
print(obj_driver.find_element(By.ID, 'name').is_displayed())
obj_driver.find_element(By.ID, 'name').clear()
print(obj_driver.find_element(By.ID, 'name').get_property('value'))
print(obj_driver.find_element(By.ID, 'name').get_attribute('placeholder'))
obj_driver.find_element(By.ID, 'name').send_keys('Jay Shree Ram')
print(obj_driver.find_element(By.ID, 'name').get_property('value'))


# ----------- https://seleniumbase.io/demo_page ------------
print('\n---------------------------------------------------------------------------')
obj_driver.get(r'https://seleniumbase.io/demo_page')
obj_driver.find_element(By.ID, 'myTextInput').send_keys('Jay Shree Krishna')
print(obj_driver.find_element(By.ID, 'myTextInput').get_property('value'))
print(obj_driver.find_element(By.ID, 'myTextInput').get_attribute('value'))

obj_driver.find_element(By.ID, 'myTextarea').send_keys('Hare Krishna')
print(obj_driver.find_element(By.ID, 'myTextarea').get_property('value'))
print(obj_driver.find_element(By.ID, 'myTextarea').get_attribute('value'))

print(obj_driver.find_element(By.ID, 'myTextInput2').get_property('value'))
print(obj_driver.find_element(By.ID, 'myTextInput2').get_attribute('value'))
obj_driver.find_element(By.ID, 'myTextInput2').clear()
obj_driver.find_element(By.ID, 'myTextInput2').send_keys('Radhe Radhe')
print(obj_driver.find_element(By.ID, 'myTextInput2').get_property('value'))
print(obj_driver.find_element(By.ID, 'myTextInput2').get_attribute('value'))

print(obj_driver.find_element(By.ID, 'placeholderText').get_property('value'))
print(obj_driver.find_element(By.ID, 'placeholderText').get_attribute('value'))
print(obj_driver.find_element(By.ID, 'placeholderText').get_attribute('placeholder'))
obj_driver.find_element(By.ID, 'placeholderText').clear()
obj_driver.find_element(By.ID, 'placeholderText').send_keys('Har Har Mahadev')
print(obj_driver.find_element(By.ID, 'placeholderText').get_property('value'))
print(obj_driver.find_element(By.ID, 'placeholderText').get_attribute('value'))

obj_driver.quit()