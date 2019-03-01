# 动态路由
# 导入Flask模块
from flask import Flask
from flask import url_for

# 创建一个Flask的实例
app = Flask(__name__)
app.debug = True


# 注册一个路由
@app.route("/")
def index():  # 视图函数
    print(url_for('index'))
    print(url_for('index', _external=True))
    return "Hello,Welcome to Flask Web World!"


if __name__ == "__main__":
    app.run(port=8081)
