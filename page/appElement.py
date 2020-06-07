"""
该界面为用例基本操作对象的定位
"""
from selenium.webdriver.common.by import By


class PageElement:
    """首页"""
    # 更新取消按钮
    home_update_dis_btn_xpath = (By.XPATH, "//*[contains(@text,'稍后更新')]")
    # 我的
    home_my_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/mine_layout")

    """个人中心"""
    # 登录/注册
    person_login_sigin_btn_xpath = (By.XPATH, "//*[contains(@text,'登录/注册')]")
    # 用户名
    person_username_id = (By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv")
    # 设置
    person_setting_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/mine_set_rl")

    """登录页面"""
    # 返回按钮
    login_return_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/title_back")
    # 账号
    login_account_id = (By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et")
    # 密码
    login_passwd_id = (By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et")
    # 登录按钮
    login_sub_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/login_btn")
    # 登录成功确认
    login_suc_acc_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/btn_neg")

    """设置页面"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/set_logout_tv")
    # 退出确认
    setting_logout_acc_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/bt_ok")
    # 退出取消
    setting_logout_dis_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/bt_no")
