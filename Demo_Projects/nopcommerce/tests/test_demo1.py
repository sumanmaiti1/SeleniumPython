import pytest
from nopcommerce.utilities.loggen import LogGen
from nopcommerce.tests.basetest import BaseTest


class TestDemo1(BaseTest):
    a = LogGen.log_gen()

    def test_11(self):
        self.a.info('--------TC 11 Starts ------------')
        self.a.info('--------TC 11 Executing ------------')
        self.a.info('--------TC 11 Ends ------------')

    def test_21(self):
        self.a.info('--------TC 21 Starts ------------')
        self.a.info('--------TC 21 Executing ------------')
        self.a.info('--------TC 21 Ends ------------')

    def test_31(self):
        self.a.info('--------TC 31 Starts ------------')
        self.a.info('--------TC 31 Executing ------------')
        self.a.info('--------TC 31 Ends ------------')

    def test_41(self):
        self.a.info('--------TC 41 Starts ------------')
        self.driver.get('https://www.amazon.com')
        assert False
        self.a.info('--------TC 41 Executing ------------')
        self.a.info('--------TC 41 Ends ------------')
