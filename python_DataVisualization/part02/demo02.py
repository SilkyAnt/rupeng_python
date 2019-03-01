# encoding=utf8
import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5, 6]
y_value = [1, 4, 9, 16, 25, 36]
# s是点的大小
plt.scatter(x_value, y_value, s=50)
# title表示标题，#fontSize表示字体大小
# xlabel表示X轴的标签，#ylabel表示Y轴的标签
plt.title("Square Number", fontSize=24)
plt.xlabel("value", fontSize=14)
plt.ylabel("Square of Value", fontSize=14)
# tick_params:刻度参数
# axis="both":表示x轴和y轴 ，labelsize表示刻度字体的大小
# color表示刻度的颜色。
'''
which
: [‘major’ | ‘minor’ | ‘both’]
Default is ‘major’; apply arguments to which ticks.
which一共3个参数[‘major’ | ‘minor’ | ‘both’]
默认是major表示主刻度，后面分布为次刻度及主次刻度都显示
'''
plt.tick_params(axis="both", which='minor', labelsize=10, color="red")
plt.show()
