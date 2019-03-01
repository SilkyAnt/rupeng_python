# 通过request对象的files实现文件上传
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="../templates")
app.debug = True


@app.route("/")
def index():
    return render_template("13upload.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    print(request.files['files'])
    f = request.files['files']
    print(f.filename)
    f.save("../upload/" + str(f.filename))
    return "文件上传成功!"


if __name__ == "__main__":
    app.run(port=8080)
