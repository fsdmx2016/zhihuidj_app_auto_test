#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/23 10:22
@Desc    :
"""
import os
import time

from selenium.webdriver.common.by import By

from base import base_config
import unittest
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
            time.sleep(2)
            # 点击行业资讯
            base_operate.click_element(self.driver, zx_page.hy_zixun)
            time.sleep(2)
            base_operate.click_element(self.driver, zx_page.detail_comment)
            time.sleep(2)
            base_operate.click_element(self.driver, zx_page.detail_comment_edit)
            self.driver.press_keycode(8)
            time.sleep(2)
            base_operate.click_element(self.driver, zx_page.send_comment)
            time.sleep(2)
        finally:
            self.driver.quit()
