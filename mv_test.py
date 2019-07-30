# -*- coding: utf-8 -*-
import os
import shutil


def cpfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


#filename = "C:/Users/user/Pictures/4sbql1gcucf.jpg"


#cpfile("C:/Users/user/Pictures/4sbql1gcucf.jpg",
#       "C:/Users/user/Desktop/界面项目/data-process/4sbql1gcucf.jpg")


def des_name(filename):
    name = filename.split("/")[-1]
    print(name)
    pres = os.getcwd()
    print(pres)
    pres = pres + "\\" + name
    print(pres)
    return pres
