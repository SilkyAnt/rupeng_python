# coding=utf-8
# 我这个例子已过时，测不出结果
# 知识点：要想不验证SSL，设置verify为False
import requests

r = requests.get("https://www.12306.cn/mormhweb/", verify=True)
print r.text
