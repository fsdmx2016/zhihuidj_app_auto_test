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
from page import base_page, zx_page
from utils import base_operate


# 文章收藏
class Test_article_detail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    # 进入文章详情、收藏文章
    def test_enter_detail_collect(self):
        base_operate.base_login(self.driver)
        try:
            # 点击资讯tab
            base_operate.click_element(self.driver, base_page.tab_zx)
            time.sleep(2)
            # 点击行业资讯
            base_operate.click_element(self.driver, zx_page.hy_zixun)
            time.sleep(2)
            # 点击收藏按钮
            base_operate.click_element(self.driver, zx_page.collect)
            time.sleep(3)
        finally:
            self.driver.quit()
