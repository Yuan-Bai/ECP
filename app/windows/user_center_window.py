from PyQt5.QtWidgets import QWidget
from app.ui_py.user_center_ui import Ui_Form
from app.windows.become_business_window import BecomeBusinessWindow
from app.windows.message_window import MessageWindow


class UserCenterWindow(QWidget, Ui_Form):
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
        self.label_becomeBusiness.clicked.connect(
            lambda: self.switch.switch_windows(BecomeBusinessWindow, self.switch)
        )
        self.label_28.clicked.connect(
            lambda: self.switch.switch_windows(MessageWindow, self.switch)
        )
