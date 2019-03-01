# 绘制直方图
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
die = Die()
for roll in range(1000):
    result = die.roll()
    results.append(result)

# 分析每个点出现的频率
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 画直方图
hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.y_labels = "Frequencies of Results"
hist.add('D6', frequencies)
hist.render_to_file("demo03.svg")
print(frequencies)
