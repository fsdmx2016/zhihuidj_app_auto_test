#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/18 10:08
@Desc    :
"""
import os

from appium.webdriver import Remote

apk_path = '/Users/sunpeng/Desktop/智慧蛋鸡_2.8.2.apk'


def init_driver():
    dict = {}
    dict['platformName'] = 'Android'  # 指定手机平台名称
    dict['platformVersion'] = '13'  # 指定手机操作系统版本
    dict['deviceName'] = '99f64c62'  # 指定手机或者模拟器名称
    dict['app'] = apk_path  # 指定apk/ipa文件在电脑上的路径
    dict['automationName'] = 'UIAutomator2'
    dict['noReset'] = True  # no不Reset重置-->true不重置应用 false-->重置
    dict[
        'appPackage'] = 'com.zhihuidanji.smarterlayer'
    dict[
        'appActivity'] = 'com.zhihuidanji.smarterlayer.ui.GuideUI'
    dict['unicodeKeyboard'] = True  # 使用Unicode编码方式发送字符串
    dict['resetKeyboard'] = False  # 隐藏键盘
    driver = Remote('http://127.0.0.1:4723/wd/hub', dict)
    return driver
