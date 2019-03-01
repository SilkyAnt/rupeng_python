# encoding=utf8
import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]
plt.axis([0, 1100, 0, 1100000])
# plt.scatter(x_value,y_value,s=4,edgecolors="none",c="red")
plt.scatter(x_value, y_value, s=2, c=y_value, cmap=plt.cm.Blues)
plt.title("Square Number", fontSize=24)
plt.xlabel("value", fontSize=14)
plt.ylabel("Square of Value", fontSize=14)
plt.tick_params(axis="both", labelsize=10, color="red")
plt.show()
