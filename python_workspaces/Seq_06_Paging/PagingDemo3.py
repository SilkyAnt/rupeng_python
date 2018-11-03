from flask import Flask, render_template, request
from DBUtil import PyMySQL

# 第二次优化过后的代码
app = Flask(__name__)
app.debug = True
db = PyMySQL()
pageSize = 3
pages = 0
lists = []


@app.route("/")
def hello_world():
    # 计算总的页数 = 总的条数/每页显示的条数
    sql = "select count(1) from person"
    counts = int(db.getOneData(sql)[0])

    if counts % pageSize == 0:
        global pages
        pages = counts // pageSize
    else:
        pages = counts // pageSize + 1

    sql = "select * from person limit %s,%s"
    tuples = db.getManyData(sql, (0, pageSize))
    for i in range(1, pages + 1):
        global lists
        lists.append(i)
    return render_template("index03.html", persons=tuples, pageIndex=1, lists=lists)


@app.route("/page")
def page():
    sql = "select * from person limit %s,%s"
    pageIndex = int(request.args.get("pageIndex"))
    if pageIndex <= 0:
        pageIndex = 1
    if pageIndex > pages:
        pageIndex = pages
    tuples = db.getManyData(sql, ((pageIndex - 1) * 3, pageSize))
    return render_template("index03.html", persons=tuples, pageIndex=pageIndex, lists=lists)


if __name__ == "__main__":
    app.run(port=8080)
