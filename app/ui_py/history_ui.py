# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/history.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 470)
        Form.setStyleSheet("QFrame{\n"
"    border:1px solid red;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_7)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_12)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 5)
        self.horizontalLayout_5.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_13)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.frame_13)
        self.label_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_13)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 4)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_14 = QtWidgets.QFrame(self.frame)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.frame_15)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        self.horizontalLayout_8.setStretch(0, 4)
        self.horizontalLayout_8.setStretch(1, 5)
        self.horizontalLayout_7.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_14 = QtWidgets.QLabel(self.frame_16)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_16)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 3)
        self.label_16 = QtWidgets.QLabel(self.frame_16)
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame_16)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 4)
        self.verticalLayout.addWidget(self.frame_14)
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_18 = QtWidgets.QFrame(self.frame_17)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_17 = QtWidgets.QLabel(self.frame_18)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        self.horizontalLayout_10.setStretch(0, 4)
        self.horizontalLayout_10.setStretch(1, 5)
        self.horizontalLayout_9.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_18 = QtWidgets.QLabel(self.frame_19)
        self.label_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 1, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_19)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 0, 0, 1, 3)
        self.label_20 = QtWidgets.QLabel(self.frame_19)
        self.label_20.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.frame_19)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 4)
        self.verticalLayout.addWidget(self.frame_17)
        self.frame_20 = QtWidgets.QFrame(self.frame)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_21 = QtWidgets.QLabel(self.frame_21)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_12.addWidget(self.label_21)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_12.addWidget(self.pushButton_7)
        self.horizontalLayout_12.setStretch(0, 4)
        self.horizontalLayout_12.setStretch(1, 5)
        self.horizontalLayout_11.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_22 = QtWidgets.QLabel(self.frame_22)
        self.label_22.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 1, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_22)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 0, 0, 1, 3)
        self.label_24 = QtWidgets.QLabel(self.frame_22)
        self.label_24.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 1, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.frame_22)
        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 4)
        self.verticalLayout.addWidget(self.frame_20)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.label_10.setText(_translate("Form", "TextLabel"))
        self.label_11.setText(_translate("Form", "TextLabel"))
        self.label_12.setText(_translate("Form", "TextLabel"))
        self.label_13.setText(_translate("Form", "TextLabel"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.label_14.setText(_translate("Form", "TextLabel"))
        self.label_15.setText(_translate("Form", "TextLabel"))
        self.label_16.setText(_translate("Form", "TextLabel"))
        self.label_17.setText(_translate("Form", "TextLabel"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.label_18.setText(_translate("Form", "TextLabel"))
        self.label_19.setText(_translate("Form", "TextLabel"))
        self.label_20.setText(_translate("Form", "TextLabel"))
        self.label_21.setText(_translate("Form", "TextLabel"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
        self.label_22.setText(_translate("Form", "TextLabel"))
        self.label_23.setText(_translate("Form", "TextLabel"))
        self.label_24.setText(_translate("Form", "TextLabel"))
