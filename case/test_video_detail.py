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

# 视频类型进入到视频详情页播放
class Video_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

    # 视频类型进入到视频详情页播放
    def test_video_lock(self):
        base_operate.enter_home(self.driver)
        self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="交易"]').click()
        time.sleep(1)
        # 滑动两次保证元素被找到
        base_operate.swipe_down(self.driver)
        base_operate.swipe_down(self.driver)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.ScrollView').find_element(
            By.CLASS_NAME, 'android.widget.ImageView').click()

