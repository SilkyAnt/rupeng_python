from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:您的数据库密码@172.3.8.234:3306/rupeng"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = True

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
                )


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
                           backref=db.backref('pages', lazy='dynamic'))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# db.create_all()
'''
p1 = Page(id=1)
p2 = Page(id=2)
p3 = Page(id=3)

t1 = Tag(id=1)
t2 = Tag(id=2)
t3 = Tag(id=3)
p1.tags = [t1, t2]
p2.tags = [t2, t3]
p3.tags = [t1, t3]
db.session.add_all([p1, p2, p3])
'''

p1 = Page.query.filter_by(id=2).one()
print(p1.tags)

db.session.commit()
db.session.close()
