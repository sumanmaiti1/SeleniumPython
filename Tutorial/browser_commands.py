from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from Locators import xpath_advanced as xpath

obj_option , obj_service = Options(),  Service()
obj_option.add_experimental_option('detach',True)
obj_option.add_argument("--start-maximized")
obj_option.add_experimental_option("excludeSwitches", ["enable-automation","disable-popup-blocking"])
# ----- this will disable Personalize Web experience pop up ---------
prefs = {
    'user_experience_metrics': {
        'personalization_data_consent_enabled': True
    }
}
obj_option.add_experimental_option('prefs', prefs)

obj_driver = webdriver.Edge(service=obj_service, options=obj_option)

# -------------- Implicite wait -----------
obj_driver.implicitly_wait(5)

# -------------- Get commands --------------
obj_driver.get('https://www.google.com/')
print(obj_driver.title)    # ----------- Prints the page title
print(obj_driver.current_url)    # ----------- Prints the url of launched site
print(obj_driver.current_window_handle)    # ----------- Prints the id of current window handle
# print(obj_driver.page_source)    # ----------- Prints the page source
obj_driver.get('https://www.flipkart.com/')
print(obj_driver.title)    # ----------- Prints the page title
print(obj_driver.capabilities)
print(obj_driver.log_types)
print(obj_driver.mobile)
print(obj_driver.name)
print(obj_driver.get_window_size())

# ------------- Navigational Commands --------------
obj_driver.back()
obj_driver.refresh()
obj_driver.forward()

# -------------- conditional commnds ----------------
obj_driver.get(r"https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
print(obj_driver.find_element(By.XPATH,xpath.textbox_name).is_enabled())
print(obj_driver.find_element(By.XPATH,xpath.chkbox_music).is_selected())
print(obj_driver.find_element(By.XPATH,xpath.chkbox_music).is_displayed())

# ------------ Browser window Commands ---------------
obj_driver.maximize_window()
obj_driver.minimize_window()
obj_driver.maximize_window()
obj_driver.set_window_size(500,500)
obj_driver.maximize_window()

# -------------- Browser Commands ---------------
obj_driver.close()
obj_driver.quit()