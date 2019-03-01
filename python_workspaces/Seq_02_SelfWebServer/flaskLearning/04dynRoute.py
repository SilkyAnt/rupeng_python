# 动态路由
# 导入Flask模块
from flask import Flask
from flask import send_file

# 创建一个Flask的实例
app = Flask(__name__)
app.debug = True


# 注册一个路由
@app.route("/")
def index():  # 视图函数
    # 代码直接访问静态页面，没有经过Jinja2 模板的渲染。
    return send_file("../templates/03Hello.html")


@app.route("/user/<name>")
def user(name):
    return "hello,%s" % name


@app.route("/userid/<int:id>")
def userId(id):
    return "hello,%d" % id


if __name__ == "__main__":
    app.run(port=8080)
