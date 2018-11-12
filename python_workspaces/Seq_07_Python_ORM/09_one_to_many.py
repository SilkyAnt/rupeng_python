import pymysql
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref

pymysql.install_as_MySQLdb()
engine = create_engine("mysql+mysqldb://root:您的数据库密码@172.3.8.234:3306/rupeng?charset=utf8", echo=True)
dbSession = sessionmaker(bind=engine)
session = dbSession()

Base = declarative_base()


# one
class Role(Base):
    __tablename__ = "role"
    r_id = Column(Integer, primary_key=True, autoincrement=True)
    r_name = Column(String(10))

    # 配置one-to-many
    users = relationship("User", backref=backref("role"))

    def __repr__(self):
        output = "(%s,%s)" % (self.r_id, self.r_name)
        return output


# many
class User(Base):
    __tablename__ = "user"
    u_id = Column(Integer, primary_key=True, autoincrement=True)
    u_name = Column(String(40), nullable=False)
    u_r_id = Column(Integer, ForeignKey("role.r_id"))

    def __repr__(self):
        output = "(%s,%s,%s)" % (self.u_id, self.u_name, self.role)
        return output


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# 填充数据
'''
r1 = Role(r_name="adb")
r2 = Role(r_name="system")
r3 = Role(r_name="user")
session.add(r1)
session.add(r2)
session.add(r3)

session.add_all([
    User(u_name="刘华", role=r1),
    User(u_name="黄河", role=r2),
    User(u_name="程虎", role=r1),
    User(u_name="湖光", role=r2),
    User(u_name="共同", role=r3),
    User(u_name="刘胡亚", role=r2),
    User(u_name="必要", role=r3),
    User(u_name="公关", role=r1)
])

session.commit()
session.close()
'''
'''
# 正向查询 one->many role->user
r1 = session.query(Role).filter(Role.r_id == 3).one()
for u in r1.users:
    print(u.u_id, u.u_name, u.u_r_id)

# 反向查询
u1 = session.query(User).filter(User.u_id == 4).one()
print(u1.role.r_id, u1.role.r_name)
'''

'''
# 修改
u2 = session.query(User).filter(User.u_id == 2).one()
r3 = session.query(Role).filter(Role.r_id == 3).one()
u2.role = r3
'''

'''
# 删除
u2 = session.query(User).filter(User.u_id == 1).one()
session.delete(u2)
'''

r2 = session.query(Role).filter(Role.r_id == 1).one()
# 不指定级联删除，默认删除是置空
session.delete(r2)

session.commit()
session.close()
