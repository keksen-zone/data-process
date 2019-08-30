import numpy as np
import pandas as pd


def txt2csv_hydra():
    txt = np.loadtxt('Hydrate_Info.txt',skiprows=1)
    txtDF = pd.DataFrame(txt)
    txtDF.to_csv('Hydrate_Info.csv', header=0, index=False)


def txt2csv_coord():
    txt = np.loadtxt('Plot_coord.txt')
    txtDF = pd.DataFrame(txt)
    txtDF.to_csv('Plot_coord.csv', header=0, index=False)


def txt2csv_ss():
    txt = np.loadtxt('SS_Time_Series.txt',skiprows=1)
    txtDF = pd.DataFrame(txt)
    txtDF.to_csv('SS_Time_Series.csv', header=0, index=False)

