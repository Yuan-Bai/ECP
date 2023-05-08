from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from app.api import login_api
from app.routes import req
from app.ui_py.frame_goods_ui import Ui_Frame as Fgu
from app.ui_py.frame_maindisplay_ui import Ui_Frame as Fmu
from app.ui_py.frame_register_ui import Ui_Frame as Fru
from app.ui_py.frame_login_ui import Ui_Frame as Flu
from app.windows.goods_buy_window import GoodsBuyWindow
from app.windows.user_center_window import UserCenterWindow


class GoodsFrame(QFrame, Fgu):
    def __init__(self, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.switch = switch

        # 调用父类方法创建ui
        self.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        self.label.clicked.connect(self.to_buy)

    def to_buy(self):
        self.switch.switch_windows(GoodsBuyWindow, self.switch)


class MainDisplayFrame(QFrame, Fmu):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None

        # 调用父类方法创建ui
        self.setupUi(self)


class RegisterFrame(QFrame, Fru):
    def __init__(self, user, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.user = user
        self.switch = switch

        # 调用父类方法创建ui
        self.setupUi(self)
        # 修改ui
        self.setup_ui()

    def setup_ui(self):
        self.pushButton_toLogin.clicked.connect(lambda: self.switch.switch_windows(LoginFrame,
                                                                                   self.user, self.switch))
        self.pushButton_register.clicked.connect(self.register)

    def register(self):
        self.setCursor(QtGui.QCursor(Qt.WaitCursor))
        pwd = self.lineEdit_2.text()
        if pwd != self.lineEdit_3.text():
            print('密码不一致')
            self.setCursor(QtGui.QCursor(Qt.ArrowCursor))
            return False
        self.user.pwd = pwd
        self.user.name = self.lineEdit.text()
        self.user.register()
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))


class LoginFrame(QFrame, Flu):
    def __init__(self, user, login_signup_switch, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.user = user
        self.login_signup_switch = login_signup_switch
        self.switch = switch

        # 调用父类方法创建ui
        self.setupUi(self)
        # 修改ui
        self.setup_ui()

    def setup_ui(self):
        self.pushButton_toRegister.clicked.connect(
            lambda: self.login_signup_switch.switch_windows(RegisterFrame, self.user, self.login_signup_switch)
        )
        self.pushButton_login.clicked.connect(self.login)

    def login(self):
        self.setCursor(QtGui.QCursor(Qt.WaitCursor))
        self.user.name = self.lineEdit.text()
        self.user.pwd = self.lineEdit_2.text()
        params = {
            'name': self.user.name,
            'pwd': self.user.pwd
        }
        resp = req.to_python(req.request('post', login_api, params=params, timeout=3))
        data = req.get_data(resp)
        self.user.update_by_json(data)
        if self.user.is_login:
            # 调用父类属性切换窗口
            self.switch.switch_windows(UserCenterWindow, self.user, self.switch)
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

