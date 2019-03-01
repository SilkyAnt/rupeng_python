# 动态路由
# 导入Flask模块
from flask import Flask, redirect

# 创建一个Flask的实例
app = Flask(__name__)
app.debug = True


# 注册一个路由
@app.route("/baidu")
def index():  # 视图函数
    return redirect("https://www.baidu.com")


if __name__ == "__main__":
    app.run(port=8081)
