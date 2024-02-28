from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

obj_options, obj_service = Options(), Service()

# ----- this will start Browser in Maximized Mode ----
obj_options.add_argument("--start-maximized")

# ----- this will start Browser in headless Mode ----
obj_options.add_argument("--headless")

# ----- this will start Browser in Private/incognito Mode ----
obj_options.add_argument("inprivate")

# ----- this will keep the driver browser open even after execution unless closed or Quit----
obj_options.add_experimental_option('detach', True)

obj_options.add_experimental_option('useAutomationExtension', False)

# ------ This will disable ' Ms Edge is being controlled by an Automated software' message -------
# ------ This will disable pop up blocking -----
obj_options.add_experimental_option("excludeSwitches", ["enable-automation","disable-popup-blocking"])

# ----- this will disable Personalize Web experience pop up ---------
prefs = {
    'user_experience_metrics': {
        'personalization_data_consent_enabled': True
    }
}
obj_options.add_experimental_option('prefs', prefs)

obj_driver = webdriver.Edge(options=obj_options, service=obj_service)
obj_driver.get('https://google.com')
print(obj_driver.title)

obj_driver.close()