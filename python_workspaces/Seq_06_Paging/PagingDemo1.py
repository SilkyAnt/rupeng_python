from flask import Flask, render_template, request
from DBUtil import PyMySQL

# 没有优化的代码
app = Flask(__name__)
app.debug = True
db = PyMySQL()
pageSize = 3


@app.route("/")
def hello_world():
    sql = "select * from person"
    tuples = db.getManyData(sql)
    return render_template("index01.html", persons=tuples, pageIndex=1)


@app.route("/first")
def first():
    sql = "select * from person limit %s,%s"
    pageIndex = int(request.args.get("pageIndex"))
    tuples = db.getManyData(sql, ((pageIndex - 1) * 3, pageSize))
    return render_template("index01.html", persons=tuples, pageIndex=pageIndex)


@app.route("/pre")
def pre():
    sql = "select * from person limit %s,%s"
    pageIndex = int(request.args.get("pageIndex"))
    tuples = db.getManyData(sql, ((pageIndex - 1) * 3, pageSize))
    return render_template("index01.html", persons=tuples, pageIndex=pageIndex)


@app.route("/next")
def next():
    sql = "select * from person limit %s,%s"
    pageIndex = int(request.args.get("pageIndex"))
    tuples = db.getManyData(sql, ((pageIndex - 1) * 3, pageSize))
    return render_template("index01.html", persons=tuples, pageIndex=pageIndex)


@app.route("/last")
def last():
    # 计算总的页数 = 总的条数/每页显示的条数
    sql = "select count(1) from person"
    counts = int(db.getOneData(sql)[0])

    if counts % pageSize == 0:
        pages = counts // pageSize
    else:
        pages = counts // pageSize + 1

    sql = "select * from person limit %s,%s"
    tuples = db.getManyData(sql, ((pages - 1) * pageSize, pageSize))
    return render_template("index01.html", persons=tuples, pageIndex=pages)


if __name__ == "__main__":
    app.run(port=8080)
