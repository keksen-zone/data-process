#在这里测试了绘制不均匀的网格，效果还可以，考虑后续进行采用
import matplotlib.pyplot as plt
import numpy as np

ax = plt.gca()
Arr_y=np.array([0.5,1,1.5,3,3.5,7])
Arr_x=np.array([0.5,1,1.5,3,3.5,7])

#Arr_y: y-direction data, 1D numpy array or list.
for j in range(len(Arr_y)):
    plt.hlines(y = Arr_y[j], xmin = Arr_x.min(), xmax = Arr_x.max(), color = 'black')

#Arr_x: x-direction data, 1D numpy array or list.
for i in range(len(Arr_x)):
    plt.vlines(x = Arr_x[i], ymin = Arr_y.min(), ymax = Arr_y.max(), color = 'green')
Arr_xticks=np.arange(0,6)
Arr_yticks=np.arange(0,6)
#Custom your ticks here, 1D numpy array or list.
ax.set_xticks(Arr_xticks)
ax.set_yticks(Arr_yticks)

plt.xlim(Arr_x.min(), Arr_x.max())
plt.ylim(Arr_y.min(), Arr_y.max())

plt.show()