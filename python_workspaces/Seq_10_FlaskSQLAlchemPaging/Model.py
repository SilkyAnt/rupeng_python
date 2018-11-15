from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

# 分页功能
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:您的数据库密码@172.3.8.234:3306/rupeng"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# KeyError: 'SQLALCHEMY_TRACK_MODIFICATIONS'报错请安装 2.1版本的flask_sqlalchemy包
# 参考链接：https://blog.csdn.net/xiadada2/article/details/79042987
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return "%s,%s,%s" % (self.id, self.name, self.address)


# db.drop_all()
# db.create_all()


'''
# 添加数据
for i in range(1, 101, 1):
    p = Person(id=i, name="czf" + str(i), address="北京昌平" + str(i))
    db.session.add(p)
db.session.commit()
db.session.close()
'''

'''
palls = Person.query.order_by("id").paginate(7, 9, False)
print(palls.items)
print(palls.total)
print(palls.pages)
print(palls.has_next)
print(palls.has_prev)
print(palls.next)
print(palls.next_num)
print(palls.page)
'''