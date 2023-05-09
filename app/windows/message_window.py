from PyQt5.QtWidgets import QWidget

from app.ui_py.message_ui import Ui_Form
from app.windows.frame import ChatFrame


class MessageWindow(QWidget, Ui_Form):
    def __init__(self, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.switch = switch
        self.chat_list = []

        # 调用父类方法创建ui
        self.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        self.listWidget.insertItem(0, '系统消息')
        self.listWidget.insertItem(1, '默认消息')
        self.stackedWidget.addWidget(ChatFrame())
        self.stackedWidget.addWidget(ChatFrame())

        self.listWidget.currentRowChanged.connect(self.display)

    def display(self, i):
        self.stackedWidget.setCurrentIndex(i+2)
