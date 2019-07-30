# -*- coding: utf-8 -*-
import csv
import os
from pylab import *
import matplotlib.pyplot as plt

def draw_average(attr):
    print("average entered")
    print(attr)
    filedir = os.getcwd() + '\\cutted2csv'
    filenames = os.listdir(filedir)
    mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
    mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    time=[]
    average=[]
    for file in filenames:
        #print(file)
        tmp=file.replace(" ", "")
        tmp=tmp.replace(".csv", "")
        #print(tmp)
        #print(float(tmp))
        time.append(float(tmp))

        with open("cutted2csv\\"+file, 'r') as data:
            reader = csv.reader(data)
            col = [row[attr] for row in reader]
            #float_col = map(eval, col)
            sum_col=0
            for i in col:
                sum_col=sum_col+float(i)
            ava = sum_col/len(col)
            #print(ava)
            average.append(ava)

    hb = list(zip(time,average))
    #hb = [(119321950.0, 8.145663774656002), (12518750.0, 13.055779873439894), (128350.0, 13.273922225959284), (1550.0, 13.260259962783815), (162521950.0, 6.576182315846416), (1869150.0, 13.311581527232809), (199241950.0, 5.618039491082461), (204101950.0, 5.526831180705229), (208151950.0, 5.453713073654115), (213551950.0, 5.357368192737707), (218951950.0, 5.264145632308539), (224351950.0, 5.181581572767957), (225701950.0, 5.165013959097347), (227051950.0, 5.15015755191728), (228401950.0, 5.1369616899454575), (230831950.0, 5.123083084542763), (249191950.0, 5.098686385192554), (292391950.0, 5.064214295960514), (31950.0, 13.263698157909694), (335591950.0, 5.0451578767167815), (37094750.0, 12.362429254472508), (378791950.0, 5.034569090095943), (421991950.0, 5.02870874384321), (465191950.0, 5.02548532756053), (49550.0, 13.265951260256365), (508391950.0, 5.023729468700781), (5145950.0, 13.237835614414875), (518400000.0, 5.02345399469014), (56350.0, 13.26671267009098), (65150.0, 13.267683764826653), (73950.0, 13.268622362546116), (76121950.0, 10.506047321773867), (896350.0, 13.313010494637762)]

    hb.sort()
    print(hb)
    # print(hb[0][0])
    # print(hb[0][1])
    af_time=[]
    af_ava=[]
    for item in hb:
        af_time.append(item[0])
        af_ava.append(item[1])
    print(af_time)
    print(af_ava)
    plt.plot(af_time,af_ava)
    plt.xlabel("时间")
    plt.ylabel("属性的平均值")
    plt.show()

#draw_average(1)