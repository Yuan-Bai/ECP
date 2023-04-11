from PyQt5.QtWidgets import QWidget
from app.ui_py.user_center_ui import Ui_Form
from app.routes import *


class UserCenterWindow(QWidget, Ui_Form):
    def __init__(self, user, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.user = user

        # 调用父类方法创建ui
        self.setupUi(self)

    def setup_ui(self):
        self.label_becomeBusiness.clicked.connect(self.become_business)

    def become_business(self):
        become_business(self.user)
        self.user.is_business = True
