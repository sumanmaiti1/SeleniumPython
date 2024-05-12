from selenium import webdriver
from nopcommerce.utilities.readconfig import ReadConfig
from nopcommerce.utilities.loggen import LogGen
from nopcommerce.configuration import configuration as config

class Browser:
    """This class deals with the Webdriver Class, Webdriver Options & Webdriver Services"""

    __implicitwait = ReadConfig.read_config('timeout', 'implicit_wait')
    __driver_path = config.web_driver_path + "\\"
    __loggen = LogGen.log_gen()
    __driver, __option, __service = None, None, None

    @staticmethod
    def get_driver(strbrowser: str, **kwargs):
        strheadless = ""
        for key, value in kwargs.items():
            if key.strip().upper().__eq__("HEADLESS"):
                strheadless = str(value).strip().upper()
            elif key.strip().upper().__eq__("MOBILE"):
                strmobile =  value
        try:
            if strbrowser.upper().__eq__('CHROME'):
                Browser.__option = webdriver.ChromeOptions()
                Browser.__service = webdriver.ChromeService(Browser.__driver_path + "chromedriver.exe")
                Browser.__set_options(headless=strheadless, mobile=strmobile)
                Browser.__driver = webdriver.Chrome(options=Browser.__option, service=Browser.__service)
            else:
                Browser.__option = webdriver.EdgeOptions()
                Browser.__service = webdriver.EdgeService(Browser.__driver_path + "msedgedriver.exe")
                Browser.__set_options(headless=strheadless, mobile=strmobile)
                Browser.__driver = webdriver.Edge(options=Browser.__option, service=Browser.__service)

            return Browser.__driver
        except Exception as err:
            Browser.__loggen.info(f'Exception occured at runtime. Error: {err}')

    # ------------- set Option for the webdriver object --------------

    @staticmethod
    def __set_options(**kwargs):
        Browser.__option.add_argument('--start-maximized')
        Browser.__option.add_argument('--disable-infobars')

        # ----------------- Setting options for headless browser -----------------
        for key, value in kwargs.items():
            if key.strip().upper().__eq__("HEADLESS"):
                strheadless = str(value).strip().upper()
                if strheadless == "TRUE" or strheadless == "YES" or strheadless == "Y":
                    Browser.__option.add_argument('--headless')
            elif key.strip().upper().__eq__("MOBILE"):
                if value is not None:
                    Browser.__option.add_experimental_option("mobileEmulation", value)

        Browser.__option.add_experimental_option('excludeSwitches', ['enable-automation', 'useAutomationExtension'])

        # ------------------ To disable personalise your web experience message in new edge browser -------------
        prefs = {
            'user_experience_metrics': {
                'personalization_data_consent_enabled': True
            }
        }
        Browser.__option.add_experimental_option('prefs', prefs)
