# encoding=utf8
import matplotlib.pyplot as plt

x_value = list(range(1, 101))
y_value = [x ** 2 for x in x_value]
plt.axis([0, 110, 0, 11000])
# 散点图默认为蓝色和黑色轮廓，但绘制很多数据时，黑色轮廓可能粘在一起
# 通过两种方法设置点的颜色
# plt.scatter(x_value,y_value,s=4,edgecolors="none",c="red")
plt.scatter(x_value, y_value, s=4, edgecolors="none", c=(1, 0, 0))
plt.title("Square Number", fontSize=24)
plt.xlabel("value", fontSize=14)
plt.ylabel("Square of Value", fontSize=14)
plt.tick_params(axis="both", labelsize=10, color="red")
plt.show()
