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
from page import base_page, transaction_page
from utils import base_operate


# 视频类型进入到视频详情页播放
class Video_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()
        base_operate.base_login(cls.driver)

    # 视频类型进入到视频详情页播放
    def test_video_lock(self):
        try:
            self.driver.find_element(base_page.tab_jy[0], base_page.tab_jy[1]).click()
            time.sleep(1)
            # 滑动三次保证元素被找到
            base_operate.swipe_down(self.driver)
            base_operate.swipe_down(self.driver)
            self.driver.find_element(transaction_page.video_region[0], transaction_page.video_region[1]).find_element(
                transaction_page.live_broadcast_btn[0], transaction_page.live_broadcast_btn[1]).click()
            time.sleep(3)
            is_enter = base_operate.is_element_exist(self.driver, '课程简介')
            assert is_enter, True
        finally:
            self.driver.close_app()
