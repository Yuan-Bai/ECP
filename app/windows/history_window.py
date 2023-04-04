from PyQt5.QtWidgets import QWidget
from app.ui_py.history_ui import Ui_Form


class HistoryWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None

        # 调用父类方法创建ui
        self.setupUi(self)
