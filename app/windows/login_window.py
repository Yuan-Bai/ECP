import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from app.ui_py.login_ui import Ui_Form
from app.routes import *
from app.windows.frame import RegisterFrame


class LoginWindow(QWidget, Ui_Form):
    def __init__(self, user, switch_user_center, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.frame_register = None
        self.user = user
        self.flag_area = 'login'
        self.switch_user_center = switch_user_center

        # 调用父类方法创建ui
        self.setupUi(self)
        self.setup_ui()

        self.area_dict = {
            'login': self.frame_login,
            'register': self.frame_register
        }

    def setup_ui(self):
        self.frame_register = RegisterFrame()
        self.horizontalLayout_3.insertWidget(1, self.frame_register, 1)
        self.frame_register.hide()

        self.pushButton_toRegister.clicked.connect(self.switch_register_frame)
        self.pushButton_login.clicked.connect(lambda: self.login())

        self.frame_register.pushButton_toLogin.clicked.connect(self.switch_login_frame)
        self.frame_register.pushButton_register.clicked.connect(self.register)

    def login(self):
        self.setCursor(QtGui.QCursor(Qt.WaitCursor))
        self.user.name = self.lineEdit.text()
        self.user.pwd = self.lineEdit_2.text()
        user_json = login(self.user)
        if user_json:
            self.user.is_login = True
            # todo
            self.user.pwd = user_json['pwd']
            self.switch_user_center()
            print('登录成功')
        else:
            self.user.is_login = False
            print('登录失败')
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def register(self):
        self.setCursor(QtGui.QCursor(Qt.WaitCursor))
        self.setCursor(QtGui.QCursor(Qt.WaitCursor))
        self.user.pwd = self.frame_register.lineEdit_2.text()
        if self.user.pwd != self.frame_register.lineEdit_3.text():
            print('密码不一致')
            self.setCursor(QtGui.QCursor(Qt.ArrowCursor))
            return False
        self.user.name = self.frame_register.lineEdit.text()
        if register(self.user) == 'success':
            print('注册成功')
        else:
            print('注册失败')
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def switch_register_frame(self):
        if self.flag_area != 'register':
            self.frame_login.hide()
            self.frame_register.show()
            self.flag_area = 'register'

    def switch_login_frame(self):
        if self.flag_area != 'login':
            self.frame_register.hide()
            self.frame_login.show()
            self.flag_area = 'login'

