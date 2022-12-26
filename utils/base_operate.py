#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/22 15:51
@Desc    :
"""
import os

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# 列表页面上下滑动
from page import base_page, login_page


def swipe_down(driver):
    # 往下滑动
    l = getSize(driver)
    x1 = int(l[0] * 0.3)
    y1 = int(l[0] * 0.73)
    y2 = int(l[0] * 0.15)
    x2 = int(l[0] * 0.3)
    driver.swipe(x1, y1, x2, y2, 1000)
    time.sleep(1)


def swipe_left(driver):
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


# 跳过检查更新，进入首页
def enter_home(driver):
    if is_element_exist(driver, '同意'):
        driver.find_element(By.ID, 'm_tv_right').click()
    if is_element_exist(driver, '下次再说'):
        driver.find_element(base_page.skip_update[0], base_page.skip_update[1]).click()
    time.sleep(4)


# 前置登录
def base_login(driver):
    enter_home(driver)
    # 如果登录按钮存在,则登录账号
    if is_element_exist(driver, '登录'):
        driver.find_element(base_page.login_btn[0], base_page.login_btn[1]).click()
        time.sleep(3)
        if driver.find_element(login_page.quick_login[0], login_page.quick_login[1]):
            driver.find_element(login_page.agree_agreement[0], login_page.agree_agreement[1]).click()
            time.sleep(1)
            driver.find_element(login_page.quick_login[0], login_page.quick_login[1]).click()
        else:
            time.sleep(3)
            driver.find_element(login_page.other_login[0], login_page.other_login[1]).click()
            time.sleep(1)
            driver.find_element(login_page.login_by_password[0], login_page.login_by_password[1]).click()
            time.sleep(3)
            user_name = driver.find_element(login_page.user_name_btn[0], login_page.user_name_btn[1])
            user_name.click()
            os.system('adb shell input text {}'.format('17338123926'))
            time.sleep(2)
            password = driver.find_element(login_page.password_btn[0], login_page.password_btn[1])
            password.click()
            os.system('adb shell input text {}'.format('123456'))
            driver.find_element(login_page.login_btn[0], login_page.login_btn[1]).click()


# 判断元素是否存在
def is_element_exist(driver, element):
    source = driver.page_source
    if element in source:
        return True
    else:
        return False


# 等待元素出现，默认等待5s
def wait_element_appear(driver, search_type, search_value):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((search_type, search_value)))

# 元素点击
def click_element(driver, element_value):
    return driver.find_element(element_value[0], element_value[1]).click()

# 获取元素
def get_element(driver, element_value):
    return driver.find_element(element_value[0], element_value[1])

# 点击元素-父子关系
def click_elements(driver, element_value, child_element_value):
    return driver.find_element(element_value[0], element_value[1]).find_element(
        child_element_value[0], child_element_value[1]).click()
