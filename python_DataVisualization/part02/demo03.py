# encoding=utf8
import matplotlib.pyplot as plt

# x轴的数据
x_value = list(range(1, 1001))
# y轴的数据自动计算
y_value = [x ** 2 for x in x_value]
# 设置每个坐标轴的取值范围
# x轴的范围:0-1100
# y轴的范围:0-1100000
plt.axis([0, 1100, 0, 1100000])
plt.scatter(x_value, y_value, s=2)
plt.title("Square Number", fontSize=24)
plt.xlabel("value", fontSize=14)
plt.ylabel("Square of Value", fontSize=14)
plt.tick_params(axis="both", labelsize=10, color="red")
plt.show()
