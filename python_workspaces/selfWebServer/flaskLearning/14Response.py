# 学习 Response
from flask import Flask,make_response

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return "hello,world"

@app.route("/ping")
def ping():
    return "hello,world",200,{"Content-Type":"text/css"}

@app.route("/res")
def res():
    res = make_response("response")
    res.mimetype = "text/pain"
    res.headers["x-tag"] = "sth.img"
    res.status_code = 404
    return res

if __name__=="__main__":
    app.run(port=8080)
