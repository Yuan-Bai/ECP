from PyQt5.QtWidgets import QWidget
from app.switch import Switch
from app.ui_py.verification_ui import Ui_Form
from app.windows.frame import LoginFrame
from app.windows.user_center_window import UserCenterWindow


class VerificationWindow(QWidget, Ui_Form):
    def __init__(self, user, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.user = user
        # 判断是否登录
        if self.user.is_login:
            # self.hide()
            switch.switch_windows(UserCenterWindow, self.user, switch)
            return
        self.switch = switch

        # 调用父类方法创建ui
        self.setupUi(self)

        # 初始化switch
        self.login_signup_switch = Switch(self.frame_login_and_signup)

        # 对父类ui进行修改
        self.setup_ui()

    def setup_ui(self):
        self.login_signup_switch.switch_windows(LoginFrame, self.user, self.login_signup_switch, self.switch)
