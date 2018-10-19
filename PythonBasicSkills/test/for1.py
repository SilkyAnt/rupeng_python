friend = [1,2,3,4,5]

for a in friend:
    del friend[0]
    if len(friend) == 2:
        print('I want to invite you,{}' .format(friend[0]))
        print('I want to invite you,{}' .format(friend[1]))
    if len(friend) == 0:
        print(a)
        break
print(len(friend))

#friend 是5个元素的列表 最后输出的长度是 2  为什么