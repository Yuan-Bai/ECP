from PyQt5.QtWidgets import QWidget

from app.entity.user import Business
from app.ui_py.become_business_ui import Ui_Form
from app.routes import req
from app.api import become_business_api
from PyQt5.QtWidgets import QFileDialog
from app.entity.user import user
from app.windows.business_window import BusinessWidow


class BecomeBusinessWindow(QWidget, Ui_Form):
    def __init__(self, switch, parent=None):
        super().__init__(parent)
        # 初始化必要变量
        self.start_x = None
        self.start_y = None
        if user.is_business:
            switch.switch_windows(BusinessWidow, user, switch)
            return
        self.switch = switch

        # 调用父类方法创建ui
        self.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        self.pushButton_2.clicked.connect(lambda: self.switch.switch_windows(BecomeBusinessWindow, user, self.switch))
        self.pushButton.clicked.connect(self.become_business)
        self.pushButton_chooseFile.clicked.connect(self.choose_file)

    def become_business(self):
        params = {
            'user_name': user.name,
            'user_pwd': user.pwd,
            'business_name': self.lineEdit_businessName.text(),
            'business_address': self.lineEdit_businessAddress.text(),
            'business_phone': self.lineEdit_business_phone.text(),
        }

        files = [
            ('files[]', (self.lineEdit_businessName.text()+'.jpg', open(self.lineEdit_businessImage.text(), 'rb'), 'image/jpeg')),
        ]
        response = req.to_python(req.request('post', become_business_api, params=params, files=files))
        if response['retCode'] != '200':
            print(response['message'])
        else:
            data = response['data']
            self.user.business = Business(address=data['address'], create_time=data['create_time'],
                                          user_id=data['user_id'], phone=data['phone'], image_url=data['image_url'],
                                          name=data['name'], id=data['id'], credit=data['credit'])
            self.user.is_business = True

    def choose_file(self):
        file_dialog = QFileDialog()
        file_dialog.setDirectory("C:/")
        file_dialog.setNameFilter("图片文件(*.jpg *.png)")
        if file_dialog.exec_():
            self.lineEdit_businessImage.setText(file_dialog.selectedFiles()[0])
