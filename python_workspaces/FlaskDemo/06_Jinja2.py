from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

class Student():
    def getStuName(self):
        return "张三"

stu = Student()

# 渲染模板最简单的例子
@app.route('/')
def hello_world():
    dict1 = {
        "classNO": "23",
        "classNumber": "50"
    }
    list1 = ["北京", "上海", "深圳", "广东"]
    return render_template("06_Hello.html", username="rupeng", userpwd="123456",
                           dict=dict1, list=list1,stu2 = stu)

# 传递一个变量 再渲染模板
@app.route('/<index>')
def hello_world2(index):
    list1 = ["北京", "上海", "深圳", "广东"]
    return render_template("06_Hello.html", list=list1,myIndex=int(index))


if __name__ == "__main__":
    app.run(port=8080)
