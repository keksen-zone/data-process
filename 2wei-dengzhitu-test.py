import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# txt = np.loadtxt('Plot_Data.txt')
# txtDF = pd.DataFrame(txt)
# txtDF.to_csv('file1.csv', index=False)

with open('file1.csv', 'r') as f:
    reader = csv.reader(f)
    col1 = [row[0] for row in reader]
#    print(col1)
    tmp=np.array(col1).astype(np.float)
    print(tmp.max())
    print(np.argwhere(tmp==tmp.max()))
    print(tmp.min())
    print(np.argwhere(tmp == tmp.min()))
    Z = np.array(col1).reshape(50, 50)
    # 转换一维到二维
    # 实际还需要转换到三维


x = np.arange(0,50)
y = np.arange(0,50)
X, Y = np.meshgrid(x, y)

g = plt.contourf(X, Y, Z, 5, alpha=0.5, cmap=plt.cm.jet)
plt.clabel(g, inline=1, fontsize=10)
plt.title('this is a test')
plt.colorbar()
plt.grid(c='w',linestyle='-.')
plt.show()
