# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wdget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class Ui_ChooseDirection(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ChooseDirection")
        self.setSizeIncrement(454, 193)
        self.verticalLayoutWidget = QtWidgets.QWidget()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 441, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(ChooseDirection)
        self.pushButton.setGeometry(QtCore.QRect(240, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ChooseDirection)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(ChooseDirection)
        QtCore.QMetaObject.connectSlotsByName(ChooseDirection)

    def retranslateUi(self, ChooseDirection):
        _translate = QtCore.QCoreApplication.translate
        ChooseDirection.setWindowTitle(_translate("ChooseDirection", "Form"))
        self.radioButton_5.setText(_translate("ChooseDirection", "5cm"))
        self.radioButton_4.setText(_translate("ChooseDirection", "4cm"))
        self.radioButton_3.setText(_translate("ChooseDirection", "3cm"))
        self.radioButton.setText(_translate("ChooseDirection", "2cm"))
        self.radioButton_2.setText(_translate("ChooseDirection", "1cm"))
        self.pushButton.setText(_translate("ChooseDirection", "ok"))
        self.pushButton_2.setText(_translate("ChooseDirection", "cancle"))
