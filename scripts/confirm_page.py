"""
测试页面是否跑得通
"""
from selenium.webdriver.common.by import By

from base.page import Page

# 首页关闭更新
Page.get_home().close_update()
# 首页-我的
Page.get_home().click_my_btn()
# 个人中心-登录注册
Page.get_person().click_login_sigin()
#  登录操作
Page.get_login().login("15077632873", "xzynzyn")

# 测试输入错误的密码
# 定位提升信息
# mess_xpath = (By.XPATH, "//*[contains(@text,'错误')]")
# # 任意页面类都是集成了Base类，所以可以调用base类方法，search_ele为base类的方法
# message = Page.get_setting().search_ele(mess_xpath, timeout=3, poll_frequency=0.3).text
# print("提示信息：", message)
# # 点击返回按钮
# Page.get_login().login_return()
# 因为该方法已经被封装。所以只需要调用即可get_login为任意去，为了调用base的方法
print("提示信息为：", Page.get_login().get_toast("错误"))

# # 登录确认按钮
# Page.get_login().login_acc()
# # 个人中心-打印用户名
# print("用户名：", Page.get_person().get_user_name())
# # 个人中心-设置
# Page.get_person().click_setting_btn()
# # 页面点击退出
# Page.get_setting().setting_quit()
