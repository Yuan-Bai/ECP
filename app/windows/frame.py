from PyQt5.QtWidgets import QFrame
from app.ui_py.frame_goods_ui import Ui_Frame as Fgu
from app.ui_py.frame_maindisplay_ui import Ui_Frame as Fmu
from app.ui_py.frame_register_ui import Ui_Frame as Fru


class GoodsFrame(QFrame, Fgu):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None

        # 调用父类方法创建ui
        self.setupUi(self)


class MainDisplayFrame(QFrame, Fmu):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None

        # 调用父类方法创建ui
        self.setupUi(self)


class RegisterFrame(QFrame, Fru):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None

        # 调用父类方法创建ui
        self.setupUi(self)
