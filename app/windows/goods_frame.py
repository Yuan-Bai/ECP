from PyQt5.QtWidgets import QFrame
from app.ui_py.frame_goods_ui import Ui_Frame


class GoodsFrame(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None

        # 调用父类方法创建ui
        self.setupUi(self)
