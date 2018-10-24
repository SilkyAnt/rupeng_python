from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

# 上下文中的request变量
@app.route('/user/<username>')
def get_user(username):
    user = load_user(username)
    return render_template("07_ifTemplate.html", user=user)


def load_user(username):
    if username == "admin":
        return "管理员"
    else:
        return None


if __name__ == '__main__':
    app.run(port = 8080)
