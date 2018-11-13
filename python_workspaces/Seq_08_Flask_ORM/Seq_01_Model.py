from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:您的数据库密码@172.3.8.234:3306/rupeng"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


# 如果没有 __tablename__ 赋值
# 类 Person 对应 表名 person。如果类名为 PersonMan ，则表名为 person_man
class Person(db.Model):
    __tablename__ = "personByTableName"
    # 如果有传参，字段映射则为对应参数：p_id
    pid = db.Column("p_id", db.Integer, primary_key=True, autoincrement=True)
    # 如果没有传参，字段名默认为变量名
    pname = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return "%s,%s" % (self.pid, self.pname)


# db.drop_all()
# db.create_all()


'''
# 添加三个对象
p1 = Person(pname="对象一")
p2 = Person(pname="对象二")
p3 = Person(pname="对象三")
db.session.add_all([p1, p2, p3])
'''

'''
# 查询所有的对象
lists = Person.query.all()
print(Person.query)  # 这个就是输出 sql 语句
print(lists)

# 带条件的查询
t = Person.query.filter_by(pname="对象一").first()
print(Person.query.filter_by(pname="对象一"))  # 这个就是输出 sql 语句
print(t)

# 等价于上一条查询
t = Person.query.filter(Person.pname == "对象一").one()

# t = Person.query.limit(2).all()
# t = Person.query.offset(1).all()
# t = Person.query.order_by(Person.pname).all()
# t = Person.query.group_by(Person.pid).all()
# t = Person.query.count()
# t = Person.query.get(2)
'''

'''
# 修改数据
t = Person.query.filter(Person.pid == 2).one()
t.pname = "修改后的名字"
db.session.add(t)

# 删除数据
db.session.delete(t)
'''

db.session.commit()
db.session.close()
