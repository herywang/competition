# -*- coding: utf-8 -*-
'''
    python file describe:
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from wh.PUI.Main_window import Window
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.setFixedSize(1045, 580)
    ui.show()
    sys.exit(app.exec_())