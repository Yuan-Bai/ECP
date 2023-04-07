import requests
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QFrame, QMainWindow
from app.settings import *
from app.ui_py.main_ui import Ui_MainWindow
from app.utils import AREA
from app.windows.goods_frame import GoodsFrame
from app.windows.history_window import HistoryWindow
from app.windows.login_window import LoginWindow
from app.api import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.widget_loginArea = None
        self.widget_historyArea = None
        self.flag_area = 'HomePage'  # 标记当前页面
        self.now_row = 0

        # 调用父类方法创建ui
        self.setupUi(self)

        # 对父类ui的修改添加到此处
        # 整体修改
        self.resize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框
        # 组件修改
        self.setup_ui()

    def setup_ui(self):
        # 为frame设置阴影
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 0)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0))
        self.frame_top.setGraphicsEffect(shadow)

        # 重设置frame子组件占比
        self.verticalLayout.setStretch(1, F_RATIO)

        # 为滚动区域滚动条添加监听事件，以增加商品展示行数
        self.scrollArea.verticalScrollBar().valueChanged.connect(self.handleBarValue)

        # 添加轮播区域和商品
        rotation = QFrame()
        rotation.setObjectName('frame_rotation')
        self.gridLayout.addWidget(rotation, 0, 0, ROTATION_ROW, ROTATION_COL)
        self.addGoods()

        # 初始化“切换窗口”并隐藏
        self.widget_historyArea = HistoryWindow(self.frame_bady)
        self.horizontalLayout_2.insertWidget(0, self.widget_historyArea, FDA_RATIO)
        self.widget_historyArea.hide()

        # 设置搜索框占位符
        self.lineEdit_search.setPlaceholderText('搜索')

        # 设置必要按钮响应事件
        self.toolButton_close.clicked.connect(self.close)
        self.toolButton_min.clicked.connect(self.showMinimized)

        # 设置用户中心按钮
        self.pushButton_userCenter.clicked.connect(self.switch_login_window)

        # 设置历史记录按钮
        self.pushButton_history.clicked.connect(self.switch_history_window)

        # 设置首页按钮
        self.pushButton_homePage.clicked.connect(self.switch_homepage_window)

    # todo 添加请求
    def addGoods(self):
        index = 0
        for row in range(self.now_row, self.now_row+ROW):
            for col in range(COL):
                if row < ROTATION_ROW and col < ROTATION_COL:
                    continue
                frame = GoodsFrame()
                frame.setObjectName('frame_goods_'+str(index))
                # resp = requests.get(goods_image_api)
                # resp1 = requests.get(resp.text)
                # photo = QPixmap()
                # photo.loadFromData(resp1.content, "JPG")
                # frame.label.setPixmap(photo)
                # frame.label.setScaledContents(True)
                self.gridLayout.addWidget(frame, row, col, 1, 1)
                index += 1
        self.now_row += ROW

    # -*- 监听事件函数开始 -*-
    def handleBarValue(self, value):
        if value == self.scrollArea.verticalScrollBar().maximum():
            self.setCursor(QtGui.QCursor(Qt.WaitCursor))
            self.addGoods()
            self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            super(MainWindow, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(MainWindow, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except Exception:
            pass
    # -*- 监听事件函数结束 -*-

    def switch_login_window(self):
        self.widget_loginArea = LoginWindow()
        self.widget_loginArea.show()

    def switch_history_window(self):
        if self.flag_area != AREA.History:
            self.flag_area = AREA.History
            self.scrollArea.hide()
            self.widget_historyArea.show()

    def switch_homepage_window(self):
        if self.flag_area != AREA.HomePage:
            self.flag_area = AREA.HomePage
            self.widget_historyArea.hide()
            self.scrollArea.show()

    def update(self) -> None:
        pass
