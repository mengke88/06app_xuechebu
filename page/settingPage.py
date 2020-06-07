"""
个人设置页面点击退出，点击退出后回个人中心页面
"""

from base.base import Base
from page.appElement import PageElement


class SettingPage(Base):

    def __init__(self):
        super().__init__()

    def setting_quit(self, tag=1):
        """
        退出方法
        :param tag: 1，确认退出，0取消退出
        :return:
        """
        # 点击退出按钮
        self.click_ele(PageElement.setting_logout_btn_id)
        if tag == 1:
            # 点击退出确认按钮
            self.click_ele(PageElement.setting_logout_acc_btn_id)
        if tag == 0:
            # 退出取消
            self.click_ele(PageElement.setting_logout_dis_btn_id)

        # 向下滑动,调用封装好的滑动方法，默认是1向上滑动，所以手指传入2向下滑动，页面往上
        self.swipe_screen(2)
