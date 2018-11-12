import pymysql
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

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

    def __repr__(self):
        output = "(%s,%s,%s)" % (self.u_id, self.u_name, self.u_r_id)
        return output


Base.metadata.create_all(engine)
