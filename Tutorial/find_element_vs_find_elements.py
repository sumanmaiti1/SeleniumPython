from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from Locators import tutorials_point_student_registration_from as pom
from selenium.webdriver.common.by import By
import selenium.common.exceptions as selenium_exceptions

obj_option , obj_service = Options(), Service()
obj_option.add_experimental_option('detach',True)
obj_option.add_experimental_option("excludeSwitches",["enable-automation","disable-popup-blocking"])
obj_option.add_argument('--start-maximized')
prefs = {'user_experience_metrics': {'personalization_data_consent_enabled': True}}
obj_option.add_experimental_option("prefs",prefs)

obj_driver = webdriver.Edge(service=obj_service, options=obj_option)
obj_driver.get(r"https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

# -------------- Find Element ----------------
print('Is Student Registration Form page displayed : ', obj_driver.find_element(eval(pom.headings_student_registration_from.split(':::')[0]),pom.headings_student_registration_from.split(':::')[1]).is_displayed())
obj_driver.find_element(eval(pom.txtbox_name.split(':::')[0]),pom.txtbox_name.split(':::')[1]).send_keys('Suman')

# --------- if element is not found , findelementmethod raises exception
try:
    obj_driver.find_element(eval(pom.txtbox_name_invalid_path.split(':::')[0]),pom.txtbox_name_invalid_path.split(':::')[1]).send_keys('Suman')
except selenium_exceptions.NoSuchElementException as e:
    print('Exception raised', e.msg)

# ---------- if a selector identifies more than one element, find element selects first element -----------
obj_driver.find_element(eval(pom.radio_buttons.split(':::')[0]),pom.radio_buttons.split(':::')[1]).click()  # ---- this will select first radio buuton , that is Male


# -------------- Find Elements, it returns of list of element ----------------
elements = obj_driver.find_elements(eval(pom.radio_buttons.split(':::')[0]),pom.radio_buttons.split(':::')[1])
print(f'Total {len(elements)} elements found. Type: {type(elements)}')
for element in elements:
    element.click()

# ------------ If no element is fond FindElements returns Empty list
print('Elements found for invalid locator is ', len(obj_driver.find_elements(eval(pom.txtbox_name_invalid_path.split(':::')[0]),pom.txtbox_name_invalid_path.split(':::')[1])))

obj_driver.quit()