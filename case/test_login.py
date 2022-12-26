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
                self.driver.find_element(base_page.login_btn[0], base_page.login_btn[1]).click()
                time.sleep(3)
                if self.driver.find_element(login_page.quick_login[0], login_page.quick_login[1]):
                    self.driver.find_element(login_page.agree_agreement[0], login_page.agree_agreement[1]).click()
                    time.sleep(1)
                    self.driver.find_element(login_page.quick_login[0], login_page.quick_login[1]).click()
                else:
                    time.sleep(3)
                    self.driver.find_element(login_page.other_login[0], login_page.other_login[1]).click()
                    time.sleep(1)
                    self.driver.find_element(login_page.login_by_password[0], login_page.login_by_password[1]).click()
                    time.sleep(3)
                    user_name = self.driver.find_element(login_page.user_name_btn[0], login_page.user_name_btn[1])
                    user_name.click()
                    os.system('adb shell input text {}'.format('17338123926'))
                    time.sleep(2)
                    password = self.driver.find_element(login_page.password_btn[0], login_page.password_btn[1])
                    password.click()
                    os.system('adb shell input text {}'.format('123456'))
                    self.driver.find_element(login_page.login_btn[0], login_page.login_btn[1]).click()


        finally:
            self.driver.close_app()
