# 文件上传
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

app = Flask(__name__, template_folder="../templates")
app.debug = True
app.secret_key = 'A'


class UploadFile(FlaskForm):
    attach = FileField("请选择上传的文件", validators=[FileRequired(),
                                               FileAllowed(['jpg', 'png'], 'Images only!')])


@app.route("/")
def index():
    form = UploadFile()
    return render_template("Seq_02_FlaskWTF/03_UploadFile.html", form=form)


@app.route("/upload", methods=["get", "post"])
def upload():
    form = UploadFile()
    # print(form.attach.data)
    if form.validate_on_submit():
        filename = form.attach.data.filename
        form.attach.data.save("../static/uploads/" + filename)
        return "ok"
    else:
        return render_template("Seq_02_FlaskWTF/03_UploadFile.html", form=form)


if __name__ == "__main__":
    app.run(port=8080)
