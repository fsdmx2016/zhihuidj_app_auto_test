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

    def test_share_article(self):
        base_operate.base_login(self.driver)

        try:
            # 点击资讯tab
            base_operate.click_element(self.driver, base_page.tab_zx)
            time.sleep(1)
            base_operate.swipe_down(self.driver)
            time.sleep(2)
            base_operate.click_elements(self.driver, zx_page.hot_list, zx_page.hot_list_first)

            # 点击分享按钮
            base_operate.click_elements_index(self.driver,zx_page.share_btn,1)
            time.sleep(3)
            assert is_element_exist(self.driver, '分享/收藏'), True
        finally:
            self.driver.quit()
