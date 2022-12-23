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
from page import base_page
from utils import base_operate

# 分享到第三方平台
class test_article_collect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    def send_report(self):
        base_operate.enter_home(self.driver)

        self.driver.find_element(base_page.tab_zx[0], base_page.tab_zx[1]).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="热点排行"]').find_element(
            By.CLASS_NAME, 'android.view.View').click()
        time.sleep(2)
        self.driver.find_elements(By.CLASS_NAME, 'android.widget.ImageView')[1].click()

