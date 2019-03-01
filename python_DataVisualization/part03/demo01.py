# encoding=utf8
from random import choice
import matplotlib.pyplot as plt


# 随机漫步
class RandomWalk():
    def __init__(self, num_point=5000):
        # 初始化随机漫步的总步数
        self.num_point = num_point
        # 所以随机漫步都始于(0,0)
        self.x_value = [0]
        self.y_value = [0]
        # 定义随机漫步的方法

    def fill_walk(self):
        while (len(self.x_value) < self.num_point):
            # 随机行走的方向：前进和倒退
            x_direction = choice([1, -1])
            # 每次随机做的步长
            x_distance = choice([0, 1, 2, 3, 4])
            # 每次走的步长
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            # 每次随机做的步长
            y_distance = choice([0, 1, 2, 3, 4])
            # 每次走的步长
            y_step = y_direction * y_distance
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x和y的值,其中self.x_value[-1]是最后一个值
            # self.x_value[-1]和self.y_value[-1]当前点的坐标
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            # 漫出一步之后的落脚坐标
            self.x_value.append(next_x)
            self.y_value.append(next_y)


rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_value, rw.y_value, s=15)
plt.show()
