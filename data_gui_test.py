# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from data_gui import *
from PyQt5.QtWidgets import QFileDialog, QAction, QMessageBox
from PyQt5.QtWidgets import QGraphicsOpacityEffect

class DataWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DataWindow, self).__init__(parent)
        self.setupUi(self)

        # self.radioButton_2.setChecked(True)
        # self.radioButton_3.setChecked(True)
        # self.radioButton_6.setChecked(True)
        # self.radioButton_8.setChecked(True)
        #
        # self.actionPlot_Data.triggered.connect(self.open_Plot_Data)
        # self.actionPlot_Coord.triggered.connect(self.open_Plot_Coord)
        # self.actionSS_Time_Series.triggered.connect(self.open_SS_Time_Series)
        # self.actionHydrate_Info.triggered.connect(self.open_Hydrate_Info)
        #
        # self.action.triggered.connect(self.data_extract)


    # def pmt_clicked(self):
    #
    # def pmt2_clicked(self):
    #
    # def open_Plot_Data(self):
    #
    # def open_Plot_Coord(self):
    #
    # def open_SS_Time_Series(self):
    #
    # def open_Hydrate_Info(self):
    #
    # def data_extract(self):
    #
    # def data_exist(self):
    #
    # def hpj(self):
    #
    #
    # def h3d(self):
    #
    # def hqx(self):
    #
    # def hpm(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = DataWindow()
    myWin.show()
    sys.exit(app.exec_())
