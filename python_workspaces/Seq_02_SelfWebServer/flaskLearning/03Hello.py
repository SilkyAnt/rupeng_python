# 访问Html文件
# 导入Flask模块
from flask import Flask
from flask import send_file

# 创建一个Flask的实例
app = Flask(__name__)


# app.debug = True

# 注册一个路由
@app.route("/")
def index():  # 视图函数
    # 代码直接访问静态页面，没有经过Jinja2 模板的渲染。
    return send_file("../templates/03Hello.html")


# 确保直接执行这个脚本时
if __name__ == "__main__":
    # 启动服务器
    # 端口号只能用参数设置，debug模式可以用参数，也可以用第六行的代码
    app.run(port=8080, debug=True)
