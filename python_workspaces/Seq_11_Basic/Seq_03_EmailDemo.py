from flask import Flask
from flask_mail import Mail, Message
import Config

# 从配置文件里面读取
app = Flask(__name__)

# 读取配置文件
app.config.from_object(Config)
# 下面注释的代码等价于上一行代码
# app.config.from_pyfile('Config.py')
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject="重要任务", sender='419795232@qq.com', recipients=['1037178580@qq.com'])
    msg.html = "给你一个重要任务！"
    mail.send(msg)
    return "OK"


if __name__ == '__main__':
    app.run()
