from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates', static_folder='', static_url_path='')
app.debug = True


@app.route("/")
def index():
    return render_template("11Login.html")


@app.route("/forms", methods=['GET', 'POST'])
def getformData():
    for key in request.values:
        print(key + ":" + request.values.get(key))
    return "login success"


if __name__ == '__main__':
    app.run(port=8080)

# 总结
"""
request.args 只能接收 GET 方法提交的数据
request.values 能接收 GET 方法和 POST 方法提交的数据
request.form 能接收 POST 方法和 PUT 方法提交的数据
"""
