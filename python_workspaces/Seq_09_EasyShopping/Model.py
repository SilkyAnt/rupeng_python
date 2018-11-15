from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:您的数据库密码@172.3.8.234:3306/rupeng"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# KeyError: 'SQLALCHEMY_TRACK_MODIFICATIONS'报错请安装 2.1版本的flask_sqlalchemy包
# 参考链接：https://blog.csdn.net/xiadada2/article/details/79042987
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


class Category(db.Model):
    b_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    b_name = db.Column(db.String(60), nullable=False)
    slists = db.relationship("SmallClass", backref=db.backref("c"))


class SmallClass(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(60), nullable=False)
    b_id = db.Column(db.Integer, db.ForeignKey("category.b_id"))


# db.drop_all()
# db.create_all()

'''
# 添加数据
c1 = Category(b_name="家用电器")

s11 = SmallClass(s_name="电视机")
s12 = SmallClass(s_name="空调")
s13 = SmallClass(s_name="冰箱")
s14 = SmallClass(s_name="热水器")
s15 = SmallClass(s_name="消毒柜")
s16 = SmallClass(s_name="电风扇")
s17 = SmallClass(s_name="饮水机")
s18 = SmallClass(s_name="吸尘器")
s19 = SmallClass(s_name="挂烫机")
s110 = SmallClass(s_name="电话机")
s111 = SmallClass(s_name="收录机")
s112 = SmallClass(s_name="豆浆机")
s113 = SmallClass(s_name="跑步机")
s114 = SmallClass(s_name="血压计")
s115 = SmallClass(s_name="电饭煲")

c1.slists = [s11, s12, s13, s14, s15, s16, s17, s18, s19, s110, s111, s112, s113, s114, s115]

c2 = Category(b_name="书籍")

s21 = SmallClass(s_name="文学")
s22 = SmallClass(s_name="哲学")
s23 = SmallClass(s_name="经济")
s24 = SmallClass(s_name="社会")
s25 = SmallClass(s_name="科学")
s26 = SmallClass(s_name="法律")
s27 = SmallClass(s_name="军事")
s28 = SmallClass(s_name="艺术")
s29 = SmallClass(s_name="漫画")
s210 = SmallClass(s_name="古文")
s211 = SmallClass(s_name="社科")
s212 = SmallClass(s_name="宗教")
s213 = SmallClass(s_name="神话")
s214 = SmallClass(s_name="人文")
s215 = SmallClass(s_name="历史")

c2.slists = [s21, s22, s23, s24, s25, s26, s27, s28, s29, s210, s211, s212, s213, s214, s215]


c3 = Category(b_name="手机数码")

s31 = SmallClass(s_name="苹果")
s32 = SmallClass(s_name="三星")
s33 = SmallClass(s_name="vivo")
s34 = SmallClass(s_name="华为")
s35 = SmallClass(s_name="荣耀")
s36 = SmallClass(s_name="OPPO")
s37 = SmallClass(s_name="中兴")
s38 = SmallClass(s_name="联想")
s39 = SmallClass(s_name="酷派")
s310 = SmallClass(s_name="小米")
s311 = SmallClass(s_name="努比亚")
s312 = SmallClass(s_name="摩托罗拉")
s313 = SmallClass(s_name="魅族")
s314 = SmallClass(s_name="金立")
s315 = SmallClass(s_name="HTC")

c3.slists = [s31, s32, s33, s34, s35, s36, s37, s38, s39, s310, s311, s312, s313, s314, s315]


c4 = Category(b_name="日用百货")

s41 = SmallClass(s_name="礼品")
s42 = SmallClass(s_name="玩具")
s43 = SmallClass(s_name="烟具")
s44 = SmallClass(s_name="药盒")
s45 = SmallClass(s_name="化妆品")
s46 = SmallClass(s_name="药盒")
s47 = SmallClass(s_name="鞋类")
s48 = SmallClass(s_name="塑料")
s49 = SmallClass(s_name="工艺品")
s410 = SmallClass(s_name="炊事")
s411 = SmallClass(s_name="礼品")
s412 = SmallClass(s_name="促销")
s413 = SmallClass(s_name="洗漱")
s414 = SmallClass(s_name="糖果")
s415 = SmallClass(s_name="家居")

c4.slists = [s41, s42, s43, s44, s45, s46, s47, s48, s49, s410, s411, s412, s413, s414, s415]
db.session.add(c1)
db.session.add(c2)
db.session.add(c3)
db.session.add(c4)


db.session.commit()
db.session.close()
'''