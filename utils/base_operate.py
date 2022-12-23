#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/22 15:51
@Desc    :
"""
from selenium.webdriver.common.by import By

from base import base_config

import time


# 列表页面上下滑动
from page import base_page


def swipe_down(driver):
    # 往下滑动
    l = getSize(driver)
    x1 = int(l[0] * 0.3)
    y1 = int(l[0] * 0.73)
    y2 = int(l[0] * 0.15)
    x2 = int(l[0] * 0.3)
    driver.swipe(x1, y1, x2, y2, 1000)
    time.sleep(1)



def swip_left(driver):
    l = getSize(driver)
    x1 = int(l[0] * 0.75)
    x2 = int(l[0] * 0.25)
    y1 = int(l[0] * 0.3)
    y2 = int(l[0] * 0.3)
    driver.swipe(x1, x2, y1, y2, 1000)
    time.sleep(1)
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def enter_home(driver):
    # if is_element_exist(driver, '同意'):
    #     driver.find_element(By.ID, 'm_tv_right').click()
    driver.find_element(base_page.skip_update[0], base_page.skip_update[1]).click()
    time.sleep(4)



def is_element_exist(driver, element):
    source = driver.page_source
    if element in source:
        return True
    else:
        return False
