# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd

def cut2csv():
    filePath = 'cutted\\'
    if (os.path.exists(filePath + "0.txt")):
        os.remove(filePath + "0.txt")
    csvfilePath = 'cutted2csv\\'
    files = os.listdir(filePath)
    print(files)

    for file in files:
        with open(filePath + file, 'r', encoding='utf-8') as f:
            time = f.readline().replace('\n', '')
            other = f.readlines()
            with open(csvfilePath + '%s.txt' % (time), 'w', encoding='utf-8') as w:
                for line in other:
                    w.write(line)
            w.close()
        f.close()

        # 修改：直接删除cutted中所有txt内容
        os.remove(filePath+file)

    txtfile = os.listdir(csvfilePath)
    print(txtfile)
    for file in txtfile:
        txt = np.loadtxt(csvfilePath + '%s' % (file))
        txtdf = pd.DataFrame(txt)
        csv_name = file.replace('.txt', '.csv')
        #csv_name = file.replace(' ', '')
        txtdf.to_csv(csvfilePath + '%s' % (csv_name), header=0, index=False)
        if (os.path.exists(csvfilePath + file)):
            os.remove(csvfilePath + file)
