#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/23 10:22
@Desc    :
"""
import os
import time

from base import base_config
import unittest
from selenium.webdriver.common.by import By
from page import base_page

# 文章评论
from utils import base_operate
from page import zx_page
from utils.base_operate import is_element_exist


class test_remark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    def test_send_report(self):
        try:
            base_operate.enter_home(self.driver)
            self.driver.find_element(base_page.tab_zx[0], base_page.tab_zx[1]).click()
            time.sleep(1)
            self.driver.find_element(zx_page.hot_list[0], zx_page.hot_list[1]).find_element(
                zx_page.hot_list_first[0], zx_page.hot_list_first[1]).click()
            time.sleep(2)
            edit_text = self.driver.find_element(zx_page.reply[0], zx_page.reply[1])
            edit_text.click()
            current_time = str(time.time())
            os.system('adb shell input text {}'.format(current_time))
            edit_text.send_keys('123123')
            time.sleep(1)
            self.driver.find_element(zx_page.send[0], zx_page.send[1]).click()
            time.sleep(1)
            assert is_element_exist(self.driver, current_time), True
        finally:
            self.driver.close_app()
