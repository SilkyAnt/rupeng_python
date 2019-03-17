from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='419795232',
    MAIL_PASSWORD='xcywimnfskinbhbj'
)
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject="重要任务", sender='419795232@qq.com', recipients=['1037178580@qq.com'])
    msg.html = "给你一个重要任务！"
    mail.send(msg)
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)
