from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class FirstUI(QWidget):
    first = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(FirstUI, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.but = QPushButton('first', self)
        self.but.resize(100, 40)
        self.but.move(100, 100)
        self.but.clicked.connect(self.but_clicked)

    def but_clicked(self):
        self.first.emit('first')
        self.close()


class SecondUi(QWidget):
    second = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(SecondUi, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.but = QPushButton('second', self)
        self.but.resize(100, 40)
        self.but.move(100, 100)
        self.but.clicked.connect(self.but_clicked)

    def but_clicked(self):
        self.second.emit('second')
        self.close()


class MainWindow:
    def first(self):
        self.firstui = FirstUI()
        self.firstui.first.connect(self.second)
        self.firstui.show()

    def second(self, st):
        print(st)
        self.secondui = SecondUi()
        self.secondui.second.connect(self.first)
        self.secondui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = MainWindow()
    ma.first()
    sys.exit(app.exec_())  # app.exet_()是指程序一直循环运行直到主窗口被关闭终止进程（如果没有这句话，程序运行时会一闪而过）

