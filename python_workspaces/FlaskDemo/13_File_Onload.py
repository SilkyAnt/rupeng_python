from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template("11_base.html")


# 文件的加载
@app.route('/img3')
def img():
    return render_template("13_ShowImg.html")


if __name__ == "__main__":
    app.run(port=8080)
