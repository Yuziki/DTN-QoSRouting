import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x_axis_data = [10, 15, 20, 25, 30] #x
y1_axis_data = [82, 85, 89, 110, 135] #y
y2_axis_data = [96, 108, 131, 169, 184] #y

plt.plot(x_axis_data, y1_axis_data,  'r*--', alpha=0.5, linewidth=1, label='Dijstra')#'bo-'表示蓝色实线，数据点实心原点标注
plt.plot(x_axis_data, y2_axis_data,  'b*--', alpha=0.5, linewidth=1, label='DTSR')#'bo-'表示蓝色实线，数据点实心原点标注
## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，

plt.legend()  #显示上面的label
plt.xlabel('用户请求频率') #x_label
plt.ylabel('平均时延')#y_label

plt.show()

y1_axis_data = [0.0370, 0.042, 0.065, 0.069, 0.098] #y
y2_axis_data = [0.00838, 0.0095, 0.012, 0.015, 0.021] #y
plt.plot(x_axis_data, y1_axis_data, 'r*--', alpha=0.5, linewidth=1, label='Dijstra')#'bo-'表示蓝色实线，数据点实心原点标注
plt.plot(x_axis_data, y2_axis_data,  'b*--', alpha=0.5, linewidth=1, label='DTSR')#'bo-'表示蓝色实线，数据点实心原点标注
## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，

plt.legend()  #显示上面的label
plt.xlabel('用户请求频率') #x_label
plt.ylabel('平均丢包率')#y_label

plt.show()

y1_axis_data = [1.74, 2.36, 2.97, 4.12, 6.7] #y
y2_axis_data = [1.19, 1.22, 1.31, 1.39, 1.52] #y
plt.plot(x_axis_data, y1_axis_data, 'r*--', alpha=0.5, linewidth=1, label='Dijstra')#'bo-'表示蓝色实线，数据点实心原点标注
plt.plot(x_axis_data, y2_axis_data,  'b*--', alpha=0.5, linewidth=1, label='DTSR')#'bo-'表示蓝色实线，数据点实心原点标注
## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，

plt.legend()  #显示上面的label
plt.xlabel('用户请求频率') #x_label
plt.ylabel('平均路由次数')#y_label

plt.show()
