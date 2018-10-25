from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
app.secret_key = '1234567'


@app.route('/', methods=('GET', 'POST'))
def login():
    return render_template("14_reg.html")


# 模拟注册功能，表单提交，后台验证
@app.route('/reg', methods=('GET', 'POST'))
def reg():
    username = request.form['username']
    print(username)
    if None == username or username == "":
        username_error = "用户名不能为空!"
    else:
        username_error = ""
    print(username)
    userpwd = request.form['userpwd']
    if len(userpwd) < 6 or len(userpwd) > 10:
        pwderror = "用户的密码长度为6-10"
    else:
        pwderror = ""
    return render_template("14_reg.html", usernameError2=username_error, pwderror=pwderror)


if __name__ == "__main__":
    app.run(port=8080)
