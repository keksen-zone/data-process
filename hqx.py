# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import *
import csv
import matplotlib.ticker as ticker

mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

def ss_chanqi():
    with open('SS_Time_Series.csv' , 'r') as f:
        reader = csv.reader(f)
        day = [float(row[0]) for row in reader] # 时间
    with open('SS_Time_Series.csv' , 'r') as f:
        reader = csv.reader(f)
        cqsl = [float(row[1]) for row in reader] # 产气速率
    with open('SS_Time_Series.csv' , 'r') as f:
        reader = csv.reader(f)
        ljcql = [float(row[3]) for row in reader] # 累计产气量


    rcParams["figure.figsize"] = [12.8,4.8]
    plt.subplot(121)
    plt.plot(day,cqsl)
    plt.xlabel("时间/d")
    plt.ylabel("产气速率m^3/d")


    plt.subplot(122)
    plt.plot(day,ljcql)
    plt.xlabel("时间/d")
    plt.ylabel("累计产气量m^3")

    plt.show()

def ss_chanshui():
    with open('SS_Time_Series.csv' , 'r') as f:
        reader = csv.reader(f)
        day = [float(row[0]) for row in reader] # 时间
    with open('SS_Time_Series.csv' , 'r') as f:
        reader = csv.reader(f)
        cssl = [float(row[4]) for row in reader] # 产水速率
    with open('SS_Time_Series.csv' , 'r') as f:
        reader = csv.reader(f)
        ljcsl = [float(row[5]) for row in reader] # 累计产水量

    rcParams["figure.figsize"] = [12.8,4.8]
    plt.subplot(121)
    plt.plot(day,cssl)
    plt.xlabel("时间/d")
    plt.ylabel("产水速率m^3/d")


    plt.subplot(122)
    plt.plot(day,ljcsl)
    plt.xlabel("时间/d")
    plt.ylabel("累计产水量m^3")

    plt.show()

def hydrate():
    with open('Hydrate_Info.csv' , 'r') as f:
        reader = csv.reader(f)
        day = [float(row[0]) for row in reader] # 时间
    with open('Hydrate_Info.csv' , 'r') as f:
        reader = csv.reader(f)
        shwfjqsl = [float(row[2]) for row in reader] # 水合物分解气速率m3/d
    with open('Hydrate_Info.csv' , 'r') as f:
        reader = csv.reader(f)
        shwljfjl = [float(row[4]) for row in reader] # 水合物累积分解量m3

    rcParams["figure.figsize"] = [12.8,4.8]
    plt.subplot(121)
    plt.plot(day,shwfjqsl)
    plt.xlabel("时间/d")
    plt.ylabel("水合物分解气速率m^3/d")

    plt.subplot(122)
    plt.plot(day,shwljfjl)
    plt.xlabel("时间/d")
    plt.ylabel("水合物累积分解量m^3")

    plt.show()
