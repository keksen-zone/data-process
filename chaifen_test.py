# -*- coding: utf-8 -*-
#修改后缀名命令 ren output output.txt
import os
import pandas as pd
import numpy as np
import re

def chaifen():
    cut=re.compile(r'TIME = ')
    fileContent = open('Plot_Data1.txt', 'r', encoding='utf8').read();  # 读文件内容
    paraList = cut.split(fileContent)  # 根据换行符对文本进行切片
    #lineList = cut.search(fileContent)
    #print(lineList)

    #fileWriter = open('cutted/0.txt', 'w', encoding='utf8');  # 创建一个写文件的句柄
    for paraIndex in range(len(paraList)):  # 遍历切片后的文本列表
        fileWriter = open('cutted/' + str((paraIndex)) + '.txt', 'w', encoding='utf8');
        fileWriter.write(paraList[paraIndex]);  # 先将列表中第一个元素写入文件里
        fileWriter.close();  # 关闭当前句柄
        #fileWriter = open('cutted/' + str((paraIndex + 1)) + '.txt', 'w',encoding='utf8');
