# 创建一个模拟骰子的类
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
print(results)
