import time
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class MyLabel(QLabel):
    clicked = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.start_time = 0

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        start_time = round(time.time()*1000)

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        end_time = round(time.time()*1000)
        if end_time - self.start_time > 200:
            self.clicked.emit(self)
