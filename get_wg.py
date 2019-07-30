# -*- coding: utf-8 -*-
def get_wg():
    with open('wg.txt','r') as f:
        line = f.readline()
        x = line.split(' ')[0]
        y = line.split(' ')[1]
        z = line.split(' ')[2]
        print(x+" "+y+" "+z)
        return int(x), int(y), int(z)