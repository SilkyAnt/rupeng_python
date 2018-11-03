from flask import Flask,render_template,request,redirect
from DBUtil import PyMySQL
app = Flask(__name__)
db=PyMySQL()
pages=0
@app.route('/')
def hello_world():
    # 计算总的页数=总的条数/每页显示的条数
    #
    sql = "select count(*) from person";
    counts = int(db.getOneData(sql)[0])
    if counts % 3 == 0:
        global pages
        pages = counts // 3
    else:
        pages = counts // 3 + 1
    sql="select * from person"
    tuples=db.getManyData(sql)
    return render_template("index.html",persons=tuples,pageIndex=1,pages=pages)
@app.route("/first")
def first():
    sql = "select * from person limit %s,%s"
    pageIndex=int(request.args.get('pageIndex'))
    tuples = db.getManyData(sql,((pageIndex-1)*3,3,))
    return render_template("index.html", persons=tuples,pageIndex=1,pages=pages)

@app.route("/pre")
def pre():
    sql = "select * from person limit %s,%s"
    pageIndex=int(request.args.get('pageIndex'))
    tuples = db.getManyData(sql,((pageIndex-1)*3,3,))
    return render_template("index.html", persons=tuples,pageIndex=pageIndex,pages=pages)

@app.route("/next")
def next():
    sql = "select * from person limit %s,%s"

    pageIndex=int(request.args.get('pageIndex'))
    tuples = db.getManyData(sql,((pageIndex-1)*3,3,))
    return render_template("index.html", persons=tuples,pageIndex=pageIndex,pages=pages)

@app.route("/last")
def last():
    pageIndex = int(request.args.get('pageIndex'))
    sql = "select * from person limit %s,%s"
    tuples = db.getManyData(sql, ((pageIndex-1)*3, 3,))
    return render_template("index.html", persons=tuples,pageIndex=pageIndex,pages=pages)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
