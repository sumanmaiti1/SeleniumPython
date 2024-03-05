from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser:
    '''
    This class will deral with webdriver setup and teardown.
    it has obly two methods to playwith..
    setup
    teardown
    '''
    __browser_driver = None
    # ------------- This is class constructor
    # def __init__(self)->None:
    #     self.__strbrowser = ''

    # ------------- This is a private method which deals with setting browser capabilities ------------
    def __set_browser_capabilities(self):
        if self.__strbrowser.upper()=='EDGE':
            self.__obj_option = webdriver.EdgeOptions()
            self.__obj_service = webdriver.EdgeService()
        elif self.__strbrowser.upper()=='CHROME':
            self.__obj_option = webdriver.ChromeOptions()
            self.__obj_service = webdriver.ChromeService()

        self.__obj_option.add_argument('--start-maximized')
        self.__obj_option.add_experimental_option('detach', True)
        self.__obj_option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.__prefs={'user_experience_metrics': {'personalization_data_consent_enabled': True}}
        self.__obj_option.add_experimental_option('prefs',self.__prefs)

    # ------------- This is a private method which deals with initiating diff driver instance ------------
    def __set_browser_driver(self):
        if (len(self.__strbrowser.strip()))>0:
            if self.__strbrowser.upper()=='CHROME':
                Browser.__browser_driver = webdriver.Chrome(options=self.__obj_option, service=self.__obj_service)
            elif self.__strbrowser.upper()=='EDGE':
                Browser.__browser_driver = webdriver.Edge(options=self.__obj_option, service=self.__obj_service)
        else:
            print('No Browser name is provided')
    def setup(self,strbrowser:str):
        '''
        This will initiate and return webdriver instance.
        it takes one input parameter as browsername
        it returns a webdriver instance
        '''
        self.__strbrowser=strbrowser
        self.__set_browser_capabilities()
        self.__set_browser_driver()
        return self.__browser_driver

    def teardown(objdriver):
        '''
        This will kill the webdriver instance.
        it takes an objdriver instance as input
        '''
        objdriver.quit()

#----------- first driver instance and opening url --------
obj_driver1 = Browser().setup('chrome')
obj_driver1.get(r'https://google.com')

#----------- second driver instance and opening url --------
obj_driver2 = Browser().setup('edge')
obj_driver2.get(r'https://www.tutorialspoint.com')

#----------- printig the page titles here --------
print(obj_driver1.title)
print(obj_driver2.title)

#----------- Killing the driver instance here --------
Browser.teardown(obj_driver1)
Browser.teardown(obj_driver2)