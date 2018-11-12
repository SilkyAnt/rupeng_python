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

    def __repr__(self):
        output = "(%s,%s)" % (self.r_id, self.r_name)
        return output


# many
class User(Base):
    __tablename__ = "user"
    u_id = Column(Integer, primary_key=True, autoincrement=True)
    u_name = Column(String(40), nullable=False)
    u_r_id = Column(Integer, ForeignKey("role.r_id"))

    # 定义many-to-one 关系
    role = relationship("Role", backref=backref("users"), cascade="all,delete")

    def __repr__(self):
        output = "(%s,%s,%s)" % (self.u_id, self.u_name, self.role.r_id)
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