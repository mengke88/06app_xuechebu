"""
个人中心页面，点击登录注册，登录成功后返回用户名，并提供向下滑动点击设置
"""
from base.base import Base
from page.appElement import PageElement


class PersonPage(Base):

    def __init__(self):
        super().__init__()

    def click_login_sigin(self):
        """点击登录注册"""
        self.click_ele(PageElement.person_login_sigin_btn_xpath)

    def get_user_name(self):
        """获取用户名"""
        return self.search_ele(PageElement.person_username_id).text

    def click_setting_btn(self):
        """点击设置"""
        # 手指往上滑，让页面上滑，swiipe_screen()为base类封装的滑动方法，默认是1，向上滑动
        self.swipe_screen()
        # 点击设置
        self.click_ele(PageElement.person_setting_btn_id)
