# encoding=utf8
import matplotlib.pyplot as plt

input = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
# linewidth设置线条宽度
plt.plot(input, squares, linewidth=5)
# title表示标题，#fontSize表示字体大小
# xlabel表示X轴的标签，#ylabel表示Y轴的标签
plt.title("Square Number", fontSize=24)
plt.xlabel("value", fontSize=14)
plt.ylabel("Square of Value", fontSize=14)
# tick_params:刻度参数
# axis="both":表示x轴和y轴 ，labelsize表示刻度字体的大小
# color表示刻度的颜色。
plt.tick_params(axis="both", labelsize=10, color="red")
plt.show()
