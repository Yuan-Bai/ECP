from PyQt5.QtWidgets import QWidget
from app.ui_py.goods_buy import Ui_Form


class GoodsBuyWindow(QWidget, Ui_Form):
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
        pass
