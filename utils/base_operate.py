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
    time.sleep(2)
    if is_element_exist(driver, '下次再说'):
        click_element(driver, base_page.skip_update)
    time.sleep(4)


# 前置登录
def base_login(driver):
    enter_home(driver)
    # 如果登录按钮存在,则走登录逻辑
    if is_element_exist(driver, '登录'):
        time.sleep(1)
        # 点击登录按钮
        click_element(driver, base_page.login_btn)
        time.sleep(3)
        # 如果有一键登录按钮,则同意协议，并点击一键登录按钮
        if driver.find_element(login_page.quick_login[0], login_page.quick_login[1]):
            click_element(driver, login_page.agree_agreement)
            time.sleep(1)
            click_element(driver, login_page.quick_login)
            time.sleep(3)
        else:
            time.sleep(3)
            # 如果不插入手机卡,则直接通过密码登录
            # base_operate.click_element(self.driver, login_page.other_login)
            # time.sleep(1)
            # 切换到密码登录
            click_element(driver, login_page.login_by_password)
            time.sleep(3)
            # 找到用户名输入框
            user_name = get_element(driver, login_page.user_name_btn)
            user_name.click()
            os.system('adb shell input text {}'.format('17338123926'))
            time.sleep(2)
            # 找到密码输入框
            password = get_element(driver, login_page.password_btn)
            password.click()
            os.system('adb shell input text {}'.format('123456'))
            # 点击登录按钮
            click_element(driver, login_page.login_btn)
            time.sleep(3)


# 判断元素是否存在
def is_element_exist(driver, element):
    source = driver.page_source
    if element in source:
        return True
    else:
        return False


def wait_element(driver, element_value):
    # 循环5次,如果能找到元素,则退出,否则超过5s报错
    for i in range(5):
        if driver.find_element(element_value[0], element_value[1]):
            break
        time.sleep(1)
        if i == 4:
            raise Exception("5s元素" + element_value[1] + "依旧未找到！")


def wait_element_appear(driver, search_type, search_value):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((search_type, search_value)))


# 元素点击
def click_element(driver, element_value):
    driver.find_element(element_value[0], element_value[1]).click()


# 获取元素
def get_element(driver, element_value):
    return driver.find_element(element_value[0], element_value[1])


# 点击元素-父子关系
def click_elements(driver, element_value, child_element_value):
    driver.find_element(element_value[0], element_value[1]).find_element(
        child_element_value[0], child_element_value[1]).click()


# 点击元素列表的第N个
def click_elements_index(driver, element_value, index):
    driver.find_elements(element_value[0], element_value[1])[index].click()
