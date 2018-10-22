from flask import Flask,render_template

app = Flask(__name__,template_folder='../templates',static_folder='', static_url_path='')
app.debug = True

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/')
def index():
    return render_template("01Hello.html")

if __name__ == '__main__':
    app.run(port=8080)