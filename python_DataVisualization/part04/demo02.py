# 计算每个点出现的次数
# encoding=utf8
from random import randint


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


# 掷骰子100次
results = []
die = Die()
for roll in range(100):
    result = die.roll()
    results.append(result)

# 分析每个点出现的频率
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
