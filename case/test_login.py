#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/23 10:22
@Desc    :
"""
import os
import time

from selenium.webdriver.common.by import By

from base import base_config
import unittest
from utils import base_operate
from page import base_page, login_page


# 登录
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    def test_login(self):
        base_operate.base_login(self.driver)
        try:
            time.sleep(2)
            # 如果登录按钮存在,则走登录逻辑
            if base_operate.is_element_exist(self.driver, '登录'):
                # 点击登录按钮
                base_operate.click_element(self.driver, base_page.login_btn)
                time.sleep(3)
                # 如果有一键登录按钮,则同意协议，并点击一键登录按钮
                if base_operate.is_element_exist(self.driver, '其他方式登录'):
                    base_operate.click_element(self.driver, login_page.agree_agreement)
                    time.sleep(1)
                    base_operate.click_element(self.driver, login_page.quick_login)
                    # 验证页面上没有登录按钮
                    time.sleep(3)
                    # 判断登录后,页面没有登录文字
                    assert base_operate.is_element_exist(self.driver, "登录"), False
                else:
                    time.sleep(3)
                    # 如果不插入手机卡,则直接通过密码登录
                    # base_operate.click_element(self.driver, login_page.other_login)
                    # time.sleep(1)
                    # 切换到密码登录
                    base_operate.click_element(self.driver, login_page.login_by_password)
                    time.sleep(3)
                    # data=self.driver.find_element(By.XPATH,'//android.widget.EditText[contains(@index,1)]')
                    # data.click()
                    # data.press_keycode(8)
                    # 找到用户名输入框
                    user_name = base_operate.get_element(self.driver, login_page.user_name_btn)
                    user_name.click()
                    os.system('adb shell input text {}'.format('17338123926'))
                    time.sleep(2)
                    # 找到密码输入框
                    password = base_operate.get_element(self.driver, login_page.password_btn)
                    password.click()
                    os.system('adb shell input text {}'.format('123456'))
                    # 点击登录按钮
                    base_operate.click_element(self.driver, login_page.login_btn)
                    time.sleep(3)
                    # 判断登录后,页面没有登录文字
                    assert base_operate.is_element_exist(self.driver, "登录"), False
        finally:
            self.driver.quit()
