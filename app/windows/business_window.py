from PyQt5.QtWidgets import QWidget, QFileDialog

from app.api import upload_goods_api
from app.entity.user import user
from app.routes import req
from app.ui_py.business_ui import Ui_Form


class BusinessWidow(QWidget, Ui_Form):
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
        self.comboBox.addItems(['手机', '电脑', '裤子', '衣服', '手表', '牙膏', '显卡', '书籍', '食品'])
        self.label.clicked.connect(self.upload_goods)
        self.label_2.clicked.connect(self.choose_file)

    def upload_goods(self):
        params = {
            'goods_name': self.lineEdit.text(),
            'business_id': user.business.id,
            'goods_price': self.lineEdit_2.text(),
            'goods_amount': self.lineEdit_3.text(),
            'goods_introduce': self.lineEdit_4.text(),
            'goods_type': self.comboBox.currentText()
        }
        print(params)
        files = [
            ('files[]', (self.lineEdit.text() + '.jpg', open(self.lineEdit_5.text(), 'rb'), 'image/jpeg')),
        ]

        response = req.to_python(req.request('post', upload_goods_api, params=params, files=files))
        data = req.get_data(response)
        print(data)

    def choose_file(self):
        file_dialog = QFileDialog()
        file_dialog.setDirectory("C:/")
        file_dialog.setNameFilter("图片文件(*.jpg *.png)")
        if file_dialog.exec_():
            self.lineEdit_5.setText(file_dialog.selectedFiles()[0])
