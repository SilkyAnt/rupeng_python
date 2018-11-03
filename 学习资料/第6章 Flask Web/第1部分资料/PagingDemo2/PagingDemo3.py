from flask import Flask,render_template,request,redirect
from DBUtil import PyMySQL
app = Flask(__name__)
db=PyMySQL()
pages=0
list1=[]
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
    sql="select * from person limit 0,3"
    tuples=db.getManyData(sql)

    for i in range(1,pages+1):
        global list1
        list1.append(i)
    print(list1)
    return render_template("index4.html",persons=tuples,pageIndex=1,pages=pages,list1=list1)

@app.route("/page")
def page():
    sql = "select * from person limit %s,%s"
    pageIndex=int(request.args.get('pageIndex'))
    if pageIndex<=0:
        pageIndex=1
    if pageIndex>pages:
        pageIndex=pages

    tuples = db.getManyData(sql,((pageIndex-1)*3,3,))
    return render_template("index4.html", persons=tuples,pageIndex=pageIndex,pages=pages,list1=list1)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
