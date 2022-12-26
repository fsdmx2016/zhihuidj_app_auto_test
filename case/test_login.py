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
from page import base_page, login_page


# 登录
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()
        base_operate.base_login(cls.driver)

    def test_login(self):
        try:
            if base_operate.is_element_exist(self.driver, '登录'):
                base_operate.click_element(self.driver, base_page.login_btn)
                time.sleep(3)
                if self.driver.find_element(login_page.quick_login[0], login_page.quick_login[1]):
                    base_operate.click_element(self.driver, login_page.agree_agreement)
                    time.sleep(1)
                    base_operate.click_element(self.driver, login_page.quick_login)
                else:
                    time.sleep(3)
                    base_operate.click_element(self.driver, login_page.other_login)
                    time.sleep(1)
                    base_operate.click_element(self.driver, login_page.login_by_password)
                    time.sleep(3)
                    user_name = base_operate.get_element(self.driver, login_page.user_name_btn)
                    user_name.click()
                    os.system('adb shell input text {}'.format('17338123926'))
                    time.sleep(2)
                    password = base_operate.get_element(self.driver, login_page.password_btn)
                    password.click()
                    os.system('adb shell input text {}'.format('123456'))
                    base_operate.click_element(self.driver, login_page.login_btn)
                    time.sleep(2)
                    # 判断登录后,页面没有登录文字
                    assert  base_operate.is_element_exist(self.driver,"登录"),False
        finally:
            self.driver.close_app()
