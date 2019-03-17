# 导入faker模块
from faker import Factory

fake = Factory().create(locale="zh_CN")
# print(dir(fake))
for i in range(1, 11):
    print("第{0}次随机产生的数据:".format(i))
    print("用户姓名:{0}".format(fake.name()))
    print("用户名:{0}".format(fake.user_name()))
    print("密码:{0}".format(fake.password()))
    print("电子信箱:{0}".format(fake.email()))
    print("电话号码:{0}".format(fake.phone_number()))
    print("住址:{0}".format(fake.address()))
    print("所在城市:{0}".format(fake.city()))
    print("段落:{0}".format(fake.paragraph()))
    print("文本:{0}".format(fake.text()))
    print("IPv4:{0}".format(fake.ipv4()))
    print("网址:{0}".format(fake.url()))
    print("指定长度的字符串:{0}".format(fake.pystr(min_chars=6, max_chars=12)))
