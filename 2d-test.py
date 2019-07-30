import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import pylab

# 在这里读入两个数组然后进行绘图
with open('SS_Time_Series.csv', 'r') as f:
    reader = csv.reader(f)
    col1 = [row[0] for row in reader]
    #col1.reverse()
    print(col1)

with open('SS_Time_Series.csv', 'r') as f:
    reader = csv.reader(f)
    col2 = [row[4] for row in reader]
    print(col2)

t = np.arange(0, 33)
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('hengzuobiao')
ax1.set_ylabel('shuxing-1', color=color)
ln1 = ax1.plot(t, col1, '.', markersize=5, mfc='b',
               mec='r')  # marker 形状，大小，面的颜色和边界的颜色
ln11 = ax1.plot(t, col1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
a = plt.gca()
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
# we already handled the x-label with ax1
ax2.set_ylabel('shuxing-2', color=color, fontsize=16, rotation=270)
ln2 = ax2.plot(t, col2, color=color)
ax2.tick_params(axis='y', labelcolor=color, labelsize=12)
# ax2.set_yticks(np.arange(-1.25, 1.26, 0.25))
# ax2.set_ylim(-1.2, 1.2)
# ax2.annotate(s='nothing',xytext=(2,-0.5),xy=(9,0.3),arrowprops=dict(arrowstyle="->"))
# ax2.text(6,0,'text')

ln = ln1 + ln2
labs = ['line1', 'line2']
ax1.legend(ln, labs, loc='upper center')  # 将两条曲线的label放在同一个图例中
fig.tight_layout()  # otherwise the right y-label is slightly clipped

a = plt.gca()  # 隐藏XTOP，这里相当于画了两张图，所以隐藏了两次
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)
plt.show()
