from sqlalchemy import String, Integer, create_engine, Column, ForeignKey
from sqlalchemy.orm import backref, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import warnings

warnings.filterwarnings("ignore")
pymysql.install_as_MySQLdb()

engine = create_engine("mysql+mysqldb://root:您的数据库密码@172.3.8.234:3306/rupeng?charset=utf8", echo=True)
Base = declarative_base(bind=engine)
DBsession = sessionmaker()
session = DBsession()


class Husband(Base):
    __tablename__ = 'husband'
    h_id = Column(Integer, primary_key=True, autoincrement=True)  # 主键，自增
    h_name = Column(String(10))
    # 定义了一个one-to-one:
    wife = relationship("Wife", backref=backref("husband"), uselist=False, cascade="all,delete")

    def __repr__(self):
        output = "(%s,%s)" % (self.h_id, self.h_name)
        return output


class Wife(Base):
    __tablename__ = 'wife'
    w_id = Column(Integer, primary_key=True, autoincrement=True)
    w_name = Column(String(10), nullable=False)

    w_h_id = Column(Integer, ForeignKey('husband.h_id'))  # 外键关联

    def __repr__(self):
        output = "(%s,%s,%s)" % (self.w_id, self.w_name, self.w_h_id)
        return output


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

'''
# 添加妻子数据
r1 = Wife(w_name='w1')
r2 = Wife(w_name='w2')
r3 = Wife(w_name='w3')
r4 = Wife(w_name='w4')
r5 = Wife(w_name='w5')
# 添加丈夫数据
user1 = Husband(h_name='fuzj', wife=r1)
user2 = Husband(h_name='jie', wife=r2)
user3 = Husband(h_name='张三', wife=r3)
user4 = Husband(h_name='李四', wife=r4)
user5 = Husband(h_name='王五', wife=r5)

# 因为是级联默认是save-update，在添加丈夫的同时，会同时添加与它关联的妻子
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.add(user5)
session.commit()
session.close()
'''

'''
# 查询 husband -> wife
h1 = session.query(Husband).filter(Husband.h_id == 3).one()
# 查询 wife -> husband
w1 = session.query(Wife).filter(Wife.w_id == 2).one()
'''

'''
# 修改前
# h2->w1 w1->h1
# h2->w2 w2->h2
# 修改后
# h1->w2 w2->h1
# h2->w1 w1->h2
h1 = session.query(Husband).filter(Husband.h_id == 1).one()
h2 = session.query(Husband).filter(Husband.h_id == 2).one()

w1 = session.query(Wife).filter(Wife.w_id == 1).one()
w2 = session.query(Wife).filter(Wife.w_id == 2).one()
# 正向访问
h1.wife = w2
h2.wife = w1

# 反向访问
# w1.husband = h1
# w2.husband = h2
session.add(h1)
session.add(h2)
session.commit()
session.close()
'''


# 删除操作
h1 = session.query(Husband).filter(Husband.h_id == 2).one()
session.delete(h1)
session.commit()
session.close()
