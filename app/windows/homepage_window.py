import requests
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame
from app.entity.goods import get_goods_list
from app.settings import COL, ROW
from app.ui_py.homepage_ui import Ui_Frame
from app.windows.frame import MainDisplayFrame, GoodsFrame


class HomePageWindow(QFrame, Ui_Frame):
    def __init__(self, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.now_row = 1
        self.switch = switch

        # 调用父类方法创建ui
        self.setupUi(self)
        # 调用自己的方法创建或修改ui
        self.setup_ui()

    def setup_ui(self):
        # 为滚动区域滚动条添加监听事件，以增加商品展示行数
        self.scrollArea.verticalScrollBar().valueChanged.connect(self.handleBarValue)

        # 添加主要展示界面和商品
        main_display = MainDisplayFrame()
        main_display.setObjectName('main_display')
        self.gridLayout.addWidget(main_display, 0, 0, 1, COL)
        self.addGoods()

    # todo 添加请求
    def addGoods(self):
        index = 0
        goods_list = get_goods_list()
        for row in range(self.now_row, self.now_row+ROW):
            for col in range(COL):
                frame = GoodsFrame(self.switch)
                # frame.setObjectName('frame_goods_'+str(index))
                goods = goods_list[index]
                resp = requests.get(goods.image_url)
                photo = QPixmap()
                photo.loadFromData(resp.content, "JPG")
                frame.label.setPixmap(photo)
                frame.label.setScaledContents(True)
                self.gridLayout.addWidget(frame, row, col, 1, 1)
                index += 1
        self.now_row += ROW

    def handleBarValue(self, value):
        if value == self.scrollArea.verticalScrollBar().maximum():
            self.setCursor(QtGui.QCursor(Qt.WaitCursor))
            self.addGoods()
            self.setCursor(QtGui.QCursor(Qt.ArrowCursor))
