from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QTextEdit


class MyTextEdit(QTextEdit):
    closed = pyqtSignal(object)
    entered = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.start_time = 0

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.closed.emit(self)

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:  # 如果是Enter 按钮
            self.entered.emit(self)

