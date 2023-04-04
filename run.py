import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from app.windows.main_window import MainWindow
from app import utils


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setStyleSheet(utils.read_file('./app/static/qss/style.qss'))
    main_window.setWindowIcon(QIcon("./app/static/icons/title/windowIcon.png"))
    main_window.show()
    sys.exit(app.exec_())
