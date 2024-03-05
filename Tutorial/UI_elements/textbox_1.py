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
obj_driver.implicitly_wait(10)
obj_driver.get(r'https://www.tutorialspoint.com/selenium/practice/text-box.php')
print(obj_driver.title)

# ---------------- clear the text boxes ----------------
obj_driver.find_element(By.ID, 'fullname').clear()
obj_driver.find_element(By.ID, 'email').clear()
obj_driver.find_element(By.ID, 'address').clear()
obj_driver.find_element(By.ID, 'password').clear()

# ---------------- fill the text boxes ----------------
obj_driver.find_element(By.ID, 'fullname').send_keys('Test')
obj_driver.find_element(By.ID, 'email').send_keys('Test@test.com')
obj_driver.find_element(By.ID, 'address').send_keys('Test Address\nTest Address')
obj_driver.find_element(By.ID, 'password').send_keys('Test123$')

# ---------------- get the  values from text boxes ----------------
print(obj_driver.find_element(By.ID, 'fullname').get_property('value'))
print(obj_driver.find_element(By.ID, 'email').get_property('value'))
print(obj_driver.find_element(By.ID, 'address').get_property('value'))
print(obj_driver.find_element(By.ID, 'password').get_property('value'))

obj_driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# ------------ doing the same for https://demoqa.com/text-box -------------
obj_driver.get(r'https://demoqa.com/text-box')
obj_driver.find_element(By.ID,'userName').send_keys('Test')
obj_driver.find_element(By.ID,'userEmail').send_keys('test@test.com')
obj_driver.find_element(By.ID,'currentAddress').send_keys('Test Address\nTest Address')
obj_driver.find_element(By.ID,'permanentAddress').send_keys('Test Address\nTest Address')
# obj_driver.find_element(By.ID,'submit').click() ------- This doesn't work ....
# obj_driver.find_element(By.ID,'submit').submit() ------- This doesn't work ....
obj_driver.execute_script('arguments[0].click()',obj_driver.find_element(By.ID,'submit'))

print(obj_driver.find_element(By.ID,'output').text)

obj_driver.quit()