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
        print("所有可用的输入法：", self.driver.available_ime_engines)
        print("当前正在使用的输入法：", self.driver.active_ime_engine)
        print("切换输入法到 io.appium.settings/.UnicodeIME")
        self.driver.activate_ime_engine('io.appium.settings/.UnicodeIME')
        print("当前正在使用的输入法：", self.driver.active_ime_engine)
        # edit_text.press_keycode(8).press_keycode(12).press_keycode(12).press_keycode(14)

        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("回复楼主")').send_keys('1123123')

        # strcommand = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg '" + '123123' + "'"
        # os.system(strcommand)
        edit_text.send_keys(12312)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="发送"]').click()

