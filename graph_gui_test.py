# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from graph_gui import *
from PyQt5.QtWidgets import QFileDialog, QAction, QMessageBox
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from get_all_data import *
from z_cut import *
from y_cut import *
from three_dim_test import *
from hqx import *
from mv_test import *
from chaifen_test import *
from cut2csv import *
from average import *
from txt2csv import *

class GraphWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent)
        self.setupUi(self)

        self.radioButton_2.setChecked(True)
        self.radioButton_3.setChecked(True)
        self.radioButton_6.setChecked(True)
        self.radioButton_8.setChecked(True)

        self.actionPlot_Data.triggered.connect(self.open_Plot_Data)
        self.actionPlot_Coord.triggered.connect(self.open_Plot_Coord)
        self.actionSS_Time_Series.triggered.connect(self.open_SS_Time_Series)
        self.actionHydrate_Info.triggered.connect(self.open_Hydrate_Info)

        self.action.triggered.connect(self.data_extract)


    def pmt_clicked(self):
        unuse = QGraphicsOpacityEffect()
        unuse.setOpacity(0.3)
        useable = QGraphicsOpacityEffect()
        useable.setOpacity(1)
        self.comboBox_5.setGraphicsEffect(unuse)
        self.label_10.setGraphicsEffect(unuse)
        self.comboBox_4.setGraphicsEffect(useable)
        self.label_9.setGraphicsEffect(useable)

    def pmt2_clicked(self):
        unuse = QGraphicsOpacityEffect()
        unuse.setOpacity(0.3)
        useable = QGraphicsOpacityEffect()
        useable.setOpacity(1)
        self.comboBox_4.setGraphicsEffect(unuse)
        self.label_9.setGraphicsEffect(unuse)
        self.comboBox_5.setGraphicsEffect(useable)
        self.label_10.setGraphicsEffect(useable)

    def open_Plot_Data(self):
        print("running function")
        filename, filetype = QFileDialog.getOpenFileName(self,"选取文件","./","All Files(*)")
        print(filename + "  " + filetype)
        dest = des_name(filename)
        cpfile(filename,dest)
    def open_Plot_Coord(self):
        print("running function")
        filename, filetype = QFileDialog.getOpenFileName(self,"选取文件","./","All Files(*)")
        print(filename + "  " + filetype)
        dest = des_name(filename)
        cpfile(filename, dest)
    def open_SS_Time_Series(self):
        print("running function")
        filename, filetype = QFileDialog.getOpenFileName(self,"选取文件","./","All Files(*)")
        print(filename + "  " + filetype)
        dest = des_name(filename)
        cpfile(filename, dest)
    def open_Hydrate_Info(self):
        print("running function")
        filename, filetype = QFileDialog.getOpenFileName(self,"选取文件","./","All Files(*)")
        print(filename + "  " + filetype)
        dest = des_name(filename)
        cpfile(filename, dest)

    def data_extract(self):
        reply=QMessageBox.question(self,'即将对数据进行拆分','所需数据是否已经打开或已位于程序运行目录下',QMessageBox.Yes |QMessageBox.No,QMessageBox.Yes)
        if reply==QMessageBox.Yes:
            print("拆分数据")
            if (os.path.exists("cutted/")):
                pass
            else:
                os.mkdir("cutted/")
            if (os.path.exists("cutted2csv/")):
                pass
            else:
                os.mkdir("cutted2csv/")

            # 检查文件存在,之后进行格式转换
            if (os.path.exists("Plot_coord.txt")):
                pass
            else:
                QMessageBox.information(self, '失败', '未找到文件Plot_coord.txt', QMessageBox.Yes)
                return
            if (os.path.exists("Hydrate_Info.txt")):
                pass
            else:
                QMessageBox.information(self, '失败', '未找到文件Hydrate_Info.txt', QMessageBox.Yes)
                return
            if (os.path.exists("SS_Time_Series.txt")):
                pass
            else:
                QMessageBox.information(self, '失败', '未找到文件SS_Time_Series.txt', QMessageBox.Yes)
                return
            if (os.path.exists("Plot_Data1.txt")):
                pass
            else:
                QMessageBox.information(self, '失败', '未找到文件Plot_Data1.txt', QMessageBox.Yes)
                return
            filelist_csv = os.listdir("cutted2csv/")
            #print(filelist)
            if (len(filelist_csv) > 0):
                reply = QMessageBox.question(self, '目标文件夹不为空',
                                             '检测到拆分目标文件夹中有残留内容\n这可能是程序上次运行的输出，可以直接使用这些数据绘图或手动将这些内容删除\n若继续拆分，会造成两次数据的混合或其他预想不到的后果\n仍然要继续吗',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    chaifen()
                    cut2csv()
                    txt2csv_ss()
                    txt2csv_hydra()
                    txt2csv_coord()
                    QMessageBox.information(self, '已完成', '数据已按照时间拆分并命名在cutted2csv文件夹下\n程序退出后它们将不会被自动删除\n稍后也可以自行查看或处理',
                                            QMessageBox.Yes)
                else:
                    pass
            else:
                chaifen()
                cut2csv()
                txt2csv_ss()
                txt2csv_hydra()
                txt2csv_coord()
                QMessageBox.information(self, '已完成', '数据已按照时间拆分并命名在cutted2csv文件夹下\n程序退出后它们将不会被自动删除\n稍后也可以自行查看或处理',
                                        QMessageBox.Yes)
            # os.system("ren output output.txt")

        else:
            pass
    def data_exist(self):
        reply = QMessageBox.question(self, '确认', '所需数据已切分完成且位于cutted2csv文件夹下', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            times = get_times()
            # attri = {0:'第一列', 1:'第二列', 2:'第三列', 3:'第四列', 4:'第五列',5: '第六列', 6:'第七列',7: '第八列',8: '第九列'}
            ceng = get_z()
            pou = get_y()
            self.comboBox_2.addItems(times)
            self.comboBox_6.addItems(times)
            self.comboBox_3.addItems(["0:P", "1:T", "2:SH", "3:SW", "4:SG","5:SI", "6:C_Inhib", "7:Krg", "8:Krw"])
            self.comboBox_7.addItems(["0:P", "1:T", "2:SH", "3:SW", "4:SG", "5:SI", "6:C_Inhib", "7:Krg", "8:Krw"])
            self.comboBox_4.addItems(ceng)
            self.comboBox_5.addItems(pou)
            self.comboBox_9.addItems(["0:P", "1:T", "2:SH", "3:SW", "4:SG", "5:SI", "6:C_Inhib", "7:Krg", "8:Krw"])
            QMessageBox.information(self, '已完成', '数据读取完成\n可以进行下一步操作',
                                    QMessageBox.Yes)
        else:
            pass

    def hpj(self):
        str_attr = self.comboBox_9.currentText()
        print("属性框的内容为：" + str_attr)
        attri = int(str_attr.split(':')[0])
        print(attri)
        draw_average(attri)

    def h3d(self):
        print("button hua 3d pressed")
        # x, y, z = get_wg()
        x = len(get_x())
        y = len(get_y())
        z = len(get_z())
        print(x, y, z)
        if self.radioButton_7.isChecked():
            print("3d 无网格线")
            str_attr = self.comboBox_7.currentText()
            print("属性框的内容为：" + str_attr)
            attri = int(str_attr.split(':')[0])
            draw_3d(x,y,z,self.comboBox_6.currentText(),
                    int(attri),0,float(self.comboBox_8.currentText()))

        elif self.radioButton_8.isChecked():
            print("3d 有网格线")
            str_attr = self.comboBox_7.currentText()
            print("属性框的内容为：" + str_attr)
            attri = int(str_attr.split(':')[0])
            draw_3d(x, y, z, self.comboBox_6.currentText(),
                    int(attri), 1,float(self.comboBox_8.currentText()))

    def hqx(self):
        print("butt1 clicked")
        if (self.comboBox.currentText()=="SS_Time_Series"):
            print("ss_selected")
            if self.radioButton_2.isChecked():
                print("gas is selected")
                ss_chanqi()
            elif self.radioButton.isChecked():
                print("water is selected")
                ss_chanshui()
        elif (self.comboBox.currentText()=="Hydrate_Info"):
            print("Hydrate_selected")
            hydrate()

    def hpm(self):
        print("butt2 clicked")
        # x, y, z = get_wg()
        x = len(get_x())
        y = len(get_y())
        z = len(get_z())
        print(x, y, z)
        if self.radioButton_3.isChecked():

            # print("属性框的索引为：" + str_attr.split(':')[0])
            # print(int(attri))
            if self.radioButton_6.isChecked():
                print("平面 有网格")
                print(self.comboBox_2.currentText())
                str_attr = self.comboBox_3.currentText()
                print("属性框的内容为：" + str_attr)
                attri = int(str_attr.split(':')[0])
                # 破案了，问题出在print中 string和int、float不能混着用
                # 所以调用时传递的参数一定要对

                z_cut(self.comboBox_2.currentText(),int(attri),
                      self.comboBox_4.currentText(),int(1),
                      x, y, z)
            elif self.radioButton_5.isChecked():
                print("平面 无网格")
                str_attr = self.comboBox_3.currentText()
                print("属性框的内容为：" + str_attr)
                attri = int(str_attr.split(':')[0])
                z_cut(self.comboBox_2.currentText(), int(attri),
                      self.comboBox_4.currentText(), 0,
                      x, y, z)
        elif self.radioButton_4.isChecked():

            # print("属性框的索引为：" + str_attr.split(':')[0])
            # print(int(attri))
            if self.radioButton_6.isChecked():
                print("剖面  有网格")
                #x, y, z = get_wg()
                x = len(get_x())
                y = len(get_y())
                z = len(get_z())
                print(x, y, z)
                str_attr = self.comboBox_3.currentText()
                print("属性框的内容为：" + str_attr)
                attri = int(str_attr.split(':')[0])
                print(self.comboBox_2.currentText())
                y_cut(self.comboBox_2.currentText(), int(attri),
                      self.comboBox_5.currentText(), 1,
                      x, y, z)
            elif self.radioButton_5.isChecked():
                print("剖面 无网格")
                #x, y, z = get_wg()
                x = len(get_x())
                y = len(get_y())
                z = len(get_z())
                print(x, y, z)
                str_attr = self.comboBox_3.currentText()
                print("属性框的内容为：" + str_attr)
                attri = int(str_attr.split(':')[0])
                y_cut(self.comboBox_2.currentText(), int(attri),
                      self.comboBox_5.currentText(), 0,
                      x, y, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = GraphWindow()
    myWin.show()
    sys.exit(app.exec_())
