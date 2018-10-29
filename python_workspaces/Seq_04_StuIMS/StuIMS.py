from flask import Flask, render_template, redirect, url_for, request
from DBUtil import PyMySQL

app = Flask(__name__)

app.debug = True
db = PyMySQL()


@app.route("/toAdd")
def toAdd():
    return render_template("add.html")


@app.route("/Add", methods=["get", "post"])
def addStu():
    name = request.form["name"]
    address = request.form["address"]
    sql = "insert into stu(s_name,s_address) value(%s,%s)"
    if db.noQury(sql, (name, address)):
        # return "数据插入成功！"
        return redirect(url_for("getAllStus"))
    else:
        return redirect(url_for("toAdd"))

    # return name+" " + address
    # return redirect(url_for("getAllStus"))


@app.route("/delStu", methods=["get", "post"])
def delStu():
    sid = int(request.args.get("sid"))
    sql = "delete from stu where s_id = %s"
    if db.noQury(sql, (sid,)):
        return redirect(url_for("getAllStus"))
    else:
        return "delete error"


@app.route("/toUpdate")
def toUpdate():
    sid = int(request.args.get("sid"))
    print(sid)
    sql = "select * from stu where s_id = %s"
    stu = db.getOneData(sql, (sid,))
    return render_template("update.html", stu=stu)


@app.route("/updateStu", methods=["get", "post"])
def updateStu():
    id = int(request.form.get("sid"))
    name = request.form.get("sname")
    address = request.form.get("saddress")
    # print(id, name, address)
    sql = "update stu set s_name=%s,s_address=%s where s_id = %s"
    if db.noQury(sql, (name, address, id)):
        return redirect(url_for("getAllStus"))
    else:
        return redirect(url_for("toUpdate"))


@app.route("/")
def getAllStus():
    sql = "select * from stu"
    students = db.getManyData(sql)
    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(port=8080)
