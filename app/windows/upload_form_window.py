from PyQt5.QtWidgets import QWidget
from app.components.my_text_edit import MyTextEdit
from app.ui_py.upForm_ui import Ui_Form
from app.entity.goods import Goods
from app.entity.user import user, Business


class UpForm(QWidget, Ui_Form):
    def __init__(self, goods: Goods, shop: Business, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        self.text_edit = None
        self.total_price = 0
        self.nums = 1
        self.goods = goods
        self.shop = shop

        # 调用父类方法创建ui
        self.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        self.label.clicked.connect(self.change_text)
        self.label_2.clicked.connect(self.change_text)
        self.label_3.clicked.connect(self.change_text)
        self.pushButton.clicked.connect(self.dec_nums)
        self.pushButton_2.clicked.connect(self.inc_nums)
        self.pushButton_3.clicked.connect(self.submit)

        self.label.setText(user.address)
        self.label_2.setText(user.name)
        self.label_3.setText(user.phone)
        self.label_4.setText(self.shop.name)
        self.label_9.setText(self.goods.name)
        self.label_10.setText(str(self.goods.price))
        self.total_price += self.goods.price
        self.label_12.setText(str(self.total_price))

    def change_text(self, label):
        self.text_edit = MyTextEdit()
        self.text_edit.show()
        self.text_edit.closed.connect(lambda: label.setText(self.text_edit.toPlainText()))

    def inc_nums(self):
        self.nums += 1
        # todo 修改为购买多个商品的逻辑
        self.label_12.setText(str(self.total_price * self.nums))
        self.lineEdit.setText(str(self.nums))

    def dec_nums(self):
        if self.nums <= 1:
            return
        self.nums -= 1
        self.label_12.setText(str(self.total_price * self.nums))
        self.lineEdit.setText(str(self.nums))

    def submit(self):
        if self.label.text() == '':
            print('地址为空')
        elif self.label_3.text() == '':
            print('电话号码为空')
        else:
            params = {
                'user_id': user.id,
                'goods_id': self.goods.id,
                'nums': self.nums,
                'remark': self.textEdit.toPlainText()
            }
            if user.submit_indent(params):
                print('cg')
                self.close()
            else:
                print('error')
