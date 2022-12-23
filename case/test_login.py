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


# 登录
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    def test_login(self):
        base_operate.enter_home(self.driver)

        self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="登录"]').click()
        time.sleep(1)
        if base_operate.is_element_exist(self.driver, '一键登录'):
            self.driver.find_element(By.XPATH, '//*[@resource-id="com.zhihuidanji.smarterlayer:id/title"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//android.widget.ImageView[contains(@index,7)]').click()
        time.sleep(1)
        user_name = self.driver.find_element(By.XPATH, '//android.widget.EditText[contains(@index,1)]')
        user_name.click()
        user_name.send_keys('13699103657')
        password = self.driver.find_element(By.XPATH, '//android.widget.EditText[@text="请输入密码"]')
        password.click()
        password.send_keys(
            '123456')
        self.driver.find_element(By.XPATH, '//android.widget.ImageView[contains(@index,3)]').click()

