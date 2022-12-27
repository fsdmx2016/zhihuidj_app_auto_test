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
        base_operate.base_login(self.driver)
        try:
            # 点击资讯tab
            base_operate.click_element(self.driver, base_page.tab_zx)
            time.sleep(1)
            base_operate.click_elements(self.driver,zx_page.hot_list,zx_page.hot_list_first)
            time.sleep(2)
            # 点击评论输入框
            edit_text=base_operate.get_element(self.driver, zx_page.reply)
            edit_text.click()
            current_time = str(time.time())
            os.system('adb shell input text {}'.format(current_time))
            edit_text.send_keys('123123')
            time.sleep(1)
            base_operate.click_element(self.driver, zx_page.send)
            time.sleep(1)
            assert is_element_exist(self.driver, current_time), True
        finally:
            self.driver.close_app()
