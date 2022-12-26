#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/26 14:14
@Desc    :
"""
from selenium.webdriver.common.by import By

# 同意协议
agree_agreement = [By.XPATH, '//*[@resource-id="com.zhihuidanji.smarterlayer:id/yd_quick_login_privacy_checkbox"]']
# 一键登录
quick_login = [By.XPATH, '//*[@resource-id="com.zhihuidanji.smarterlayer:id/oauth_login"]']
# 其他方式登录
other_login = [By.XPATH, '//*[@resource-id="com.zhihuidanji.smarterlayer:id/title"]']
# 账号密码登录
login_by_password = [By.XPATH, '//android.widget.ImageView[contains(@index,7)]']
# 用户名
user_name_btn = [By.XPATH, '//android.widget.EditText[@text="请输入手机号"]']
# 密码
password_btn = [By.XPATH, '//android.widget.EditText[@text="请输入密码"]']
# 登录
login_btn = [By.XPATH, '//android.widget.ImageView[contains(@index,3)]']
