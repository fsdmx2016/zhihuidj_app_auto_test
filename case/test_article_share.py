#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/23 10:22
@Desc    :
"""
import time

from base import base_config
import unittest
from selenium.webdriver.common.by import By
from page import base_page, zx_page
from utils import base_operate


# 分享到第三方平台
from utils.base_operate import is_element_exist


class test_article_share(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()
        base_operate.base_login(cls.driver)

    def test_share_article(self):
        try:
            self.driver.find_element(base_page.tab_zx[0], base_page.tab_zx[1]).click()
            time.sleep(1)
            base_operate.swipe_down(self.driver)

            self.driver.find_element(zx_page.hot_list[0], zx_page.hot_list[1]).find_element(
                zx_page.hot_list_first[0], zx_page.hot_list_first[1]).click()
            time.sleep(2)
            self.driver.find_elements(zx_page.share_btn[0], zx_page.share_btn[1])[1].click()
            time.sleep(3)
            assert is_element_exist(self.driver, '分享/收藏'), True
        finally:
            self.driver.close_app()
