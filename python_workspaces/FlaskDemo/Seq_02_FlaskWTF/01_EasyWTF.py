# 安装包 pip install flask-wtf
from flask import Flask, render_template

# 引入模块
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,length

app = Flask(__name__, template_folder="../templates")
app.debug = True
app.secret_key = "1"


# 声明一个表单的类，它的父类是FlaskForm
class SingleForm(FlaskForm):
    # 定义一个字段
    user = StringField("请输入用户名", validators=[DataRequired(message="内容不能为空！")])
    nick = StringField("请输入昵称",validators=[length(min=6,max=10,message="长度在6-10之间")])


@app.route("/login", methods=["get", "post"])
def login():
    # 创建一个表单对象
    form = SingleForm()
    # 如果已通过验证
    if form.validate_on_submit():
        # 获取表单对象中的user字段的值
        username = form.data['user']
        if username == "admin":
            return "Admin login successfully!"
        else:
            return "Wrong user!"
    else:
        return render_template("Seq_02_FlaskWTF/01_Login.html", form=form)


if __name__ == "__main__":
    app.run(port=8080)
