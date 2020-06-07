"""
测试页面脚本
"""
import allure
import pytest

from base.Driver import Driver
from base.get_data import AnalysisData
from base.page import Page


class TestLogin:

    # 依赖一次用pytest.fixture(scope="class")
    @pytest.fixture(scope="class", autouse=True)
    def goto_person(self):
        """进入个人中心--依赖一次--"""
        # 关闭更新提示
        Page.get_home().close_update()
        # 点击我的
        Page.get_home().click_my_btn()

    # 每次都依赖用pytest.fixture(autouse=True)
    @pytest.fixture(autouse=True)
    def click_login_sign(self):
        """个人中心点击登录 -每次依赖"""
        Page.get_person().click_login_sigin()

    # 参数化
    @pytest.mark.parametrize("phone,passwd,toast,exp", AnalysisData.get_yaml_data("data.yaml"))
    # 这是allure描述步骤的方法
    @allure.step(title="进入登录页面操作，开始执行登录用例的测试")
    def test_login(self, phone, passwd, toast, exp):
        """
        测试登录
        :param phone:输入数据的电话号码
        :param passwd: 密码
        :param toast: 提示框，toast拼接xpath
        :param exp: 预期结果
        :return:
        """
        # 输入登录账号登录
        Page.get_login().login(phone, passwd)
        # 因为两条业务登录成功会到个人中心，然后点击设置，退出；登录失败会回到登录页面在输入，所以
        # 我们需要做判断如果有toast值为失败用例，没有则登录成功
        if toast:
            """预期失败用例"""
            # 获取toast提示信息
            message = Page.get_login().get_toast(toast)
            try:
                # 断言
                assert message == exp
            except AssertionError as e:  # 断言失败异常
                # 如果断言失败就截图,screen_png为定义好截图方法
                Page.get_setting().screen_png()
                # 抛出断言失败异常
                raise e
            finally:
                # 点击返回按钮
                Page.get_login().login_return()

        else:
            """预期成功用例"""
            # 点击登录确认，因为登录成功会弹出一个确认按钮
            Page.get_login().login_acc()
            # 获取用户名
            username = Page.get_person().get_user_name()
            try:
                # 断言
                assert username == exp
            except AssertionError as e:
                # 截图
                Page.get_setting().screen_png()
                # 抛出断言失败异常
                raise e
            finally:
                # 点击设置
                Page.get_person().click_setting_btn()
                # 退出操作
                Page.get_setting().setting_quit()

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()
