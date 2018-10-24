from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('03Main.html')

# 遍历数组
@app.route('/for1')
def get_user1():
    return render_template('08_forTemplate.html',
                           comments=['1', '2', '3', '4'])
# 遍历字典
@app.route('/for2')
def get_user2():
    dicts = {
        "中国":"北京",
        "英国":"伦敦",
        "法国":"巴黎",
        "美国":"华盛顿"
    }
    return render_template('08_forTemplate.html',dicts=dicts)

if __name__ == '__main__':
    app.run(debug=True)
