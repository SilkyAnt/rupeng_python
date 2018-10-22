from flask import Flask,abort

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

def getuser(id):
    if id == "1":
        return "UserID"
    else:
        return None

@app.route('/user/<id>')
def user(id):
    u = getuser(id)
    if u:
        return "hello,%s" %u
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
