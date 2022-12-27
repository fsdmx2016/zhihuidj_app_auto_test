#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/18 10:44
@Desc    :
"""
from base import base_config
import unittest


# 滑动
from utils import base_operate


class Swipe_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    def test_swipe(self):
        base_operate.base_login(self.driver)
        try:
            base_operate.swipe_down(self.driver)
            base_operate.swipe_left(self.driver)
        finally:
            self.driver.close_app()
