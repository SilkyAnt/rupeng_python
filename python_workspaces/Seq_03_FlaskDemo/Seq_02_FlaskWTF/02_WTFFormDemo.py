# 安装包 pip install flask-wtf
from flask import Flask, render_template
# 引入模块
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, \
    IntegerField, DecimalField, DateField, RadioField, SelectField, \
    SelectMultipleField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange

app = Flask(__name__, template_folder="../templates")
app.debug = True
app.secret_key = "1"


# 声明一个表单的类，它的父类是FlaskForm
class SingleForm(FlaskForm):
    # 定义字段
    username = StringField("请输入用户名", validators=[DataRequired(message="内容不能为空！")])
    email = StringField("请输入电子信息", validators=[Email()])
    password = PasswordField("请输入密码：", validators=[DataRequired()])
    repwd = PasswordField("请再次输入密码", validators=[EqualTo("password", message="两次密码输入的值要相同！")])
    age = IntegerField("请输入年龄", validators=[NumberRange(min=16, max=70, message="年龄范围在16-70之间！")])
    height = DecimalField("请输入身高，单位为厘米")
    birthdate = DateField("请输入出生年月", format="%Y-%m-%d")
    gender = RadioField("请选择性别", default="f",choices=[("m", "Male"), ("f", "Female")], validators=[DataRequired()])
    job = SelectField("请选择工作类型", choices=[
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('engineer', 'Engineer'),
        ('lawyer', 'Lawyer')
    ])
    # 不知道为啥，页面渲染的内容不能多选(待解决)
    hobby = SelectMultipleField("请选择爱好", choices=[
        ('swim', 'Swimming'),
        ('skate', 'Skating'),
        ('hike', 'Hiking')
    ])
    description = TextAreaField("请自我介绍")
    # Checkbox类型，加上default='checked'即默认是选上的
    accept_terms = BooleanField("请接受以上条例", default='checked',
                                validators=[DataRequired()])
    # Submit按钮
    submit = SubmitField("注册")


@app.route("/reg", methods=["get", "post"])
def register():
    # 创建一个表单对象
    form = SingleForm()
    # 如果已通过验证
    if form.validate_on_submit():
        # 获取表单对象中的user字段的值
        return "OK"
    else:
        print("error")
        print(form.username.errors)
        return render_template("Seq_02_FlaskWTF/02_Register.html", form=form)


if __name__ == "__main__":
    app.run(port=8080)
