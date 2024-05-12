import pytest
from nopcommerce.utilities.loggen import LogGen
from nopcommerce.tests.basetest import BaseTest


class TestDemo(BaseTest):
    a = LogGen.log_gen()

    @pytest.mark.suman
    def test_1(self):
        self.a.info('--------TC 1 Starts ------------')
        self.a.info('--------TC 1 Executing ------------')
        self.driver.get('https://www.google.co.in/')
        assert 2==2
        self.a.info('--------TC 1 Ends ------------')

    @pytest.mark.suman
    def test_2(self):
        self.a.info('--------TC 2 Starts ------------')
        self.driver.get('https://sanatanisankha.blogspot.com/')
        self.a.info('--------TC 2 Executing ------------')
        assert 2 == 4
        self.a.info('--------TC 2 Ends ------------')

    def test_3(self):
        self.a.info('--------TC 3 Starts ------------')
        self.a.info('--------TC 3 Executing ------------')
        self.a.info('--------TC 3 Ends ------------')

    def test_4(self):
        self.a.info('--------TC 4 Starts ------------')
        self.a.info('--------TC 4 Executing ------------')
        self.a.info('--------TC 4 Ends ------------')
