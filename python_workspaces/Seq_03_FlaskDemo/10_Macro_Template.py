from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('03Main.html')


# 遍历数组,前台模板使用的是函数（宏）
@app.route('/for1')
def get_user1():
    return render_template('09_macroTemplate.html',
                           comments=['1', '2', '3', '4'])


# 遍历数组,前台模板使用的是方法 和 定义好的函数宏
@app.route('/for2')
def get_user2():
    return render_template('10_macroTemplate.html',
                           comments=['1', '2', '3', '4'])


if __name__ == '__main__':
    app.run(port=8080)
