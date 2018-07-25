# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QLCDNumber, QSlider
from PyQt5.QtCore import pyqtSlot
from wh.algorithm import cv_experiment

class Ui_Competition(object):


    def setupUi(self, Competition):
        self.distance = 3
        self.fileName1 = ''
        self.save_image = None
        self.value1 = 391 # choose a block_size to adaptive threshold segmentation
        self.value2 = 100 # the contour size
        self.value3 = 5 # dilate size
        Competition.setObjectName("Competition")
        Competition.resize(1045, 579)
        Competition.setIconSize(QtCore.QSize(24, 24))
        Competition.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(Competition)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 241, 151))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 60, 91, 31))
        self.label_4.setObjectName("label_4")
        self.image_1 = QtWidgets.QLabel(self.centralwidget)
        self.image_1.setGeometry(QtCore.QRect(280, 110, 341, 291))
        self.image_1.setStyleSheet("")
        self.image_1.setText("")
        self.image_1.setObjectName("image_1")
        self.image_2 = QtWidgets.QLabel(self.centralwidget)
        self.image_2.setGeometry(QtCore.QRect(650, 110, 341, 291))
        self.image_2.setStyleSheet("")
        self.image_2.setText("")
        self.image_2.setObjectName("image_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(780, 60, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 54, 12))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 20, 601, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(440, 430, 360, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 500)
        self.horizontalSlider.setValue(self.value1)



        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 430, 221, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 460, 221, 16))
        self.label_7.setObjectName("label_7")
        self.horizontalSlider_2 = QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(440, 460, 360, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setRange(0, 300)
        self.horizontalSlider_2.setValue(self.value2)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 490, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(950, 20, 75, 23))
        self.pushButton_1.setObjectName("pushButton")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 490, 221, 16))
        self.label_8.setObjectName("label_8")
        self.horizontalSlider_3 = QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(440, 490, 360, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setRange(1, 30)
        self.horizontalSlider_3.setValue(self.value3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(830, 430, 41, 16))
        self.label_9.setText(str(self.value1))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(830, 460, 41, 16))
        self.label_10.setText(str(self.value2))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(830, 490, 41, 16))
        self.label_11.setText(str(self.value3))
        self.label_11.setObjectName("label_11")

        Competition.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Competition)
        self.statusbar.setObjectName("statusbar")
        Competition.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(Competition)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1045, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        Competition.setMenuBar(self.menuBar)
        self.actionOpen_one_image_file = QtWidgets.QAction(Competition)
        self.actionOpen_one_image_file.setObjectName("actionOpen_one_image_file")
        self.actionExit = QtWidgets.QAction(Competition)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_us = QtWidgets.QAction(Competition)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.actionVersion = QtWidgets.QAction(Competition)
        self.actionVersion.setObjectName("actionVersion")
        self.menu.addSeparator()
        self.menu.addAction(self.actionOpen_one_image_file)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu.addSeparator()
        self.menu_2.addAction(self.actionAbout_us)
        self.menu_2.addAction(self.actionVersion)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.retranslateUi(Competition)
        QtCore.QMetaObject.connectSlotsByName(Competition)

    def retranslateUi(self, Competition):
        _translate = QtCore.QCoreApplication.translate
        Competition.setWindowTitle(_translate("Competition", "MainWindow"))
        self.label.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">参赛学校：湖北文理学院</span></p></body></html>"))
        self.label_3.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">参赛队伍：湖文工匠</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">指导老师：朱丽娟，谢志远</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">队长：叶陈</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">队员：王恒，毛笔君</span></p></body></html>"))
        self.label_4.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">原始图像</span></p></body></html>"))
        self.label_5.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">处理后得图像</span></p></body></html>"))
        self.menu.setTitle(_translate("Competition", "File"))
        self.menu_2.setTitle(_translate("Competition", "Help"))
        self.actionOpen_one_image_file.setText(_translate("Competition", "Open one image file"))
        self.actionOpen_one_image_file.setIconText(_translate("Competition", "Open one image file"))
        self.actionExit.setText(_translate("Competition", u"打开相机"))
        self.actionAbout_us.setText(_translate("Competition", "About us"))
        self.actionVersion.setText(_translate("Competition", "Version"))
        self.label_6.setText(_translate("Competition", "adaptiveThershold blockSize"))
        self.label_7.setText(_translate("Competition", "contour size"))
        self.label_8.setText(_translate("Competition", "output dilate image size"))
        self.pushButton.setText(_translate("Competition", "保存图片"))
        self.pushButton_1.setText(_translate("Competition", "采集图像"))


    def changeDistance(self, distance):
        self.distance = distance



class Window(QMainWindow, Ui_Competition):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionOpen_one_image_file.triggered.connect(self.openFile)
        self.pushButton.clicked.connect(self.on_click)
        self.horizontalSlider_3.valueChanged.connect(self.changeValue3)
        self.horizontalSlider_2.valueChanged.connect(self.changeValue2)
        self.horizontalSlider.valueChanged.connect(self.changeValue1)

    def openFile(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件","D:/_个人文件夹/光电竞赛文档",
                                                          "All Files (*);;png Files (*.png);;text Files (*.txt);;"
                                                          "bmp Files (*.bmp);;jpg Files (*.jpg);;"
                                                          "jpeg Files (*.jpeg);;gif Files (*.gif)")
        # print(fileName1, filetype)
        # png = QtGui.QPixmap(fileName1).scaled(self.image_1.width(), self.image_1.height())
        # self.image_1.setPixmap(png)
        # self.image_2.setPixmap(png)
        self.fileName1 = fileName1
        self.showExpResu(self.fileName1)

    def on_click(self):
        if self.save_image is not None:
            cv2.imwrite("save_image.png", self.save_image)

    def showExpResu(self, fileName1):
        if fileName1 != '':
            width1 = self.image_1.width()
            height1 = self.image_1.height()
            # image = cv2.imread(fileName1)
            distance = self.get_distance()
            image = cv2.imdecode(np.fromfile(fileName1, dtype=np.uint8), -1)
            final_image = cv_experiment.entrence(fileName1, distance, self.value1, self.value2, self.value3)
            if image.data:
                resized1 = cv2.resize(image, (width1, height1), interpolation=cv2.INTER_AREA)
                pixmap1 = self.CV2QImage(resized1)
                resized2 = cv2.resize(final_image, (width1, height1), interpolation=cv2.INTER_AREA)
                pixmap2 = self.CV2QImage(resized2)
                self.save_image = resized2
                self.image_1.setPixmap(pixmap1)
                self.image_2.setPixmap(pixmap2)
            else:
                return

    def CV2QImage(self, cv_image, code = 3):
        if len(cv_image.shape) == 2:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_GRAY2BGR)
        height, width, bytesPerComponent = cv_image.shape
        bytesPerLine = code * width
        cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB, cv_image)
        QImg = QImage(cv_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        return pixmap

    def get_distance(self):
        return self.distance

    def changeValue1(self ,value):
        real_value = self.horizontalSlider.value()
        if real_value % 2 == 0:
            self.value1 = real_value + 1
        else:
            self.value1 = real_value
        self.label_9.setText(str(self.value1))
        self.showExpResu(self.fileName1)

    def changeValue2(self):
        real_value = self.horizontalSlider_2.value()
        self.value2 = real_value
        self.label_10.setText(str(self.value2))
        self.showExpResu(self.fileName1)

    def changeValue3(self):
        real_value = self.horizontalSlider_3.value()
        self.value3 = real_value
        self.label_11.setText(str(self.value3))
        self.showExpResu(self.fileName1)