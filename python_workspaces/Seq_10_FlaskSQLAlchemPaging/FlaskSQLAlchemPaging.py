from flask import Flask, render_template
from Model import Person

app = Flask(__name__)

current_page_index = 0
total_pages = 0


# 自定义一个分页的方法
def personPaging(pageIndex, pageSize, error_handle=False):
    pageinate = Person.query.order_by("id").paginate(pageIndex, pageSize, error_handle)
    global total_pages, current_page_index
    current_page_index = pageinate.page
    if pageinate.total % pageSize == 0:
        total_pages = pageinate.total % pageSize
    else:
        total_pages = pageinate.total // pageSize + 1
    return pageinate.items


@app.route('/')
def hello_world():
    lists = personPaging(1, 9)
    print(lists)
    return render_template("index.html", lists=lists)


@app.route("/pre")
def pre():
    global current_page_index
    if current_page_index < 2:
        current_page_index = 2
    lists = personPaging(current_page_index - 1, 9)
    return render_template("index.html", lists=lists)


@app.route("/next")
def next():
    global total_pages, current_page_index
    if current_page_index >= total_pages:
        current_page_index = total_pages - 1
    lists = personPaging(current_page_index + 1, 9)
    return render_template("index.html", lists=lists)


@app.route("/last")
def last():
    lists = personPaging(total_pages, 9)
    return render_template("index.html", lists=lists)


if __name__ == '__main__':
    app.run(debug=True)
