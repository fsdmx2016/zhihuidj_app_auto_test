#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/12/26 12:19
@Desc    :
"""
from selenium.webdriver.common.by import By

# 热点排行
skip_update = [By.ID, 'tv_cancel']
# 热点排行
hot_list = [By.XPATH, '//android.widget.ImageView[@content-desc="热点排行"]']
# 热点排行第一条
hot_list_first = [By.CLASS_NAME, 'android.view.View']
# 回复楼主
reply = [By.XPATH, '//android.widget.EditText[@text="回复楼主"]']
# 发送按钮
send = [By.XPATH, '//android.view.View[@content-desc="发送"]']
# 行业资讯
hy_zixun = [By.XPATH, '//android.view.View[@content-desc="行业资讯"]']
# 收藏按钮
collect = [By.XPATH, '//android.widget.ImageView[contains(@index,5)]']
# 分享按钮
share_btn=[By.CLASS_NAME, 'android.widget.ImageView']
# 详情评论按钮
detail_comment=[By.XPATH, '//android.widget.ImageView[@content-desc="写评论..."]']
# 详情评论输入框
detail_comment_edit=[By.XPATH, '//android.widget.ImageView[@text="写评论..."]']
# 评论按钮
send_comment=[By.XPATH, '//android.view.View[@content-desc="发送"]']
