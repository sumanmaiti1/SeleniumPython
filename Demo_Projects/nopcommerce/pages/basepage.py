from ..libraries.html.webelement import WebElement


class BasePage:
    """This is the base page of all the pages"""

    # --------------- This is base page constructor -------------------
    def __init__(self, driver) -> None:
        self._driver = driver
        self._objwebelement = WebElement(self._driver)
