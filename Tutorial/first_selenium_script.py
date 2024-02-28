from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

# ----- initialising Service and Option object here ---------
obj_service, obj_options = Service(), Options()
# ----- this will keep the driver browser open even after execution unless closed or Quit---------
obj_options.add_experimental_option('detach', True)
obj_options.add_experimental_option('useAutomationExtension', False)
# ------ This will disable ' Ms Edge is being controlled by an Automated software' messasge
obj_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# ----- this will disable Personalize Web experience pop up ---------
prefs = {
    'user_experience_metrics': {
        'personalization_data_consent_enabled': True
    }
}
obj_options.add_experimental_option('prefs', prefs)
# ------ Initiating Obj_driver here ----------
obj_driver = webdriver.Edge(service=obj_service, options=obj_options)

# ------- opening website here -----------
obj_driver.get('https://www.google.com/')
# ------------ Printing Browser title ---------
print(obj_driver.title)
# ------ Closing the Browser here -----------
# obj_driver.close()