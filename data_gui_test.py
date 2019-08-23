# -*- coding: utf-8 -*-
import os
import sys
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow
from data_gui import *
from PyQt5.QtWidgets import QFileDialog, QAction, QMessageBox
from PyQt5.QtWidgets import QGraphicsOpacityEffect

class DataWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DataWindow, self).__init__(parent)
        self.setupUi(self)

        self.radioButton_5.setChecked(True)
        self.plainTextEdit_4.setPlainText("这部分的功能尚未实现\n请手动打开文件进行操作")

    def load_file1(self):
        if (os.path.exists("file1.txt")):
            print("file1 founded")
            os.system("notepad file1.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file1.txt', QMessageBox.Yes)
    def load_file2(self):
        if (os.path.exists("file2.txt")):
            os.system("notepad file2.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file2.txt', QMessageBox.Yes)
    def load_file3(self):
        if (os.path.exists("file3.txt")):
            os.system("notepad file3.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file3.txt', QMessageBox.Yes)
    def load_file4(self):
        if (os.path.exists("file4.txt")):
            os.system("notepad file4.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file4.txt', QMessageBox.Yes)
    def load_file5(self):
        if (os.path.exists("mesh.txt")):
            os.system("notepad file5.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件mesh.txt', QMessageBox.Yes)
    def load_file6(self):
        if (os.path.exists("file6.txt")):
            os.system("notepad file6.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file6.txt', QMessageBox.Yes)
    def load_file7(self):
        if (os.path.exists("file7.txt")):
            os.system("notepad file7.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file7.txt', QMessageBox.Yes)
    def load_file8(self):
        if (os.path.exists("file8.txt")):
            os.system("notepad file8.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file8.txt', QMessageBox.Yes)
    def load_file9(self):
        if (os.path.exists("file9.txt")):
            os.system("notepad file9.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file9.txt', QMessageBox.Yes)
    def load_file10(self):
        if (os.path.exists("file10.txt")):
            os.system("notepad file10.txt")
        else:
            QMessageBox.information(self, '打开失败', '未找到文件file10.txt', QMessageBox.Yes)

    # 注意：对于柱坐标的处理尚未完成
    def zzb_add(self): # pushbutton8
        with open("zzb1.txt","a") as zzb1:
            qymc = self.lineEdit_21.text()
            rmin = self.lineEdit_25.text()
            rmax = self.lineEdit_24.text()
            zmin = self.lineEdit_26.text()
            zmax = self.lineEdit_27.text()
            zzb1.write("'%s'\n"%qymc)
            zzb1.write("'cylindrical'   'm'\n")
            zzb1.write("%s %s %s %s\n"%(rmin,rmax,zmin,zmax))
            self.lineEdit_21.clear()
            self.lineEdit_25.clear()
            self.lineEdit_24.clear()
            self.lineEdit_26.clear()
            self.lineEdit_27.clear()
            self.plainTextEdit_2.clear()
        with open("zzb1.txt", "r") as zzb1_read:
            zzb1_text = zzb1_read.readlines()
            print(zzb1_text)
            for line in zzb1_text:
                line = line.replace("\n", "")
                self.plainTextEdit_2.appendPlainText(line)
    def zzb_ano_add(self): # pushbutton 11
        # 这里的功能尚未实现
        with open("zzb2.txt","a") as zzb2:
            pass
    def zzb_save(self): # pushbuttton9
        with open("zzb1.txt","w") as dke1:
            text = self.plainTextEdit_2.toPlainText()
            print("save test:")
            print(text)
            dke1.write(text)
    def zzb_ano_save(self): # pushbutton10
        # 这里的功能尚未实现
        pass

    def dke_add(self):
        with open("dke1.txt","a") as dke1:
            qymc = self.lineEdit_11.text()
            xmin = self.lineEdit_12.text()
            xmax = self.lineEdit_13.text()
            ymin = self.lineEdit_14.text()
            ymax = self.lineEdit_15.text()
            zmin = self.lineEdit_16.text()
            zmax = self.lineEdit_17.text()
            dke1.write("'%s'\n"%qymc)
            dke1.write("'cartesian'     'm'\n")
            dke1.write("%s %s %s %s %s %s\n"%(xmin,xmax,ymin,ymax,zmin,zmax))
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
            self.lineEdit_13.clear()
            self.lineEdit_14.clear()
            self.lineEdit_15.clear()
            self.lineEdit_16.clear()
            self.lineEdit_17.clear()

            self.plainTextEdit.clear()  # ————————————————！！！！假设每次添加后都立即修改并保存————————
        with open("dke1.txt","r") as dke1_read:
            dke1_text = dke1_read.readlines()
            print(dke1_text)
            for line in dke1_text:
                line = line.replace("\n","")
                self.plainTextEdit.appendPlainText(line)
    def dke_ano_add(self):
        with open("dke2.txt", "a") as dke2:
            fx = self.lineEdit_94.text()
            wgs = self.lineEdit_18.text()
            wgcd = self.lineEdit_19.text()
            dke2.write("%s%8s%10s\n"%(fx,wgs,wgcd))
            self.lineEdit_18.clear()
            self.lineEdit_19.clear()
            self.lineEdit_94.clear()
        self.plainTextEdit_3.clear()  # ————————————————！！！！假设每次添加后都立即修改并保存————————
        with open("dke2.txt","r") as dke2_read:
            dke2_text = dke2_read.readlines()
            print(dke2_text)
            for line in dke2_text:
                line = line.replace("\n","")
                self.plainTextEdit_3.appendPlainText(line)
    def dke_save(self):
        with open("dke1.txt","w") as dke1:
            text = self.plainTextEdit.toPlainText()
            print("save test:")
            print(text)
            dke1.write(text)
    def dke_ano_save(self):
        with open("dke2.txt","w") as dke2:
            text = self.plainTextEdit_3.toPlainText()
            print("save test:")
            print(text)
            dke2.write(text)
    def make_mesh(self):
        reply = QMessageBox.question(self, '即将生成网格', '目录下是否已存在mesh.txt', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            shutil.copy("mesh.txt","mesh_in.txt")
            os.rename("mesh_in.txt","mesh.dat")
            os.system("MeshMaker.exe<mesh.dat>out")
            QMessageBox.information(self, '已完成', '网格已生成完成\n建议打开输出文件以确认', QMessageBox.Yes)
            shutil.copy("MESH", "file5.txt")
        else:
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
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        QMessageBox.information(self, '已完成', '数据保存到file6.txt\n建议打开生成文件以确认', QMessageBox.Yes)

    def rock_add(self):
        with open("rock.txt","a") as rock:
            ysmc = self.lineEdit_61.text()
            md = self.lineEdit_62.text()
            kxd = self.lineEdit_63.text()
            ki = self.lineEdit_64.text()
            kj = self.lineEdit_65.text()
            kk = self.lineEdit_66.text()
            bhltdrxs = self.lineEdit_67.text()
            brr = self.lineEdit_68.text()
            nad = ""
            kxysxs = self.lineEdit_69.text()
            wbhlt = self.lineEdit_70.text()
            ljkxd = self.lineEdit_71.text()
            stljdzs = self.lineEdit_72.text()
            if (self.radioButton_5.isChecked()):
                nad = "1"
            elif (self.radioButton_6.isChecked()):
                nad = "0"
            rock.write("%5s%5s%10s%10s%10s%10s%10s%10s%10s\n" % (ysmc, nad, md, kxd, ki, kj, kk, bhltdrxs, brr))
            if (self.radioButton_5.isChecked()):
                rock.write("%10s%20s%40s%10s\n" % (kxysxs, wbhlt, ljkxd, stljdzs))

        self.lineEdit_61.clear()
        self.lineEdit_62.clear()
        self.lineEdit_63.clear()
        self.lineEdit_64.clear()
        self.lineEdit_65.clear()
        self.lineEdit_66.clear()
        self.lineEdit_67.clear()
        self.lineEdit_68.clear()
        self.lineEdit_69.clear()
        self.lineEdit_70.clear()
        self.lineEdit_71.clear()
        self.lineEdit_72.clear()
        self.plainTextEdit_5.clear()

        with open("rock.txt","r") as rock_read:
            rock_text = rock_read.readlines()
            for line in rock_text:
                line = line.replace("\n","")
                self.plainTextEdit_5.appendPlainText(line)

    def file2_save(self):
        with open("file2.txt","w") as f2:
            f2.write("ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            rock = open("rock.txt", "r")
            for line in rock.readlines():
                f2.write(line)
        os.remove("rock.txt")
        QMessageBox.information(self, '已完成', '数据保存到file2.txt\n建议打开生成文件以确认', QMessageBox.Yes)

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
        self.lineEdit_76.clear()
        self.lineEdit_77.clear()
        self.lineEdit_78.clear()
        self.lineEdit_79.clear()
        self.lineEdit_80.clear()
        self.lineEdit_81.clear()
        self.lineEdit_82.clear()
        self.lineEdit_83.clear()
        self.lineEdit_84.clear()
        QMessageBox.information(self, '已完成', '数据保存到file3.txt\n建议打开生成文件以确认', QMessageBox.Yes)

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
        self.lineEdit_44.clear()
        self.lineEdit_45.clear()
        self.lineEdit_46.clear()
        self.lineEdit_47.clear()
        self.lineEdit_48.clear()
        self.lineEdit_49.clear()
        self.lineEdit_50.clear()
        self.lineEdit_40.clear()
        self.lineEdit_41.clear()
        self.lineEdit_42.clear()
        self.lineEdit_43.clear()
        QMessageBox.information(self, '已完成', '数据保存到file4.txt\n建议打开生成文件以确认', QMessageBox.Yes)

    # ！！！------file5相关没有完成
    # 柱坐标相关没有完成
    def file5_save(self):
        if (self.radioButton.isChecked()):
            print("笛卡尔坐标")
            with open("mesh.txt","w") as f5:
                f5.write("Input file for a test\n")
                zdwgs = self.lineEdit_8.text()
                f5.write("%s 100 5 'old'\n"%zdwgs)
                f5.write("Regions\n")
                qy = self.lineEdit_10.text()
                f5.write("%s\n"%qy)
                dke1 = open("dke1.txt","r")
                for line in dke1.readlines():
                    f5.write(line)
                f5.write("XYZ\n")
                f5.write("%10s\n"%("00."))
                dke2 = open("dke2.txt", "r")
                for line in dke2.readlines():
                    f5.write(line)
                f5.write("\nENDFI----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            QMessageBox.information(self, '已完成', '数据保存到mesh.txt\n生成网格前请打开生成文件以确认格式正确', QMessageBox.Yes)
            #os.remove("dke1.txt")
            #os.remove("dke2.txt")
        elif (self.radioButton_2.isChecked()):
            print("柱坐标")
            with open("mesh.txt","w") as f5:
                f5.write("Input file for a test\n")
                zdwgs = self.lineEdit_22.text()
                zdljs = self.lineEdit_23.text()
                fq = self.lineEdit_20.text()
                f5.write("%s %s 5 'old'\n"%(zdwgs,zdljs))
                f5.write("Regions\n")
                f5.write("%s\n" % fq)

                zzb1 = open("zzb1.txt", "r")
                for line in zzb1.readlines():
                    f5.write(line)
                f5.write("RZ2DL\nRADII\n")
                f5.write("    2\n")
                f5.write("    0         0.5e-1")

                zzb2 = open("zzb2.txt", "r")
                for line in zzb2.readlines():
                    f5.write(line)
                # 这里应该是对layer部分进行处理，但有些没想好应该如何处理
                # 暂且保留，默认置入20个默认值
                # zzb3 = open("zzb3.txt", "r") # 用来放layer相关的部分数据文件
                # for line in zzb3.readlines():
                #     f5.write(line)
                f5.write("\nLAYER\n")
                f5.write("   20\n")
                f5.write("    8.0e00    8.0e00    8.0e00    8.0e00    8.0e00    4.0e00    4.0e00    4.0e00\n")
                f5.write("    4.0e00    4.0e00    4.0e00    4.0e00    4.0e00    4.0e00    4.0e00    8.0e00\n")
                f5.write("    8.0e00    8.0e00    8.0e00    8.0e00\n")
                f5.write("\nENDFI----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            QMessageBox.information(self, '注意', '对于柱坐标的处理尚不完善\n请手动进行确认', QMessageBox.Yes)
            QMessageBox.information(self, '注意', '涉及到LAYER部分置入了20个默认值，这些需要手动修改', QMessageBox.Yes)
            QMessageBox.information(self, '已完成', '数据保存到mesh.txt\n生成网格前请打开生成文件以确认格式正确', QMessageBox.Yes)

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
        self.lineEdit_33.clear()
        self.lineEdit_34.clear()
        self.lineEdit_35.clear()
        self.lineEdit_36.clear()
        self.lineEdit_37.clear()
        self.lineEdit_33.clear()
        self.lineEdit_33.clear()
        QMessageBox.information(self, '已完成', '数据保存到file6.txt\n建议打开生成文件以确认', QMessageBox.Yes)

    def add_file7_8(self):
        mc = self.lineEdit_85.text()
        jhbm = self.lineEdit_86.text()
        scfs = self.lineEdit_88.text()
        scjzs = self.lineEdit_89.text()
        scjjdyl = self.lineEdit_90.text()
        zrfs = self.lineEdit_91.text()
        zrsl = self.lineEdit_92.text()
        rh = self.lineEdit_93.text()
        with open("coft.txt","a") as coft:
            coft.write(jhbm)
            coft.write("\n")
        self.lineEdit_85.clear()
        self.lineEdit_86.clear()
        self.lineEdit_88.clear()
        self.lineEdit_89.clear()
        self.lineEdit_90.clear()
        self.lineEdit_91.clear()
        self.lineEdit_92.clear()
        self.lineEdit_93.clear()
        self.plainTextEdit_6.clear()
        self.plainTextEdit_7.clear()
        with open("gener.txt","a") as gener:
            if (self.radioButton_3.isChecked()):
                gener.write("%5s%5s%29s%11s%10s\n"%(mc,jhbm,scfs,scjzs,scjjdyl))
            elif (self.radioButton_4.isChecked()):
                gener.write("%5s%5s%29s%11s%10s\n"%(mc,jhbm,zrfs,zrsl,rh))
        with open("coft.txt","r") as coft_read:
            coft_text = coft_read.readlines()
            for line in coft_text:
                line = line.replace("\n","")
                self.plainTextEdit_6.appendPlainText(line)
        with open("gener.txt","r") as gener_read:
            gener_text = gener_read.readlines()
            for line in gener_text:
                line = line.replace("\n","")
                self.plainTextEdit_7.appendPlainText(line)

    def coft_save(self):
        with open("coft.txt","w") as coft:
            text = self.plainTextEdit_6.toPlainText()
            print("save test:")
            print(text)
            coft.write(text)
    def gener_save(self):
        with open("gener.txt", "w") as gener:
            text = self.plainTextEdit_7.toPlainText()
            print("save test:")
            print(text)
            gener.write(text)
    def file7_8_save(self):
        with open("file7.txt","w") as f7:
            f7.write("COFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            f7.write("SS_Time_Series\n")
            coft = open("coft.txt", "r")
            for line in coft.readlines():
                f7.write(line)
        with open("file8.txt","w") as f8:
            f8.write("GENER\n")
            gener = open("gener.txt", "r")
            for line in gener.readlines():
                f8.write(line)
        QMessageBox.information(self, '已完成', '数据保存到file7.txt和file8.txt\n建议打开生成文件以确认', QMessageBox.Yes)
        # os.remove("coft.txt")
        # os.remove("gener.txt")

    def file9_save(self):
        wgmc = self.lineEdit_51.text()
        kxd = self.lineEdit_52.text()
        cszt = self.lineEdit_53.text()
        zbl1 = self.lineEdit_54.text()
        zbl2 = self.lineEdit_55.text()
        zbl3 = self.lineEdit_56.text()
        zbl4 = self.lineEdit_57.text()
        with open("file9.txt","w") as f9:
            f9.write("INCON----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            f9.write("%5s%25s%5s\n"%(wgmc,kxd,cszt))
            f9.write("%20s%20s%20s%20s\n"%(zbl1,zbl2,zbl3,zbl4))
        self.lineEdit_51.clear()
        self.lineEdit_52.clear()
        self.lineEdit_53.clear()
        self.lineEdit_54.clear()
        self.lineEdit_55.clear()
        self.lineEdit_56.clear()
        self.lineEdit_57.clear()
        QMessageBox.information(self, '已完成', '数据成功保存在file9.txt\n建议打开生成文件以确认',QMessageBox.Yes)

    def file10_save(self):
        cszt = self.lineEdit_75.text()
        zbl1 = self.lineEdit_58.text()
        zbl2 = self.lineEdit_60.text()
        zbl3 = self.lineEdit_74.text()
        zbl4 = self.lineEdit_59.text()
        wgmc = self.lineEdit_73.text()
        with open("file10.txt","w") as f10:
            f10.write("INDOM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
            f10.write("%5s%5s\n"%(wgmc,cszt))
            f10.write("%20s%20s%20s%20s\n"%(zbl1,zbl2,zbl3,zbl4))
            f10.write("ENDCY----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8\n")
        self.lineEdit_75.clear()
        self.lineEdit_58.clear()
        self.lineEdit_60.clear()
        self.lineEdit_74.clear()
        self.lineEdit_59.clear()
        self.lineEdit_73.clear()
        QMessageBox.information(self, '已完成', '数据成功保存在file10.txt\n建议打开生成文件以确认', QMessageBox.Yes)

    def exit_data(self):
        self.close()

    def combine_all_files(self):
        reply = QMessageBox.question(self, '即将进行文件的合并', '目录下是否已存在合并所需file 1~10', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            #shutil.copy("MESH","file5.txt")
            filenames = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt',
                         'file8.txt', 'file9.txt', 'file10.txt']
            print(filenames)

            if (os.path.exists("file1.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file1不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file2.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file2不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file3.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file3不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file4.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file4不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file5.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file5不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file6.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file6不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file7.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file7不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file8.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file8不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file9.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file9不存在，文件合并失败', QMessageBox.Yes)
                return
            if (os.path.exists("file10.txt")):pass
            else:
                QMessageBox.information(self, '出现错误', 'file10不存在，文件合并失败', QMessageBox.Yes)
                return

            file = open('input', 'w')
            for f_n in filenames:
                filepath = f_n
                for line in open(filepath):
                    file.writelines(line)
                    print(line, end='')
                file.write('\n')
            file.close()
            QMessageBox.information(self, '已完成', '所有数据已合并到input文件中\n在进行下一步的操作前，建议打开input文件以确认文件格式', QMessageBox.Yes)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = DataWindow()
    myWin.show()
    sys.exit(app.exec_())
