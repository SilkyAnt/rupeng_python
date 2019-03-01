# 第一个Flask Web应用程序
# 导入Flask模块
from flask import Flask

# 创建一个Flask的实例
app = Flask(__name__)


# 注册一个路由
@app.route("/")
def index():  # 视图函数
    return "Hello,Welcome to Flask Web World!"


# 确保直接执行这个脚本时
if __name__ == "__main__":
    # 启动服务器
    app.run()
