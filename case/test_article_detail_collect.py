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
class article_detail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()
        base_operate.base_login(cls.driver)

    # 进入文章详情、收藏文章
    def test_enter_detail_collect(self):
        try:
            base_operate.enter_home(self.driver)
            self.driver.find_element(base_page.tab_zx[0], base_page.tab_zx[1]).click()
            time.sleep(1)
            self.driver.find_element(zx_page.hy_zixun[0], zx_page.hy_zixun[1]).click()
            time.sleep(2)

            self.driver.find_element(zx_page.collect[0], zx_page.collect[1]).click()
        finally:
            self.driver.close_app()
