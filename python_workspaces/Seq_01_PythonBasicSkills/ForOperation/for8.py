# 打印乘法表的层数
for row in range(1, 10):
    # 打印乘法表每层的条数
    for col in range(row + 1):
        # 打印具体的每个计算式子
        print("%d*%d=%d " % (row, col, row * col), end="")
    print()
