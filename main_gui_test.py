# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from data_gui_test import DataWindow
from graph_gui_test import GraphWindow
from main_gui import *
from PyQt5.QtWidgets import QFileDialog, QAction, QMessageBox
from PyQt5.QtWidgets import QGraphicsOpacityEffect

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    def open_draw(self):
        tmp = GraphWindow(parent=self)
        tmp.show()

    def calculate(self):
        pass

    def open_data(self):
        tmp = DataWindow(parent=self)
        tmp.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
