#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/22 14:39
@Desc    :
"""
from selenium.webdriver.common.by import By

# 取消更新
skip_update = [By.ID, 'tv_cancel']
# tab_咨询
tab_zx = [By.XPATH, '//android.widget.ImageView[@content-desc="资讯"]']
# tab_交易
tab_jy = [By.XPATH, '//android.widget.ImageView[@content-desc="交易"]']
# 登录按钮
login_btn=[By.XPATH, '//android.widget.ImageView[@content-desc="登录"]']