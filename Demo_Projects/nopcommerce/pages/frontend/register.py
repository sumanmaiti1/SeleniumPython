from selenium.webdriver.common.by import By
from ..basepage import BasePage


class Register(BasePage):
    """This Page class will contain the locators and method for Register"""

    # ------------ This is class Constructor of Register Page --------------
    def __init__(self, driver) -> None:
        self.__driver = driver
        super().__init__(self.__driver)
