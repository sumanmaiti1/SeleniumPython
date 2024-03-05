from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# ------------ Selenium Webdriver has 2 waits. 1) implicit wait   2) Explicit wait --------------
# ------------ Fluent wait is just a type of Explicit wait --------------
# ------------ python's time.sleep() is not efficient at all ------------

obj_option, obj_service = Options(), Service()
obj_option.add_argument('--start-maximized')
obj_option.add_experimental_option('detach', True)
obj_option.add_experimental_option('excludeSwitches', ['enable-automation', 'disable-popup-blocking'])
prefs = {'user_experience_metrics': {'personalization_data_consent_enabled': True}}
obj_option.add_experimental_option('prefs', prefs)

obj_driver = webdriver.Edge(options=obj_option, service=obj_service)
obj_driver.get(r"https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
# ----------- Implicit Wait ---------------
obj_driver.implicitly_wait(5)
print(obj_driver.timeouts.implicit_wait)
print(obj_driver.timeouts.page_load)
print(obj_driver.timeouts.script)

# ---------- Explicit Wait -----------
obj_wait = WebDriverWait(obj_driver, timeout=10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, NoSuchFrameException])
obj_wait.until(EC.presence_of_element_located((By.ID, 'name'))).send_keys('Jay Shree Ram')
obj_wait.until(EC.visibility_of_element_located((By.NAME, 'email'))).send_keys('Janki@SriRam.com')
obj_wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Female']/preceding-sibling::input"))).click()
print(obj_wait._driver.timeouts.implicit_wait)
print(obj_wait._timeout)
obj_driver.quit()