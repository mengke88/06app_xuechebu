"""
封装基本操作方式（如点击，输入，设置滑动事件等），相当于操作层
"""
import os
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.Driver import Driver


class Base:

    def __init__(self):
        self.driver = Driver.get_app_driver()

    # 封装只能等待的方法，在线面每个操作内容都会调用这个方法，这样每步操作都会实现等待
    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象
        """
        #
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 封装一个打印页面所以信息
    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象列表
        """
        #
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    # 封装点击页面的方法
    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        点击元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        self.search_ele(loc, timeout, poll_frequency).click()

    # 封装元素输入
    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        """
        输入内容
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param text: 输入的文本内容
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        # 定位输入框元素
        inp = self.search_ele(loc, timeout, poll_frequency)
        # 清空输入框
        inp.clear()
        # 输入信息
        inp.send_keys(text)

    # 封装滑动屏幕的方法
    def swipe_screen(self, tag=1):
        """
        滑动屏幕
        :param tag: 1:向上 2:向下 3:向左 4:向右
        :return:
        """
        # 获取屏幕分辨率 {"width":xx,"height":yy}
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        # 等待1s
        time.sleep(1)

        if tag == 1:  # 手指向上滑，所以height从高到低，页面往下走
            # 宽*50%，高*80%  宽*50%，高*20%
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 1500)
        if tag == 2:  # 手指向下滑动，所以height从低到高，，页面往上走
            # 宽*50%，高*20%  宽*50%，高*80%
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 1500)
        if tag == 3:  # 向左滑动，手指从右网左，所以width从高往低，页面向右走
            # 宽*80%，高*50%  宽*20%，高*50%
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 1500)
        if tag == 4:  # 向右滑动，手指从左往右，所以width从低到高，页面往左走
            # 宽*20%，高*50%  宽*80%，高*50%
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 1500)

    # 封装一个获取那种弹出框。然后就消失的方法，如当输入错误密码给出提示
    def get_toast(self, mess):
        """
        获取toast提示信息
        mess：拼接xpat的提示信息,表示动态获取弹出框信息，你调用的时候希望里面包含什么就写什么，这样不至于把方法写死
        """
        mess_xpath = (By.XPATH, "//*[contains(@text,'%s')]" % mess)
        return self.search_ele(mess_xpath, timeout=3, poll_frequency=0.3).text

    # 封装一个通用截图的方法
    def screen_png(self):
        """截图"""
        # 当前appiumv1.12.0版本会和uiautomator2有冲突 导致截图会卡死，所以不能用以下的方法
        # self.driver.get_screenshot_as_file("某个路径截图")

        # ----替代方案 ---
        # 定义图片名字
        png_name = "%d.png" % (int(time.time() * 1000))
        # adb方式进行截图 -截图只能保存到手机上(/sdcard/某个图片)
        os.system("adb shell screencap -p /sdcard/%s" % png_name)
        # adb 从手机在把图片拉回项目
        os.system("adb pull /sdcard/%s ./Image" % png_name)
        # 添加截图到allure测试报告中
        # 1.读取图片位置
        with open("./Image" + os.sep + png_name, "rb") as f:
            # 2.添加方法
            allure.attach(f.read(), name="截图", attachment_type=allure.attachment_type.PNG)
