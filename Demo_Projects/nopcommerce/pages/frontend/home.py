from ..basepage import BasePage
from selenium.webdriver.common.by import By
from nopcommerce.utilities.loggen import LogGen


class Home(BasePage):
    """This Page class will contain the locators and method for Home Page"""

    # ---------------- Creating Logger instance ----------------
    __loggen = LogGen.log_gen()

    # --------------- Defining page locators here ---------------
    __ccy = (By.ID, "customerCurrency")
    __register = (By.LINK_TEXT, "Register")
    __login = (By.LINK_TEXT, "Log in")
    __wishlist = (By.XPATH, "//a[contains(text(),Wishlist'')]")
    __shopping_cart = (By.XPATH, "//a[contains(text(),'Shopping cart')]")
    __search_box = (By.NAME, 'q')
    __search_buton = (By.CSS_SELECTOR, '#small-search-box-form button')

    # ------------ This is Home Page Constructor ---------------
    def __init__(self, driver) -> None:
        self.__driver = driver
        super().__init__(self.__driver)

    def verify_if_homepage_is_populated(self):
        """ This method verifies if Home page is populated successfully or not"""
        try:
            if self._objwebelement.check_if_element_is_present(self.__ccy):
                self.__loggen.info(f'Homepage is populated successfully in time.')
                assert True
            else:
                self.__loggen.error(f'Homepage is NOT populated on time')
                assert False
        except Exception as err:
            self.__loggen.error(f'Exception occured at runtime. Err- {err} ')
