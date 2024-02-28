import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

obj_options, obj_service = Options(), Service()

obj_options.add_argument('start-maximized')
obj_options.add_experimental_option('detach',True)
obj_options.add_experimental_option("excludeSwitches", ["enable-automation","disable-popup-blocking"])
prefs = {
    'user_experience_metrics': {
        'personalization_data_consent_enabled': True
    }
}
obj_options.add_experimental_option('prefs', prefs)


obj_driver = webdriver.Edge(options=obj_options, service=obj_service)
obj_driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
print(obj_driver.title)

# by ID
textbox_name = obj_driver.find_element(By.ID,'name')
textbox_name.send_keys('Jay Shree krishna')
print(textbox_name.get_property('value'))
print(textbox_name.get_attribute('value'))

# by Name
textbox_email = obj_driver.find_element(By.NAME,'email')
print(textbox_email.get_attribute('placeholder'))
textbox_email.send_keys('krishna@vasudev.com')

# by Tagname
input_fields = obj_driver.find_elements(By.TAG_NAME,'input')
print(len(input_fields))
time.sleep(2)

# By LinkText
link_login = obj_driver.find_element(By.LINK_TEXT,'Login')
link_login.click()

# By partialLinkText
link_practice_form =obj_driver.find_element(By.PARTIAL_LINK_TEXT,'Practice')
time.sleep(2)
link_practice_form.click()

# By Xpath
chkbox_sports = obj_driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/form/div[7]/div/div/div[1]/input')
chkbox_sports.click()
time.sleep(2)

# By CSS Selector
option_NCR = obj_driver.find_element(By.CSS_SELECTOR,'#state>option:nth-child(2)')
option_NCR.click()
time.sleep(2)

# By_className
logo_image = obj_driver.find_element(By.CLASS_NAME,'logo-desktop')
logo_image.click()