import requests
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from app.entity.user import Business
from app.ui_py.goods_buy_ui import Ui_Form

from app.settings import REVIEW_NUMS
from app.windows.frame import ReviewFrame
from app.windows.upload_form_window import UpForm


class GoodsBuyWindow(QWidget, Ui_Form):
    def __init__(self, goods, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.now_row = 0
        self.switch = switch
        self.goods = goods
        self.business = Business()
        self.business.update_by_json(goods.get_business_info())
        self.up_form = UpForm(self.goods, self.business)
        self.up_form.setWindowTitle('填写表单')

        # 调用父类方法创建ui
        self.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        # 获取评论
        self.scrollArea.verticalScrollBar().valueChanged.connect(self.handleBarValue)
        # 添加点击事件
        self.label_20.clicked.connect(self.jump_to_upForm)

        # 设置文本
        self.label_23.setText(self.business.name)
        self.label_5.setText(str(self.business.credit))
        self.label_7.setText(self.business.phone)
        self.label_9.setText(self.business.address)
        self.label_11.setWordWrap(True)
        self.label_11.setText(self.business.introduce)
        self.label_13.setWordWrap(True)
        self.label_13.setText(self.goods.introduce)
        self.label_15.setText(self.goods.name)
        self.label_17.setText(str(self.goods.price))
        self.label_19.setText(self.goods.type)

        # 设置图片
        resp = requests.get(self.goods.image_url)
        goods_photo = QPixmap()
        goods_photo.loadFromData(resp.content, "JPG")
        self.label_3.setPixmap(goods_photo)
        self.label_3.setScaledContents(True)

        resp = requests.get(self.business.image_url)
        business_photo = QPixmap()
        business_photo.loadFromData(resp.content, "JPG")
        self.label_2.setPixmap(business_photo)
        self.label_2.setScaledContents(True)

        self.get_reviews()

    def get_reviews(self):
        for row in range(self.now_row, REVIEW_NUMS+self.now_row):
            review = ReviewFrame()
            self.verticalLayout_2.addWidget(review)
        self.now_row += REVIEW_NUMS

    def handleBarValue(self, value):
        if value == self.scrollArea.verticalScrollBar().maximum():
            self.setCursor(QtGui.QCursor(Qt.WaitCursor))
            self.get_reviews()
            self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def jump_to_upForm(self):
        self.up_form.show()
