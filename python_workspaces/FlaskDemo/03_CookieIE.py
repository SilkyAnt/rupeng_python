from flask import Flask, make_response, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_word():
    try:
        if request.cookies["Loginadmin"] == "admin":
            return render_template("03Main.html")
    except KeyError:
        return render_template("03Login.html")
    return render_template("03Login.html")


@app.route("/formData")
def getForms():
    name = request.values['username']
    pwd = request.values['userpwd']
    if name == 'admin' and pwd == '123456':
        resp = make_response(render_template("03Main.html"))
        # 如果不设置 max_age ,cookie 在浏览器关闭后就会被删除
        # 如果使设置 max_age ，60 指的是 关闭浏览器后60秒过期
        resp.set_cookie('Loginadmin', name, max_age=60)
        return resp
    else:
        return render_template("03Login.html")


if __name__ == '__main__':
    app.run()
