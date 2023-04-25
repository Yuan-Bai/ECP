from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMainWindow
from app.settings import *
from app.switch import Switch
from app.ui_py.main_ui import Ui_MainWindow
from app.windows.history_window import HistoryWindow
from app.windows.homepage_window import HomePageWindow
from app.entity.user import User
from app.windows.verification_window import VerificationWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.scrollArea = None
        self.widget_loginArea = None
        self.widget_historyArea = None
        self.widget_registerArea = None
        self.widget_userCenter = None
        self.widget_business = None
        self.widget_becomeBusiness = None

        self.user = User()  # 有无更优雅的写法？待定
        self.user.auto_login()  # 自动登录

        # 调用父类方法创建ui
        self.setupUi(self)

        # 初始化父类自带方法后，需要初始化的变量
        self.switch = Switch(self.frame_bady)

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

        # 跳转到主页
        self.switch.switch_windows(HomePageWindow, self.user)

        # 设置搜索框占位符
        self.lineEdit_search.setPlaceholderText('搜索')

        # 设置必要按钮响应事件
        self.toolButton_close.clicked.connect(self.close)
        self.toolButton_min.clicked.connect(self.showMinimized)

        # 设置用户中心按钮
        self.pushButton_userCenter.clicked.connect(lambda: self.switch.switch_windows(VerificationWindow,
                                                                                      self.user, self.switch))

        # 设置历史记录按钮
        self.pushButton_history.clicked.connect(lambda: self.switch.switch_windows(HistoryWindow, self.user))

        # 设置首页按钮
        self.pushButton_homePage.clicked.connect(lambda: self.switch.switch_windows(HomePageWindow, self.user))

    # -*- 监听事件函数开始 -*-
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
