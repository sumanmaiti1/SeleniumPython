import pytest
from ..utilities.loggen import LogGen


class TestDemo():
    a=LogGen.log_gen()
    def test_1(self):
        self.a.info('--------TC 1 Starts ------------')
        self.a.info('--------TC 1 Executing ------------')
        self.driver.get('https://www.google.co.in/')
        self.a.info('--------TC 1 Ends ------------')

    def test_2(self):
        self.a.info('--------TC 2 Starts ------------')
        self.a.info('--------TC 2 Executing ------------')
        self.a.info('--------TC 2 Ends ------------')

    def test_3(self):
        self.a.info('--------TC 3 Starts ------------')
        self.a.info('--------TC 3 Executing ------------')
        self.a.info('--------TC 3 Ends ------------')


    def test_4(self):
        self.a.info('--------TC 4 Starts ------------')
        self.a.info('--------TC 4 Executing ------------')
        self.a.info('--------TC 4 Ends ------------')