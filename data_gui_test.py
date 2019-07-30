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

        self.radioButton_5.setChecked(True)
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
                str="HYDRATE-EQUILIBRIUM\n"
            elif (self.comboBox.currentIndex()==1):
                print("选择了动力学")
                str="HYDRATE-KINETIC\n"
            print(str)
            zf=self.lineEdit.text()
            fc=self.lineEdit_2.text()
            x=self.lineEdit_3.text()
            zdwgs=self.lineEdit_4.text()
            zdljs=self.lineEdit_5.text()
            zdyhxs=self.lineEdit_6.text()
            zdjzs=self.lineEdit_7.text()
            #print("%5s%5s%5s%5s%5s\r\n"%(zf,fc,x,"0","4"))
            f1.write("Test:This is a test file by keksen\n")
            f1.write("TOUGH-Fx MEMORY ALLOCATION\n")
            f1.write(str)
            f1.write("%5s%5s%5s%5s%5s\n"%(zf,fc,x,"0","4"))
            f1.write("%10s%10s%2s\n"%(zdwgs,zdljs,"5"))
            f1.write("%5s\n"%zdyhxs)
            f1.write("%5s\n"%zdjzs)

    def file2_save(self):
        with open("file2.txt","w") as f2:
            ysmc=self.lineEdit_61.text()
            md = self.lineEdit_62.text()
            kxd = self.lineEdit_63.text()
            ki = self.lineEdit_64.text()
            kj = self.lineEdit_65.text()
            kk = self.lineEdit_66.text()
            bhltdrxs = self.lineEdit_67.text()
            brr = self.lineEdit_68.text()
            nad=""
            kxysxs = self.lineEdit_69.text()
            wbhlt = self.lineEdit_70.text()
            ljkxd = self.lineEdit_71.text()
            stljdzs = self.lineEdit_72.text()
            if (self.radioButton_5.isChecked()):
                nad="1"
            elif (self.radioButton_6.isChecked()):
                nad="0"
            f2.write("ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            f2.write("%5s%5s%10s%10s%10s%10s%10s%10s%10s\n"%(ysmc,nad,md,kxd,ki,kj,kk,bhltdrxs,brr))
            if (self.radioButton_5.isChecked()):
                f2.write("%10s%20s%40s%10s\n"%(kxysxs,wbhlt,ljkxd,stljdzs))

    def file3_save(self):
        with open("file3.txt","w") as f3:
            drxs = self.lineEdit_76.text()
            brxs = self.lineEdit_77.text()
            shwmd = self.lineEdit_78.text()

            t_maxoff = self.lineEdit_79.text()
            c_maxoff = self.lineEdit_80.text()
            mw_maxoff = self.lineEdit_81.text()
            d_inhib = self.lineEdit_82.text()
            h_inhsol = self.lineEdit_83.text()
            difco_inhib = self.lineEdit_84.text()

            f3.write("HYDRATE--1----*-Modified Chlorobenzene data-*----5----*----6----*----7----*----8\n")
            f3.write("%6s\n"%"1")
            f3.write("'CH4'  6.0d0 1.00d00\n")
            f3.write("%6s\n" % "1")
            f3.write("%8s\n" %drxs)
            f3.write("%6s\n" % "1")
            f3.write("%8s\n" % brxs)
            f3.write("%6s\n" % "1")
            f3.write("%8s\n" % shwmd)
            f3.write("%5s%8s%9s%6s%10s%7s\n"%(t_maxoff,c_maxoff,mw_maxoff,d_inhib,h_inhsol,difco_inhib))
            if (self.comboBox_4.currentIndex()==0):
                f3.write("0\n")
            elif (self.comboBox_4.currentIndex()==1):
                f3.write("1\n")
            elif (self.comboBox_4.currentIndex()==2):
                f3.write("2\n")

            if (self.comboBox_5.currentIndex()==0):
                f3.write("HYDRATE-EQUILIBRIUM\n")
            elif (self.comboBox_5.currentIndex()==1):
                f3.write("HYDRATE-KINETIC\n")
                hhn = self.lineEdit_9.text()
                gysl = self.lineEdit_31.text()
                bmyz = self.lineEdit_32.text()
                f3.write("%5s%8s%8s\n"%(hhn,gysl,bmyz))

    def file4_save(self):
        with open("file4.txt","w") as f4:
            cov = self.lineEdit_44.text()
            mop = self.lineEdit_45.text()
            start = self.lineEdit_46.text()
            end = self.lineEdit_47.text()
            min_time = self.lineEdit_48.text()
            max_time = self.lineEdit_49.text()
            init = self.lineEdit_50.text()
            first = self.lineEdit_40.text()
            second = self.lineEdit_41.text()
            third = self.lineEdit_42.text()
            fourth = self.lineEdit_43.text()
            f4.write("START----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            f4.write("----*----1 MOP: 123456789*123456789*1234 ---*----5----*----6----*----7----*----8\n")
            f4.write("PARAM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            f4.write("%4s%4s%8s%24s%10s\n"%("3","9999",cov,mop,"0.00E-5"))
            f4.write("%10s%10s%10s%10s%20s\n"%(start,end,min_time,max_time,"9.8060"))
            f4.write("%10s%10s%40s%15s\n"%("1.E-5","1.E00","1.0e-8",init))
            f4.write("%20s%20s%20s%20s\n"%(first,second,third,fourth))

    # ！！！------file5相关没有完成
    def file5_save(self):
        # 等会再回来写7.30
        # 没有考虑好这部分应该怎么处理
        if (self.radioButton.isChecked()):
            print("笛卡尔坐标")
            with open("file5_tmp.txt","w") as f5:
                f5.write("Input file for a test\n")
                f5.write("")
        elif (self.radioButton_2.isChecked()):
            print("柱坐标")

    def file6_save(self):
        with open("file6.txt","w") as f6:
            xdstl = self.lineEdit_33.text()
            sfs = self.lineEdit_34.text()
            sfq = self.lineEdit_35.text()
            xsxs = self.lineEdit_36.text()
            mgl = self.lineEdit_37.text()
            csn = self.lineEdit_33.text()
            csa = self.lineEdit_33.text()
            f6.write("RPCAP----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            f6.write("%5s%15s%10s%10s%10s\n"%("6",sfs,"0.05",sfq,xsxs))
            f6.write("%5s%15.3f%10s%10s%10s\n"%("8",float(sfs)-0.01,csn,csa,"11"))

    def file7_8_save(self):
        with open("file7.txt","w") as f7:
            pass
        with open("file8.txt","w") as f8:
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
