# -*- coding: utf-8 -*-
import csv
import os


def get_times():
    filedir = os.getcwd() + '\\cutted2csv'
    filenames=os.listdir(filedir)
    return filenames


def get_x():
    x = []
    with open('Plot_coord.csv', 'r') as zb:
        reader = csv.reader(zb)
        col = [row[0] for row in reader]
        for element in col:
            if (element not in x):
                x.append(element)
        print(x)
    x_file = open('x.txt', 'w')
    for tmp in x:
        x_file.write(tmp + '\n')
    return x


def get_y():
    y = []
    with open('Plot_coord.csv', 'r') as zb:
        reader = csv.reader(zb)
        col = [row[1] for row in reader]
        for element in col:
            if (element not in y):
                y.append(element)
        print(y)
    y_file = open('y.txt', 'w')
    for tmp in y:
        y_file.write(tmp + '\n')
    return y


def get_z():
    z = []
    with open('Plot_coord.csv', 'r') as zb:
        reader = csv.reader(zb)
        col = [row[2] for row in reader]
        for element in col:
            if (element not in z):
                z.append(element)
        print(z)
    z_file = open('z.txt', 'w')
    for tmp in z:
        z_file.write(tmp + '\n')
    return z
