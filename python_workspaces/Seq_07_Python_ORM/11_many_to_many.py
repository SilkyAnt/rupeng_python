from sqlalchemy import String, Column, Integer, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship
import pymysql

pymysql.install_as_MySQLdb()

engine = create_engine("mysql+mysqldb://root:您的数据库密码@172.3.8.234:3306/rupeng?charset=utf8", echo=True)
Base = declarative_base(bind=engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()


# 定义多对多的映射关系
class Host(Base):
    __tablename__ = "host"
    h_id = Column(Integer, primary_key=True, autoincrement=True)
    h_name = Column(String(50))
    h_port = Column(String(20))
    h_ip = Column(String(60))


class Owner(Base):
    __tablename__ = "owner"
    o_id = Column(Integer, primary_key=True, autoincrement=True)
    o_name = Column(String(60), nullable=True)


class Host_Owner(Base):
    __tablename__ = "host_owner"
    id = Column(Integer, primary_key=True, autoincrement=True)
    h_id = Column(Integer, ForeignKey("host.h_id"))
    o_id = Column(Integer, ForeignKey("owner.o_id"))
    # 配置多对多的关系
    host = relationship("Host", backref=backref("host_hostowner"))
    owner = relationship("Owner", backref=backref("owner_hostowner"))


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

'''
# 添加数据
session.add_all([
    Host(h_name='c1', h_port='22', h_ip='1.1.1.1'),
    Host(h_name='c2', h_port='22', h_ip='1.1.1.2'),
    Host(h_name='c3', h_port='22', h_ip='1.1.1.3'),
    Host(h_name='c4', h_port='22', h_ip='1.1.1.4'),
    Host(h_name='c5', h_port='22', h_ip='1.1.1.5'),
])
session.add_all([
    Owner(o_name='root'),
    Owner(o_name='admin'),
    Owner(o_name='power'),
    Owner(o_name='user'),
])

session.add_all([
    Host_Owner(h_id=1, o_id=1),
    Host_Owner(h_id=1, o_id=2),
    Host_Owner(h_id=1, o_id=3),
    Host_Owner(h_id=2, o_id=2),
    Host_Owner(h_id=2, o_id=4),
    Host_Owner(h_id=2, o_id=3),
])
session.commit()
session.close()
'''

# 1、正常简单的查询
h1 = session.query(Host).filter(Host.h_name == 'c2').one()

# 2、根据 h_id 查询 o_id
owner_list = session.query(Host_Owner.o_id).filter(Host_Owner.h_id == 2).all()
print(owner_list)

# 3、根据 o_id 查询所使用的 h_name,这种情况下是没有配置多对多的关系
hid = session.query(Host_Owner.h_id).filter(Host_Owner.o_id.in_([2, 3, 4])).all()
print(hid)
for id in hid:
    hname = session.query(Host).filter(Host.h_id == id[0]).one()
    print(hname.h_name)

# 4、根据 o_id 查询所使用的 h_name
hos = session.query(Host_Owner).filter(Host_Owner.o_id == 2).all()
for t in hos:
    print(t.host.h_id)

# 5、查找服务器上有哪些用户
# 第一步：查找一个服务器
h1 = session.query(Host).filter(Host.h_id == 3).one()
# 第二步：反向引用这个主机的 Host_Owner 对象
for t in h1.host_hostowner:
    # 第三步：通过 Host_Owner 对象访问 Owner
    # 第四步：通过 Owner 对象访问 Owner 的 name
    print(t.owner.o_name)

# 6、查找此用户有哪些服务器
# 第一步：查找一个用户
owner = session.query(Owner).filter(Owner.o_id == 2).one()
for t in owner.owner_hostowner:
    print(t.host.h_name)

session.commit()
session.close()
