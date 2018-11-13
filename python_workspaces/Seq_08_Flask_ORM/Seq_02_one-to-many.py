from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:您的数据库密码@172.3.8.234:3306/rupeng"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = True


# 定义一个 one-to-many 的实体映射关系
class Person(db.Model):
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pname = db.Column(db.String(40), nullable=True)
    address = db.relationship("Address", backref=db.backref("person"))
    def __repr__(self):
        return "%s,%s,%s" %(self.pid,self.pname,self.address)


class Address(db.Model):
    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aname = db.Column(db.String(60), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey("person.pid"))
    def __repr__(self):
        return "%s,%s" %(self.aid,self.aname)


'''
db.drop_all()
db.create_all()

a1 = Address(aname="北京昌平")
a2 = Address(aname="北京海淀")
a3 = Address(aname="北京顺义")
a4 = Address(aname="北京天安门")

p1 = Person(pname="刘虎")
p2 = Person(pname="老六")

p1.address = [a1, a2]
p2.address = [a3, a4]

# 因为级联映射，所以地址会自动保存
db.session.add(p1)
db.session.add(p2)
'''

p1 = Person.query.filter_by(pid=1).one()
print(p1)

a1 = Address.query.filter(Address.aid == 3).one()
print(a1.person.pname)

db.session.commit()
db.session.close()
