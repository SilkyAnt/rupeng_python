# 动态路由
# 导入Flask模块
from flask import Flask,request
# 创建一个Flask的实例
app = Flask(__name__)
app.debug = True

# 注册一个路由
@app.route("/")
def index():
    return "hello"

@app.route("/jianglp")
# http://localhost:8080/jianglp?a=123&d=45
def args():
    print(request.values)
    print(request.values['a'])
    for key in request.values:
        print(key+":"+request.values.get(key))
    return "hello"

if __name__=="__main__":
    app.run(port=8080)