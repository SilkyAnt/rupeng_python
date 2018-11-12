# encoding=utf8
import pymysql
from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

# 初始化数据库连接:
engine = create_engine("mysql+mysqldb://root:您的数据库密码@172.3.8.234:3306/rupeng?charset=utf8", echo=True)
conn = engine.connect()
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
# 获取数据库和ORM框架之间的会话对象
session = DBSession()
print(session)


# 描述表和类之间的映射关系，其类的父类是Base
class User(Base):
    # 类名对应的表名
    __tablename__ = "user"
    # Column 的 第一个属性，例如 "name" 可以省略，省略之后会默认为 name
    name = Column("name", String(40))
    # Column 的 第一个属性，例如 "id" 可以省略，省略之后会默认为 id
    id = Column("id", Integer, primary_key=True)
    address = Column("address", String(40))

'''
u = User(name="huy", id=123, address="北京海淀")
# 添加对象
session.add(u)

# 查找对象
u2 = session.query(User).get(123)
# print(u2.id, u2.name, u2.address)

# 删除对象
# session.delete(u2)

# 修改对象
session.query(User).filter(User.id == 123).update({User.name: "ggggg"})
'''


# 查询记录的总记录数
print(session.query(User).count())
lists = session.query(User).all()
for u in lists:
    print(u.id, u.name, u.address)

# 提交
session.commit()
