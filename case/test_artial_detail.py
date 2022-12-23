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

# 文章收藏
class article_detail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = base_config.init_driver()

     # 进入文章详情
    def test_enter_detail(self):
        base_operate.enter_home(self.driver)

        self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="资讯"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="行业资讯"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//android.widget.ImageView[contains(@index,5)]').click()

