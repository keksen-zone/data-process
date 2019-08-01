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
        reply = QMessageBox.question(self, '即将调用主程序进行模拟', '目录下是否已存在所需input文件\n（建议手动对input文件进行检查以防止出错）', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            os.system("main.exe")
        else:
            pass

    def open_data(self):
        tmp = DataWindow(parent=self)
        tmp.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
