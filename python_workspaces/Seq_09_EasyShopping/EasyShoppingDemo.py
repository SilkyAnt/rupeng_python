from flask import Flask, render_template
from Model import Category

app = Flask(__name__)


@app.route('/')
def hello_world():
    calls = Category.query.all()
    print(calls)
    return render_template("06easyShopping.html", bigalls=calls)


if __name__ == '__main__':
    app.run(debug=True)
