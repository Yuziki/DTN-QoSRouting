import matplotlib.pyplot as plt
import numpy as np

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x_axis_data = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0] #x
y_axis_data = [114.99244206149044, 109.52571036759906, 108.47911818298306, 106.71301623031434, 105.83433835807776, 104.89166653198333,
 102.83690680962391, 99.88841503378723, 99.18048059665868, 97.36364185109107, 91.14504882260923] #y

plt.plot(x_axis_data, y_axis_data, 'b*--', alpha=0.5, linewidth=1, label='delay')#'bo-'表示蓝色实线，数据点实心原点标注
## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，

plt.legend()  #显示上面的label
plt.xlabel('切换风险阈值th') #x_label
plt.ylabel('平均时延 / ms')#y_label
 
#plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
