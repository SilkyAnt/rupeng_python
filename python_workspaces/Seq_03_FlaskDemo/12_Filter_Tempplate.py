from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template("11_base.html")


@app.route('/filter')
def f():
    return render_template("12_Filter.html",name="winston")


if __name__ == "__main__":
    app.run(port=8080)
