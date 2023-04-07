# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/static/ui/frame_goods.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(190, 226)
        Frame.setMinimumSize(QtCore.QSize(190, 226))
        Frame.setMaximumSize(QtCore.QSize(190, 226))
        Frame.setStyleSheet("QWidget{\n"
"    border:1px solid red;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_image_box = QtWidgets.QFrame(Frame)
        self.frame_image_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_box.setObjectName("frame_image_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_image_box)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame_images = QtWidgets.QFrame(self.frame_image_box)
        self.frame_images.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_images.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_images.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_images.setObjectName("frame_images")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_images)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_images)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_images)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.frame_image_box)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.frame_info = QtWidgets.QFrame(Frame)
        self.frame_info.setEnabled(True)
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_name = QtWidgets.QLabel(self.frame_info)
        self.label_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.label_blank = QtWidgets.QLabel(self.frame_info)
        self.label_blank.setText("")
        self.label_blank.setObjectName("label_blank")
        self.verticalLayout.addWidget(self.label_blank)
        self.label_price = QtWidgets.QLabel(self.frame_info)
        self.label_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_price.setObjectName("label_price")
        self.verticalLayout.addWidget(self.label_price)
        self.verticalLayout_2.addWidget(self.frame_info)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 15)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.frame_info.raise_()
        self.frame_image_box.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_name.setText(_translate("Frame", "name"))
        self.label_price.setText(_translate("Frame", "price"))