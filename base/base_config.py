#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/18 10:08
@Desc    :
"""
import os

from appium.webdriver import Remote
from config import read_config
apk_path = r"/Users/sunpeng/Desktop/zhdj_2.8.2.apk"
platformVersion = read_config.ReadConfig.get_data('device1', 'platformVersion')
deviceName = read_config.ReadConfig.get_data('device1', 'deviceName')
appPackage = read_config.ReadConfig.get_data('device1', 'appPackage')
appActivity = read_config.ReadConfig.get_data('device1', 'appActivity')


def init_driver():
    dict = {}
    dict['platformName'] = 'Android'
    dict['platformVersion'] = platformVersion
    dict['deviceName'] = deviceName
    dict['app'] = apk_path
    # dict['automationName'] = 'UIAutomator2'
    dict['noReset'] = True
    dict[
        'appPackage'] = appPackage
    dict[
        'appActivity'] = appActivity
    dict['unicodeKeyboard'] = True  # 使用Unicode编码方式发送字符串
    dict['resetKeyboard'] = True  # 隐藏键盘
    driver = Remote('http://127.0.0.1:4723/wd/hub', dict)
    return driver
