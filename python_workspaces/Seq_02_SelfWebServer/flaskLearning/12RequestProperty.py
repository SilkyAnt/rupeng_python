from flask import Flask, render_template,request

app = Flask(__name__, template_folder='../templates', static_folder='', static_url_path='')
app.debug = True

@app.route("/")
def index():
    return render_template("11Login.html")

@app.route("/forms",methods=['GET','POST'])
def getformData():
    print("method"+request.method)
    # 请求headers信息，返回的结果是个list
    print("headers:",request.headers)
    print("url:", request.url)
    print("path:", request.path)
    print("base_url:", request.base_url)
    print("url_root:", request.url_root)
    # WSGI隐含的环境配置
    print("environ:",request.environ)


    return "login success"

if __name__ == '__main__':
    app.run(port=8080)