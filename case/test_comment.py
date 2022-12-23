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

# 文章评论
from utils import base_operate


class test_remark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    def test_send_report(self):
        base_operate.enter_home(self.driver)

        self.driver.find_element(base_page.tab_zx[0], base_page.tab_zx[1]).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="热点排行"]').find_element(
            By.CLASS_NAME, 'android.view.View').click()
        time.sleep(2)
        edit_text=self.driver.find_element(By.XPATH, '//android.widget.EditText[@text="回复楼主"]')
        edit_text.click()
        edit_text.clear()
        edit_text.send_keys("123123")
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="发送"]').click()

