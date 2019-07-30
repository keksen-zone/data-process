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


    def load_file1(self):
        pass
    def load_file2(self):
        pass
    def load_file3(self):
        pass
    def load_file4(self):
        pass
    def load_file5(self):
        pass
    def load_file6(self):
        pass
    def load_file7_8(self):
        pass
    def load_file9(self):
        pass
    def load_file10(self):
        pass

    def file1_save(self):
        with open("file1.txt",'w') as f1:
            str=""
            if (self.comboBox.currentIndex()==0):
                print("选择了平衡")
                str="HYDRATE-EQUILIBRIUM"
            elif (self.comboBox.currentIndex()==1):
                print("选择了动力学")
                str="HYDRATE-KINETIC"
            print(str)
            f1.write("%5d%5d%5d%5d%5d\r\n"%())
    def file2_save(self):
        pass
    def file3_save(self):
        pass
    def file4_save(self):
        pass
    def file5_save(self):
        pass
    def file6_save(self):
        pass
    def file7_8_save(self):
        pass
    def file9_save(self):
        pass
    def file10_save(self):
        pass
    def make_mesh(self):
        pass
    def exit_data(self):
        pass
    def combine_all_files(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = DataWindow()
    myWin.show()
    sys.exit(app.exec_())
