from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template("11_base.html")


# 模板的继承 例子
@app.route('/h1')
def h1():
    return render_template("11_h1.html")


if __name__ == "__main__":
    app.run(port=8080)
