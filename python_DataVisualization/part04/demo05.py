# 同时掷两个面数不同的骰子
# 下面来创建一个6面骰子和一个10面的骰子，看看同时掷这两个骰子50000次的结果如何
# encoding=utf8
from random import randint
import pygal


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


# 掷骰子1000次
results = []
die1 = Die()
die2 = Die(10)
for roll in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)
print(results)
# 分析每个点出现的频率
frequencies = []
# 从2,3,4,5,6.....12出现的频率
for value in range(2, die1.num_sides + die2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 画直方图
hist = pygal.Bar()
hist.title = "Result of rolling D6 and D10 50000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_labels = "Frequencies of Results"
hist.add('D6+D10', frequencies)
hist.render_to_file("demo05.svg")
