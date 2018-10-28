from flask import Flask, current_app, g

app = Flask(__name__)


@app.route("/")
def hello_world():
    # 获取应用上下文
    print(app.app_context())
    # 当前激活程序的程序实例
    print(app)
    print(current_app)
    print(current_app.name)
    print(app == current_app)

    # 视图函数之间的数据传递
    print(g.number)

    return "Hello World!"


@app.before_request
def before_request():
    g.number = 1000
    print("before_request")


@app.after_request
# 一定要有一个参数，response 这个参数名称可以自己定义
def after_request(response):
    print("after_request")
    return response


if __name__ == "__mian__":
    app.run()
