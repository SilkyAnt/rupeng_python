from flask import Flask, make_response, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_word():
    resp = make_response('<a href="%s">page2</a>' % '/getCookie')
    resp.set_cookie("user", "rupeng")
    return resp


@app.route('/getCookie')
def getCookie():
    print(request.cookies.__len__())
    for k1 in request.cookies:
        print(k1, request.cookies[k1])
    return request.cookies['user']


if __name__ == '__main__':
    app.run()
