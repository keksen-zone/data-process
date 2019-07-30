# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D, art3d

def draw_3d(x, y, z, time, attri, grid_line, touming):
    print(x,y,z)
    print(time)
    print(attri)
    print("属性↑  网格线↓")
    print(grid_line)
    tmp = []
    color = []
    colors = []
    with open('cutted2csv\\%s'%time, 'r') as f:
        reader = csv.reader(f)
        col1 = [row[attri] for row in reader]
        color = np.array(col1).astype(np.float)
        norm = plt.Normalize()
        colors = plt.cm.jet(norm(color))
        # colors=get_colors(color,plt.cm.jet)
        tmp = np.array(col1).reshape(x, y, z)
    # print(tmp)
    #print(colors[0])
    #colors[:3]=0.5
    index=0
    for i in colors:
        colors[index][3]=touming
        index=index+1

    #print(colors[0])
    #print(len(colors))
    after = np.reshape(colors, (x, y, z, 4))

    # after[1:-1, 1:-1, 1:-1, 0:3] = 0
    # after[1:-1, 1:-1, 1:-1, 3] = 1

    #print(color[0])
    #print(after[0])
    #print(len(after))

    # r, theta, z = np.mgrid[0:19:1j, 0:19:1j, 0:19:1j]
    # test = np.zeros((20, 20, 20))
    # test[..., 0] = np.arange(0, 20)
    # test[..., 1] = np.arange(0, 20)
    # test[..., 2] = np.arange(0, 20)
    # colors=matplotlib.colors.hsv_to_rgb(tmp)
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # #ax.set_aspect('equal')
    # ax.voxels(tmp, edgecolors='k',color=colors)
    # plt.title('this is a test for 3d')
    # #plt.colorbar()
    # plt.show()


    spatial_axes = [x, y, z]
    filled = tmp
    colors = after

    # spatial_axes = [5, 5, 5]
    # filled = np.ones(spatial_axes, dtype=np.bool)
    #
    # colors = np.empty(spatial_axes + [4], dtype=np.float32)
    # alpha = 1
    # colors[0] = [1, 0, 0, alpha]
    # colors[1] = [0, 1, 0, alpha]
    # colors[2] = [0, 0, 1, alpha]
    # colors[3] = [1, 1, 0, alpha]
    # colors[4] = [0, 1, 1, alpha]
    #
    # # set all internal colors to black with alpha=1
    # colors[1:-1, 1:-1, 1:-1, 0:3] = 0 # 在里面的
    # colors[1:-1, 1:-1, 1:-1, 3] = 1


    fig = plt.figure()
    #print()
    #print(colors[0])
    #print(len(colors))
    ax = fig.add_subplot('111', projection='3d')
    if grid_line==0:
        ax.voxels(filled, facecolors=colors)#, edgecolors='k')
    elif grid_line==1:
        ax.voxels(filled, facecolors=colors, edgecolors='k')
    #fig.colorbar(p)
    m = cm.ScalarMappable(cmap=plt.cm.jet, norm=norm)
    m.set_array([])
    plt.colorbar(m)
    #plt.colorbar(colors)
    plt.title('this is a test')
    plt.show()

#draw_3d(25,25,15," 1.55000000E+03.csv",1,1,0.5)