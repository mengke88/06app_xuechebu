"""
app首页业务，关闭更新按钮，并点击”我的“进入登录页面
"""
from base.base import Base
from page.appElement import PageElement


class HomePage(Base):

    def __init__(self):
        super().__init__()

    def close_update(self):
        """关闭更新按钮"""
        try:
            self.click_ele(PageElement.home_update_dis_btn_xpath)
        except Exception:
            print("当前版本没有更新的版本")

    def click_my_btn(self):
        """点击我的"""
        self.click_ele(PageElement.home_my_btn_id)