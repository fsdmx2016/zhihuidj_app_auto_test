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
from utils import base_operate


# 登录


class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    def test_login(self):
        try:
            base_operate.enter_home(self.driver)

            self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="登录"]').click()
            time.sleep(1)
            if base_operate.is_element_exist(self.driver, '一键登录'):
                # self.driver.find_element(By.XPATH, '//*[@resource-id="com.zhihuidanji.smarterlayer:id/title"]').click()
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.zhihuidanji.smarterlayer:id/yd_quick_login_privacy_checkbox"]').click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.zhihuidanji.smarterlayer:id/oauth_login"]').click()
            else:
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//android.widget.ImageView[contains(@index,7)]').click()
                time.sleep(3)
                user_name = self.driver.find_element(By.XPATH, '//android.widget.EditText[@text="请输入手机号"]')
                user_name.click()
                os.system('adb shell input text {}'.format('17338123926'))
                time.sleep(2)
                password = self.driver.find_element(By.XPATH, '//android.widget.EditText[@text="请输入密码"]')
                password.click()
                os.system('adb shell input text {}'.format('123456'))
                self.driver.find_element(By.XPATH, '//android.widget.ImageView[contains(@index,3)]').click()

        finally:
            self.driver.close_app()
