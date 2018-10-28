from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "jianglp"


@app.route('/')
def helllo_world():
    try:
        if session["loginAdmin"] == "admin":
            return render_template("03Main.html")
        else:
            return render_template("03Login.html")
    except:
        return render_template("03Login.html")

    return render_template("03Login.html")


@app.route("/formData")
def getUser():
    name = request.values.get("username")
    pwd = request.values.get("userpwd")
    if name == "admin" and pwd == "123456":
        session["loginAdmin"] = "admin"
        return render_template("03Main.html")
    else:
        return render_template("03Login.html")
    print(name, pwd)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
