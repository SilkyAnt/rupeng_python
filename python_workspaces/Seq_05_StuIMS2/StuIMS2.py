from flask import Flask, render_template, request, redirect, url_for
from DBUtil import PyMySQL
import os, time

app = Flask(__name__, template_folder="templates")
app.debug = True
db = PyMySQL()

parms = ()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/getAllStu")
def getAllStu():
    gdict = {}
    sql = "select * from stu_table"
    allStus = db.getManyData(sql)
    # print(allStus)
    for s in allStus:
        gid = s[3]
        sql = "select name from grade where id =%s"
        gname = db.getOneData(sql, (gid,))
        # print(gname[0])
        kv = {s[0]: gname[0]}
        gdict.update(kv)
    return render_template("index.html", allStus=allStus, gdict=gdict)


@app.route("/toAdd")
def toAdd():
    sql = "select id,name from grade"
    gnames = db.getManyData(sql)
    return render_template("add.html", gnames=gnames)


@app.route("/AddStu", methods=["get", "post"])
def AddStu():
    name = request.form.get("stu_name")
    age = request.form.get("stu_age")
    gid = request.form.get("stu_grade")
    hobbys = request.form.getlist("stu_hobby")
    hobbys = ",".join(hobbys)
    sex = request.form.get("stu_sex")
    f = request.files["stu_pic"]
    sql = "insert into stu_table(name,age,gradeid,picture,hobby,sex) values(%s,%s,%s,%s,%s,%s)"
    BASE_DIR = os.path.dirname(__file__)
    if db.noQury(sql, (name, age, gid, "imgs/" + f.filename, hobbys, sex)):
        f.save(BASE_DIR + "/static/imgs/" + f.filename)
        # 图片上传有可能没有上传完的时候，页面就跳转到首页，图片有可能显示不出来
        # 解决这个问题有两种方法，1、把上传作为一个独立的单元，等上传执行结束在执行下一步
        # 2、引入模块 time  ，然后执行 time.sleep(3)这个方法。
        return redirect("getAllStu")
    print(name, age, gid, hobbys, sex, f.filename)
    return render_template("add.html")


@app.route("/toUpdate")
def toUpdate():
    sql = "select id,name from grade"
    gnames = db.getManyData(sql)
    # 接收修改学生的ID
    sid = int(request.args.get("sid"))
    print(gnames, sid)
    # 根据学生的ID查询该学生的所有信息
    sql = "select * from stu_table where id = %s"
    lists = db.getManyData(sql, (sid,))
    return render_template("update.html", gnames=gnames, stu=lists[0])


@app.route("/UpdateStu", methods=["get", "post"])
def UpdateStu():
    id = request.form.get("stu_id")
    name = request.form.get("stu_name")
    age = request.form.get("stu_age")
    gid = request.form.get("stu_grade")
    hobbys = request.form.getlist("stu_hobby")
    hobbys = ",".join(hobbys)
    sex = request.form.get("stu_sex")
    oldpic = request.form.get("stu_old_pic")

    try:
        f = request.files["stu_pic"]
        BASE_DIR = os.path.dirname(__file__)
        # 用时间给文件名命名，防止文件名重复
        filename = str(time.time()).replace(".", "")
        f.save(BASE_DIR + "/static/imgs/" + filename + f.filename)
        os.remove(BASE_DIR + "/static/" + oldpic)
        global parms
        parms = (name, age, gid, "imgs/" + f.filename, hobbys, sex, id)
    except:
        print(oldpic)
        parms = (name, age, gid, oldpic, hobbys, sex, id)
    sql = "update stu_table set name = %s,age = %s, gradeid = %s,picture =%s " \
          ",hobby = %s,sex = %s where id = %s"
    if db.noQury(sql, parms):
        return redirect(url_for("getAllStu"))
    else:
        return render_template("error.html")


@app.route("/delStu")
def delStu():
    sid = request.args.get("sid")
    sql = "delete from sut_table where id = %s"
    if db.noQury(sql, (sid,)):
        # 其实值删除了数据库中的记录，但是对应的物理图片没有删除
        # 有兴趣可以自己去实现以下，我是没有时间弄了！
        return redirect(url_for("getAllStu"))
    else:
        return render_template("error.html")


if __name__ == '__main__':
    app.run(port=8080)
