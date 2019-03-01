# 同时掷两个骰子
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
die2 = Die()
for roll in range(1000):
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
hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_labels = "Frequencies of Results"
hist.add('D6+D6', frequencies)
hist.render_to_file("demo04.svg")
