#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/18 10:44
@Desc    :
"""
import time

from base import base_config
import unittest
from selenium.webdriver.common.by import By
from page import base_page

# 滑动
from utils import base_operate


class Swipe_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()
        base_operate.base_login(cls.driver)

    def test_swipe(self):
        try:
            base_operate.swipe_down(self.driver)
            base_operate.swip_left(self.driver)
        finally:
            self.driver.close_app()
