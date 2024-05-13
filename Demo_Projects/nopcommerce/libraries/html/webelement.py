from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from nopcommerce.utilities.readconfig import ReadConfig
from nopcommerce.utilities.loggen import LogGen


class WebElement:
    """ This class deals with Element method"""

    __loggen = LogGen.log_gen()

    # ---------- this is WebElement constructor ------------
    def __init__(self, driver) -> None:
        self.__driver = driver
        self.__timeout = ReadConfig.read_config('timeout', 'explicit_wait')
        self._webdriverwait = WebDriverWait(driver=self.__driver, timeout=self.__timeout, poll_frequency=2)

    def get_element(self, locator: tuple):
        """This method will search and return a webelement. Returns None otherwise.
        it recieves a locator:tuple  """
        try:
            return self._webdriverwait.until(ec.presence_of_element_located(locator))
        except Exception as err:
            self.__loggen.error(f'Exception occured at runtime. Err- {err} ')
            return None

    def get_elements(self, locator: tuple) -> list:
        """This method will search and return a List of webelements. Returns Empty List [] otherwise.
        it recieves a locator:tuple  """
        try:
            return self.__driver.find_elements(locator)
        except Exception as err:
            self.__loggen.error(f'Exception occured at runtime. Err- {err} ')
            return []

    def check_if_element_is_present(self, locator: tuple) -> bool:
        """This method will check if a webelement is present in Secreen. Returns False otherwise.
        it recieves a locator:tuple  """
        try:
            return self.get_element(locator).is_displayed()
        except Exception as err:
            self.__loggen.error(f'Exception occured at runtime. Err- {err} ')
            return False

    def check_if_element_is_enabled(self, locator: tuple) -> bool:
        """This method will check if a webelement is Enabled in Secreen. Returns False otherwise.
        it recieves a locator:tuple  """
        try:
            return self.get_element(locator).is_enabled()
        except Exception as err:
            self.__loggen.error(f'Exception occured at runtime. Err- {err} ')
            return False

    def check_if_element_is_selected(self, locator: tuple) -> bool:
        """This method will check if a webelement is Selected in Secreen. Returns False otherwise.
        it recieves a locator:tuple  """
        try:
            return self.get_element(locator).is_selected()
        except Exception as err:
            self.__loggen.error(f'Exception occured at runtime. Err- {err} ')
            return False

    def click_element(self, locator: tuple) -> None:
        """This method will click on a webelement . Returns None
        it recieves a locator:tuple  """
        try:
            return self.get_element(locator).click()
        except Exception as err:
            self.__loggen.error(f'Exception occured at runtime while clicking. Err- {err} ')
            self.__driver.execute_script("arguments[0].click();", self.get_element(locator))
